return {
	{ -- collection of various small independent plugins/modules
		"nvim-mini/mini.nvim",
		dependencies = { "nvim-treesitter/nvim-treesitter-textobjects" },
		config = function()

			local spec = require("mini.ai").gen_spec
			require("mini.ai").setup({
				n_lines = 500,
				custom_textobjects = {
					F = spec.treesitter({ i = "@function.inner", a = "@function.outer" }),
					i = spec.treesitter({ i = "@conditional.inner", a = "@conditional.outer" }),
					l = spec.treesitter({ i = "@loop.inner", a = "@loop.outer" }),
					c = spec.treesitter({ i = "@class.inner", a = "@class.outer" }),
				}
			})

			require("mini.surround").setup()

			require("mini.comment").setup()

			require("mini.operators").setup()

			require("mini.pairs").setup()

			require("mini.splitjoin").setup()

		end,
	},
}
