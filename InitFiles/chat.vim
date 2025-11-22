"========================
" Vim Configuration (Cleaned)
"========================

"------------------------
" Filetype & Syntax
"------------------------
filetype plugin indent on       "Enable filetype-specific plugins and indentation
syntax on                       "Enable syntax highlighting
set spelllang=en_us             "Spell check in English
set spell                       "Enable spell checking

"------------------------
" Encoding & Display
"------------------------
set encoding=utf-8              "Use UTF-8 encoding
set background=dark             "Dark background
set number                      "Show absolute line numbers
set relativenumber              "Show relative line numbers
set cursorline                  "Highlight current line
set cursorcolumn                "Highlight current column
set colorcolumn=80              "Column guide at 80 characters
set wrap                        "Enable line wrapping"
set linebreak                   "Wrap lines at word boundaries

"------------------------
" Tabs & Indentation
"------------------------
set expandtab                   "Use spaces instead of tabs
set tabstop=4                   "Tab character width
set softtabstop=4               "Insert/delete spaces as if tab=4
set shiftwidth=4                "Indentation width
set autoindent                  "Copy indentation from previous line
set smartindent                 "Enable C-style smart indentation

"------------------------
" Search & Highlight
"------------------------
set hlsearch                    "Highlight search results
set incsearch                   "Incremental search
set ignorecase                  "Case-insensitive search
set smartcase                   "Case-sensitive if uppercase letters used

"------------------------
" Undo, Backup, & Files
"------------------------
set nobackup                    "No backup files
set noswapfile                  "No swap files
set history=1000                "Store 1000 command-line entries
set ff=unix                     "Use Unix line endings

"------------------------
" UI & Status
"------------------------
set title                       "Show current file in window title
set showmode                    "Show current mode
set ruler                       "Show cursor position
set showcmd                     "Show partial commands
set laststatus=3                "Global status line
set belloff=all                 "Disable error bell
set visualbell                  "Use visual bell instead

"------------------------
" Clipboard
"------------------------
set clipboard=unnamedplus       "Use system clipboard

"------------------------
" Folding
"------------------------
set foldenable                  "Enable folding
set foldmethod=manual           "Manual folding (adjust as needed)

"------------------------
" Window & Tab Navigation
"------------------------
nnoremap <leader>h <C-w>h
nnoremap <leader>j <C-w>j
nnoremap <leader>k <C-w>k
nnoremap <leader>l <C-w>l
nnoremap <C-j> :bprev<CR>
nnoremap <C-k> :bnext<CR>

"------------------------
" Search Highlight Clearing
"------------------------
nnoremap <CR> :nohlsearch<CR>
nnoremap <Esc> :nohlsearch<CR>

"------------------------
" Terminal
"------------------------
nnoremap <leader>\t :terminal ++rows=6<CR>

"------------------------
" Line Navigation Shortcuts
"------------------------
nnoremap B ^
nnoremap E $
nnoremap <leader>B g^
nnoremap <leader>E g$
nnoremap <leader>d d^

"------------------------
" LaTeX Shortcuts
"------------------------
nnoremap <leader>\c :!pdflatex %<CR>
nnoremap <leader>\wc :w<CR>:!pdflatex %<CR>

"------------------------
" Miscellaneous
"------------------------
" Disable automatic commenting on new lines
autocmd FileType * setlocal formatoptions-=c formatoptions-=r formatoptions-=o

" Allow movement over visual lines
noremap j gj
noremap k gk

" Highlight last inserted text
nnoremap gV '[V']

" Load and save view automatically
autocmd BufWinLeave * mkview

" Highlight trailing spaces
match ErrorMsg '\s+$'

" Remove DOS line endings
nnoremap <leader>\rl :e ++ff=dos<CR>

" Optional: Uncomment to enable mouse support
" set mouse=a

" Optional: Uncomment to show trailing whitespace
" set list
