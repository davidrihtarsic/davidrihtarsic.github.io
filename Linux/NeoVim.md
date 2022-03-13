# NEOVIM

## Avtomatsko popravljanje napak

najprej si zapomnimo mesto kjer smo `ms`, nato s spell-check-erjem najdemo napako `[s`, iz menuja izberemo 1. predlog `1z=` in skočimo nazaj na masto "s" `'s`  

```bash
:normal!  ms[s1z=`s<CR>
```

## Save vim session
Zapimni si vse odprte dokumente:

```bash
:mksession! ~/.config/nvim/david_session.sav
```
## TO-DO

:buffers to dmenu? in nato izvereš v  kateri buffer bi šel...

## PLUGINS

### YouCompleteMe

najpreje sem v init.vim dodol plugin

    Plug 'ycm-core/YouCompleteMe'

Greš v folder ~/.vim/plugged/YouCompleteMe/

    python3 install.py --all

> mislim, da potem dela tako kot mora... juhej.
