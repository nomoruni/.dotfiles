local lspconfig = require('lspconfig')
lspconfig.csharp_ls.setup({
	on_attach = on_attach,
	capabilities = capabilities,
})
lspconfig.jedi_language_server.setup({
	on_attach = on_attach,
	capabilities = capabilities,
})
lspconfig.lua_ls.setup({
       	on_attach = on_attach,
	capabilities = capabilities,
})
lspconfig.omnisharp.setup({
	on_attach = on_attach,
	capabilities = capabilities,
})
lspconfig.pylyzer.setup({
	on_attach = on_attach,
	capabilities = capabilities,
})
lspconfig.pylsp.setup({
	on_attach = on_attach,
	capabilities = capabilities,
})
