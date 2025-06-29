#!/bin/zsh

NAME="antidote"
HOST="mattmc3"
REPO="https://github.com/$HOST/$NAME.git"

PLUGIN_MANAGER_DIR="$HOME/.local/share/$NAME"
CURRENT_DECLARATIONS_FILE="$(realpath "$0")"
ZSH_PLUGINS_BASE="${CURRENT_DECLARATIONS_FILE%/*}/plugins_list"
ZSH_PLUGINS_FILE="${ZSH_PLUGINS_BASE}.txt"

CACHE_DIR="${CURRENT_DECLARATIONS_FILE%/*}/.cache"
mkdir -p "$CACHE_DIR"
ZSH_BUNDLE_CACHE="${CACHE_DIR}/.antidote_cache.zsh"

ZSH_AFTER_FILE="${ZSH_PLUGINS_BASE}_after.zsh"

if [[ ! -d "$PLUGIN_MANAGER_DIR" ]]; then
    if ! command -v git >/dev/null 2>&1; then
        echo "Git not found. Cannot install Antidote."
        exit 1
    fi
    mkdir -p "$PLUGIN_MANAGER_DIR"
    git clone --depth=1 "$REPO" "$PLUGIN_MANAGER_DIR"
fi

ANTIDOTE_ENTRY="$PLUGIN_MANAGER_DIR/$NAME.zsh"
if [[ ! -f "$ANTIDOTE_ENTRY" ]]; then
    echo "❌ $NAME: couldn't find $ANTIDOTE_ENTRY"
    echo "Check the repository or script path."
    exit 1
fi

source "$ANTIDOTE_ENTRY"
autoload -Uz antidote

[[ -f "$ZSH_PLUGINS_FILE" ]] || touch "$ZSH_PLUGINS_FILE"
[[ -f "$ZSH_BUNDLE_CACHE" ]] || touch "$ZSH_BUNDLE_CACHE"

OLD_LIST="$(mktemp)"
NEW_LIST="$(mktemp)"

grep '^# Bundling' "$ZSH_BUNDLE_CACHE" | sed 's/# Bundling //' | sort > "$OLD_LIST"
sort "$ZSH_PLUGINS_FILE" > "$NEW_LIST"

ADDED=()
REMOVED=()

while IFS= read -r line; do
    grep -Fxq "$line" "$OLD_LIST" || ADDED+=("$line")
done <"$NEW_LIST"

while IFS= read -r line; do
    grep -Fxq "$line" "$NEW_LIST" || REMOVED+=("$line")
done <"$OLD_LIST"

if [[ ! -s "$ZSH_BUNDLE_CACHE" || "$ZSH_PLUGINS_FILE" -nt "$ZSH_BUNDLE_CACHE" ]]; then
    echo -e "\n🔄 Regenerating Antidote plugin cache..."
    echo "---------------------------------------------"

    [[ ${#ADDED[@]} -gt 0 ]] && {
        echo -e "\n➕ Added plugins:"
        for plugin in "${ADDED[@]}"; do
            echo "   → $plugin"
        done
    }

    [[ ${#REMOVED[@]} -gt 0 ]] && {
        echo -e "\n➖ Removed plugins:"
        for plugin in "${REMOVED[@]}"; do
            echo "   ← $plugin"
        done
    }

    [[ ${#ADDED[@]} -eq 0 && ${#REMOVED[@]} -eq 0 ]] && {
        echo -e "\n⚠️  No visible changes, but rebuilding (mtime)."
    }

    antidote bundle < "$ZSH_PLUGINS_FILE" > "$ZSH_BUNDLE_CACHE"

    echo -e "\n✅ Done regenerating plugin cache."
    echo "---------------------------------------------"
fi

rm -f "$OLD_LIST" "$NEW_LIST"

source "$ZSH_BUNDLE_CACHE"
[[ -f "$ZSH_AFTER_FILE" ]] && source "$ZSH_AFTER_FILE"

