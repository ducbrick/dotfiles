return {
	{ -- collection of various small independent plugins/modules
		"echasnovski/mini.nvim",
		config = function()
			require("mini.ai").setup({ n_lines = 500 })

			require("mini.surround").setup()

			require("mini.comment").setup()

			require("mini.operators").setup()

			require("mini.pairs").setup()
		end,
	},
}
