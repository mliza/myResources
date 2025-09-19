filetype plugin indent on       "Enable filetype-specific
syntax on                       "Enable syntax color
syntax spell toplevel           "Allow spell on .txt files
set spelllang=en_us             "Allows spell to be in English
set encoding=utf-8              "Enable encoding
set background=dark             "Enable contrast
set number                      "Show line numbers
set nolist                      "Hide end of line characters
set relativenumber              "Show relative line numbers
set expandtab                   "Use space instead of tab
set tabstop=4                   "Width of tab character
set softtabstop=4               "Fine tunes the amount of white space
set shiftwidth=4                "White space to add in normal mode
set textwidth=79                "Text wrap width
set wrap                        "Allow text to wrap
set autoindent                  "Autoindent in new line
set linebreak                   "Avoid wrapping a line in the middle of a word
set nobackup                    "Doesn't create backup files
set noswapfile                  "Doesn't create noswapfile files
set smartindent                 "Indent text
set title                       "Reflects file currently being working
set backspace=indent,eol,start  "Allow backspacing over indentation
set hlsearch                    "Enable search highlight
set history=1000                "Increase the undo limit
set ignorecase                  "Ignore capital letters during search
set showmatch                   "Show matching parenthesis
set smartcase                   "Allows uppercase in search
set incsearch                   "Allows to start search before finishing word
set colorcolumn=80              "Add a colored column at 90
set ruler                       "Insert numbers
set showcmd                     "Show (partial) command in bottom-right
set cursorline                  "Highlight current line
set cursorcolumn                "Highlight current column
set wildmenu                    "Visual autocomplete for command menu
set spell                       "Enable spell
set foldenable                  "Enable folding
set foldmethod=manual           "Enable folding base on indentation 
set laststatus=3                "Status Bar modified
set belloff=all                 "Kill error bell sound
set visualbell                  "Use visualbell instead of error bell sound
set splitbelow                  "Split screens below
set showmode                    "Show the mode you are on the last line
set noscrollbind                "Disable scroll binding
set nocursorbind                "Disable cursor binding
set clipboard=unnamed           "Defaults clipboard to system clipboard (for linux use unnamedplus)
set ff=unix                     "Sets the editor to use unix ending line
set gp=git\ grep\ -n            "Set source repo to see where words are repeating
set tags=tags                   "Set tags
let mapleader = " "             "Setup leader
"set list                        "Set trailing white space
"set mouse=a                     "Enable mouse

"Moving between different windows
nnoremap <leader>h :wincmd h<CR>
nnoremap <leader>j :wincmd j<CR>
nnoremap <leader>k :wincmd k<CR>
nnoremap <leader>l :wincmd l<CR>

"Disable ignore search when is uppercase
nnoremap <CR> :nohlsearch<cr>

"Disable search highlight using escape
nnoremap <esc> :nohlsearch<CR>

"Open terminal below shortcut
nnoremap <leader>\t :terminal ++rows=6<CR>

"Remove DOS line ending
nnoremap <leader>\rl :e ++ff=dos<CR>

"Move to the beginning, the end of the line and delete up to cursor
nnoremap B ^
nnoremap E $
nnoremap <leader>B g^
nnoremap <leader>E g$
nnoremap <leader>d d^

"Move between tabs
nnoremap <C-j> :bprev<CR>                                                                            
nnoremap <C-k> :bnext<CR>

"Disables automatic commenting on newline
autocmd FileType * setlocal formatoptions-=c formatoptions-=r formatoptions-=o

"Allow single line always 
noremap j gj
noremap k gk

"Copy and past files to clipboard
noremap <C-c> "+y
noremap <C-x> "+d
noremap <C-p> "+p

"Highlight the last inserted text
nnoremap gV '[V']

"Load and save view automatically 
autocmd BufWinLeave * if &diff | diffoff | endif | mkview

"Mark trailing spaces as errors
match ErrorMsg '\s\+$'

"Write and compile latex on background 
nnoremap <leader>\c :call system('pdflatex *.tex')<CR>
nnoremap <leader>\wc :w <bar> :call system('pdflatex *.tex')<CR>
"Change colors on vimdiff 
"cterm-sets the style, ctermfg-sets the txt color, ctermbg-set the highlight
"DiffAdd-added line, DiffDelete-removed line, DiffChange-part of changed line
"DiffText-exact part of the text that was deleted 
highlight DiffAdd    cterm=bold ctermfg=10 ctermbg=17 gui=none guifg=bg guibg=Red
highlight DiffDelete cterm=bold ctermfg=10 ctermbg=17 gui=none guifg=bg guibg=Red
highlight DiffChange cterm=bold ctermfg=10 ctermbg=17 gui=none guifg=bg guibg=Red
highlight DiffText   cterm=bold ctermfg=10 ctermbg=88 gui=none guifg=bg guibg=Red
highlight CursorLineNR ctermbg=Red
