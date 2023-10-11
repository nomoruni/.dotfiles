vim.g.mapleader = " "
vim.keymap.set("n", "<F1>", "")
vim.keymap.set("n", "<leader>fe", vim.cmd.Ex)
vim.keymap.set("n", "<C-s>", vim.cmd.w)
vim.keymap.set("n", "<leader>tt", vim.cmd.tabnew)
vim.keymap.set("n", "<leader>tb", vim.cmd.tabprevious)
vim.keymap.set("n", "<leader>tn", vim.cmd.tabNext)
vim.keymap.set("n", "<leader>tc", vim.cmd.tabclose)


vim.keymap.set("n", "<leader>vs", vim.cmd.vsplit)
vim.keymap.set("n", "<leader>vh", vim.cmd.split)


vim.keymap.set("n", "<leader>ll", "<cmd> Neotree toggle <CR>")
vim.keymap.set("n","<leader>lb", "<cmd> Neotree buffers <CR>")

vim.keymap.set("n", "<leader>ct", "<cmd> tabnew | :terminal <CR>")
vim.keymap.set("n", "<leader>ch", "<cmd> split | :terminal <CR>")
