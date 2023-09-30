lua require('init')

"plugins
call plug#begin()

Plug 'bluz71/vim-moonfly-colors', { 'as': 'moonfly' }
Plug 'bluz71/vim-nightfly-colors', { 'as': 'nightfly' }
Plug 'itchyny/lightline.vim'

call plug#end()

"set nightfly colorscheme
set termguicolors
colorscheme nightfly

"search highlightation and cliboard to computor clipboard
set hlsearch
set incsearch
set cursorline
set clipboard=unnamedplus

set number relativenumber

"syntax and mouse
syntax on
"set showmatch
set mouse=a

"tab things
set tabstop=4
set softtabstop=4
set shiftwidth=4
set expandtab
set autoindent
set fileformat=unix

"show syntax optionsthing i think
set wildmode=longest,list,full

"status bar
set laststatus=2
set noshowmode
let g:lightline = { 'colorscheme': 'nightfly' }

let g:nightflyCursorColor = v:true

