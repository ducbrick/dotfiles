---@type LazySpec
return {
  "mikavilpas/yazi.nvim",
  version = "*", -- use the latest stable version
  event = "VeryLazy",
  dependencies = {
    { "nvim-lua/plenary.nvim", lazy = true },
  },
  keys = {
    -- 👇 in this section, choose your own keymappings!
    {
      "<leader>p",
      mode = { "n", "v" },
      "<cmd>Yazi<cr>",
      desc = "[P]roject tree at current file",
    },
    {
      -- Open in the current working directory
      "<leader>P",
      "<cmd>Yazi cwd<cr>",
      desc = "[P]roject tree at current working directory",
    },
  },
  ---@type YaziConfig | {}
  opts = {
    keymaps = {
      show_help = "<f1>",
    },
		-- the type of border to use for the floating window. Can be many values,
    -- including 'none', 'rounded', 'single', 'double', 'shadow', etc. For
    -- more information, see :h nvim_open_win
    yazi_floating_window_border = "single",
  },
}
