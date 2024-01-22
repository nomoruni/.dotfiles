vim.g.mapleader = ' '
vim.g.maplocalleader = ' '

vim.keymap.set("n", "<leader>fm", vim.cmd.Ex)
vim.keymap.set("n", "<A-l>", vim.cmd.bnext)
vim.keymap.set("n", "<A-h>", vim.cmd.bprevious)
vim.keymap.set("n", "<A-b>", vim.cmd.bdelete)

vim.keymap.set("n", "<A-t>", vim.cmd.terminal)

vim.keymap.set("n", "<leader>l", "$")
vim.keymap.set("n", "<leader>h", "0")
vim.keymap.set("i", "<C-l>", "<C-o>$")
vim.keymap.set("i", "<C-h>", "<C-o>0")

vim.keymap.set("v", "J", ":m '>+1<CR>gv=gv")
vim.keymap.set("v", "K", ":m '<-2<CR>gv=gv")
