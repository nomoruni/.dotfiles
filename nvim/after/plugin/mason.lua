require('mason').setup({
	PATH = "append",
})
require('mason-lspconfig').setup{
--	ensure_installed = {"lua_ls","omnisharp","csharp_ls","jedi_language_server","lua_ls","pylyzer","omnisharp_mono","pylsp"}
}
require("mason-nvim-dap").setup({
    handlers = {
        function(config)
          -- all sources with no handler get passed here

          -- Keep original functionality
          require('mason-nvim-dap').default_setup(config)
        end,
        python = function(config)
            config.adapters = {
	            type = "executable",
	            command = "/usr/bin/python3",
	            args = {
		            "-m",
		            "debugpy.adapter",
	            },
            }
            require('mason-nvim-dap').default_setup(config) -- don't forget this!
        end,

    },
})

