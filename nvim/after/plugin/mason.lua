require('mason').setup({})
require('mason-lspconfig').setup{
	ensure_installed = {"lua_ls","omnisharp","csharp_ls","jedi_language_server","lua_ls","pylyzer","omnisharp_mono","pylsp"}
}


