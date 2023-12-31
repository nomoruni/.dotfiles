require'nvim-treesitter.configs'.setup {
  -- A list of parser names, or "all" (the five listed parsers should always be installed)
  ensure_installed = {"css", "html", "javascript", "cpp", "rust", "python", "c", "lua", "vim", "vimdoc", "query", "org" , "c_sharp", "xml", "json"},

  -- Install parsers synchronously (only applied to `ensure_installed`)
  sync_install = true,

  -- Automatically install missing parsers when entering buffer
  -- Recommendation: set to false if you don't have `tree-sitter` CLI installed locally
  auto_install = true,

  highlight = {
    enable = true,
    additional_vim_regex_highlighting = ('org'),
  },
}
