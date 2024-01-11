require("core.keymaps")
require("lazy.config")

vim.opt.relativenumber = true

vim.opt.smartindent = true

vim.opt.incsearch = true 

vim.opt.termguicolors = true

vim.opt.scrolloff = 8
vim.opt.signcolumn = "yes"
vim.opt.isfname:append("@-@")

vim.opt.updatetime = 50

vim.cmd.tnoremap  '<Esc> <C-\\><C-n>'


vim.o.background = "dark" -- or "light" for light mode
vim.cmd([[colorscheme gruvbox]])
