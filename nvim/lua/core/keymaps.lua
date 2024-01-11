vim.g.mapleader = ' '
vim.g.maplocalleader = ' '

vim.keymap.set("n", "<leader>fm", vim.cmd.Ex)
vim.keymap.set("n", "<A-l>", vim.cmd.bnext)
vim.keymap.set("n", "<A-h>", vim.cmd.bprevious)
vim.keymap.set("n", "<A-b>", vim.cmd.bdelete)

vim.keymap.set("n", "<A-t>", vim.cmd.terminal)
