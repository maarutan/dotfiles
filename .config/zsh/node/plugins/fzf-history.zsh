#!/usr/bin/env zsh
# ┌─┐┌─┐┌─┐  ┬ ┬┬┌─┐┌┬┐┌─┐┬─┐┬ ┬
# ├┤ ┌─┘├┤───├─┤│└─┐ │ │ │├┬┘└┬┘
# └  └─┘└    ┴ ┴┴└─┘ ┴ └─┘┴└─ ┴ 
#--------------------------------------------
# (c) maarutan   https://github.com/maarutan


#fzf history
bindkey -r '^H'
bindkey '^H' fzf_history_search


#zsh history

bindkey -r '^N'
bindkey '^N' history-beginning-search-forward # ctrl + n

bindkey -r '^P'
bindkey '^P' history-beginning-search-backward # ctrl + p



