--plugins
local Plug = vim.fn['plug#']

vim.call('plug#begin')


--colors plugin
Plug('bluz71/vim-nightfly-colors', {as = 'nightfly'})
Plug('bluz71/vim-moonfly-colors', {as = 'moonfly'})
--powerline plugin
Plug 'itchyny/lightline.vim'
--treesitter plugin
Plug('nvim-treesitter/nvim-treesitter', {run = ':TSUpdate'})
--rainbow parenthesis plugin
Plug 'hiphish/rainbow-delimiters.nvim'
--lsp plugins
Plug 'williamboman/mason.nvim'
Plug 'williamboman/mason-lspconfig.nvim'
Plug 'neovim/nvim-lspconfig'
--autocomplete
Plug 'hrsh7th/nvim-cmp'
Plug 'hrsh7th/cmp-nvim-lsp'
Plug 'L3MON4D3/LuaSnip'
--autopairs
Plug 'windwp/nvim-autopairs'

vim.call('plug#end')

--REQUIRE OTHER DOCUMENTS THINGS
--enable treesitter highlighting
require('treesitter')
--enable rainbow parnthesis
require('rainbow')
--lsp require
require('lsp_config')
--completion require
require('completions')
--autopairs require
require('autopairs')

--set nightfly colorscheme
vim.opt.termguicolors = true
vim.cmd [[colorscheme moonfly]]

--search highlightation and cliboard to computor cliborg
vim.opt.hlsearch = true
vim.opt.incsearch = true
vim.opt.cursorline = true
vim.opt.clipboard = "unnamedplus"

--set numbers
vim.opt.relativenumber = true
vim.opt.number = true

--syntax on
vim.opt.syntax = 'on'

--enable mouse
vim.opt.mouse = 'a'

--tab things
vim.opt.tabstop = 4
vim.opt.softtabstop = 4
vim.opt.shiftwidth = 4
vim.opt.expandtab = true
vim.opt.autoindent = true

--idk really what this does, prolly not much
vim.opt.fileformat = 'unix'

--status bar
vim.opt.laststatus = 2
vim.opt.showmode = false
vim.g.lightline = { colorscheme = 'moonfly' }

--cursor stay thick
vim.opt["guicursor"] = ""

--start scrolling before bottom line
vim.opt.scrolloff = 10
