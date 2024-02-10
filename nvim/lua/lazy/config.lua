local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
if not vim.loop.fs_stat(lazypath) then
	vim.fn.system({
		"git",
		"clone",
		"--filter=blob:none",
		"https://github.com/folke/lazy.nvim.git",
		"--branch=stable", -- latest stable release
		lazypath,
	})
end
vim.opt.rtp:prepend(lazypath)

local plugins = {
	{"nvim-treesitter/nvim-treesitter",
	build = ":TSUpdate",
	dependencies = {'rush-rs/tree-sitter-asm'}},
	{ "ellisonleao/gruvbox.nvim",
	priority = 1000,
	config = true,
	},
	{"williamboman/mason.nvim"},
	{"williamboman/mason-lspconfig.nvim"},
	{'neovim/nvim-lspconfig'},
	{'hrsh7th/cmp-nvim-lsp'},
	{'hrsh7th/cmp-buffer'},
	{'hrsh7th/cmp-path'},
	{'hrsh7th/cmp-cmdline'},
	{'hrsh7th/nvim-cmp'},
	{'L3MON4D3/LuaSnip'},
	{'nvim-telescope/telescope.nvim', tag = '0.1.5',
	dependencies = { 'nvim-lua/plenary.nvim' }},
	{'j-morano/buffer_manager.nvim',
	dependencies = { 'nvim-lua/plenary.nvim' }},
	{'romgrk/barbar.nvim',
	dependencies = {
		'lewis6991/gitsigns.nvim', -- OPTIONAL: for git status
		'nvim-tree/nvim-web-devicons', -- OPTIONAL: for file icons
	},
	init = function() vim.g.barbar_auto_setup = false end,
		opts = {
    		},
	},
	{'nvim-lualine/lualine.nvim',
    	dependencies = { 'nvim-tree/nvim-web-devicons' }}

}


require("lazy").setup(plugins, opts)
