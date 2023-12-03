set nocompatible    "Need it for Vundle
filetype off        "Need it for Vundle

"set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
Plugin 'VundleVim/Vundle.vim'      "https://github.com/VundleVim/Vundle.vim
Plugin 'dpelle/vim-LanguageTool'   "https://github.com/dpelle/vim-LanguageTool
Plugin 'luochen1990/rainbow'       "https://github.com/luochen1990/rainbow
Plugin 'itchyny/lightline.vim'     "https://github.com/itchyny/lightline.vim
Plugin 'lifepillar/vim-solarized8' "https://vimawesome.com/plugin/solarized-8
call vundle#end()

colorscheme solarized8          "Enable colorscheme

"Configure lightline
let g:lightline = {
      \ 'colorscheme': 'solarized',
      \ }

"Configure rainbow 
let g:rainbow_active = 1
let g:tex_flavor = 'latex'
let g:rainbow_load_separately = [
    \ [ '*' , [['(', ')'], ['\[', '\]'], ['{', '}']] ],
    \ [ '*.tex' , [['(', ')'], ['\[', '\]']] ],
    \ [ '*.cpp' , [['(', ')'], ['\[', '\]'], ['{', '}']] ],
    \ [ '*.{html,htm}' , [['(', ')'], ['\[', '\]'], ['{', '}'], ['<\a[^>]*>', '</[^>]*>']] ],
    \ ]
let g:rainbow_guifgs = ['RoyalBlue3', 'DarkOrange3', 'DarkOrchid3', 'FireBrick']
let g:rainbow_ctermfgs = ['lightblue', 'lightgreen', 'yellow', 'red', 'magenta']
"End configure rainbow
