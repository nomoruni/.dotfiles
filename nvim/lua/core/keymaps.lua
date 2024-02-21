vim.g.mapleader = ' '
vim.g.maplocalleader = ' '

-- Open file manager --
vim.keymap.set("n", "<leader>fm", vim.cmd.Ex)

-- Jump to definitions
vim.keymap.set("n", "<leader>jd", "<C-]>")

-- Buffers --
vim.keymap.set("n", "<A-l>", vim.cmd.bnext)
vim.keymap.set("n", "<A-h>", vim.cmd.bprevious)
vim.keymap.set("n", "<A-b>", vim.cmd.bdelete)

-- Save/Write the file --
vim.keymap.set("n", "<C-s>", vim.cmd.w)

-- Open the terminal in a new buffer --
vim.keymap.set("n", "<A-t>", vim.cmd.terminal)

-- Move to the start and the end of lines -- 
vim.keymap.set("n", "<leader>l", "$")
vim.keymap.set("n", "<leader>h", "0")
vim.keymap.set("i", "<C-l>", "<C-o>$")
vim.keymap.set("i", "<C-h>", "<C-o>0")

-- Move in insert mode --
vim.keymap.set("i", "<A-j>", "<C-o>j");
vim.keymap.set("i", "<A-k>", "<C-o>k");
vim.keymap.set("i", "<A-h>", "<C-o>h");
vim.keymap.set("i", "<A-l>", "<C-o>l");

-- Move selected lines -- 
vim.keymap.set("v", "K", ":m '<-2<CR>gv=gv")
vim.keymap.set("v", "J", ":m '>+1<CR>gv=gv")

-- Split --
vim.keymap.set("n", "<leader>sv", ":vsplit | Explore<CR>")
vim.keymap.set("n", "<leader>sh", ":hsplit | Explore<CR>")
vim.keymap.set("n", "<leader>ss", "<C-w>w")
vim.keymap.set("n", "<leader>sc", ":q<CR>")
