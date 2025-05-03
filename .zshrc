#!/usr/bin/env zsh

export ZSH_CONFIG="$HOME/.config/zsh"
source $ZSH_CONFIG/init


# pnpm
export PNPM_HOME="/home/maaru/.local/share/pnpm"
case ":$PATH:" in
  *":$PNPM_HOME:"*) ;;
  *) export PATH="$PNPM_HOME:$PATH" ;;
esac
# pnpm end
