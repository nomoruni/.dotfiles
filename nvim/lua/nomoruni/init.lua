--print("Hello from Nomoruni")
require("nomoruni/remap")

vim.wo.number = true
vim.opt.termguicolors = true

--LAZY.NVIM--

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
	"ellisonleao/gruvbox.nvim", priority = 1000,

	{
		'nvim-telescope/telescope.nvim', tag = '0.1.2',
		-- or                              , branch = '0.1.x',
		dependencies = { 'nvim-lua/plenary.nvim' }
	},

	{"nvim-treesitter/nvim-treesitter", build = ":TSUpdate"},

	{'ThePrimeagen/harpoon'},

	{'dinhhuy258/git.nvim'},

	{'williamboman/mason.nvim'},          
	{'williamboman/mason-lspconfig.nvim'}, 
	{'neovim/nvim-lspconfig'},            

	{'hrsh7th/nvim-cmp'},    
	{'hrsh7th/cmp-nvim-lsp'},
	{'hrsh7th/cmp-buffer'},
	{'hrsh7th/cmp-path'},
	{'hrsh7th/cmp-cmdline'},
	{'L3MON4D3/LuaSnip'},    
	{'saadparwaiz1/cmp_luasnip'},
	{'norcalli/nvim-colorizer.lua'},
        {"utilyre/barbecue.nvim",
        	name = "barbecue",
        	version = "*",
        	dependencies = {
        		"smiteshp/nvim-navic",
        		"nvim-tree/nvim-web-devicons", -- optional dependency
        	},
        	opts = {
        		-- configurations go here
        	},
        },
        {"nvim-neo-tree/neo-tree.nvim",
        	branch = "v3.x",
        	dependencies = {
        		"nvim-lua/plenary.nvim",
        		"nvim-tree/nvim-web-devicons", -- not strictly required, but recommended
        		"MunifTanjim/nui.nvim",
        	}
        },
	--Multiple Cursors
        {"smoka7/multicursors.nvim",
            event = "VeryLazy",
            dependencies = {
                'smoka7/hydra.nvim',
            },
            opts = {},
            cmd = { 'MCstart', 'MCvisual', 'MCclear', 'MCpattern', 'MCvisualPattern', 'MCunderCursor' },
            keys = {
                    {
                        mode = { 'v', 'n' },
                        '<Leader>m',
                        '<cmd>MCstart<cr>',
                        desc = 'Create a selection for selected text or word under the cursor',
                    },
                },
        },


	{
		"neanias/everforest-nvim",
		version = false,
		lazy = false,
		priority = 1000,
		},
		{'feline-nvim/feline.nvim'},
		{'nvim-orgmode/orgmode',
			dependencies = {
				{ 'nvim-treesitter/nvim-treesitter', lazy = true },
			},
			event = 'VeryLazy',
		},

	{'mfussenegger/nvim-dap',
		"jay-babu/mason-nvim-dap.nvim",
	},
}



require("lazy").setup(plugins, opts)



