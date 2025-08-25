return {
	'nvim-telescope/telescope.nvim',
	dependencies = {
		'nvim-lua/plenary.nvim',
		{ 'nvim-telescope/telescope-fzf-native.nvim', build = 'make' }
	},
	config = function ()

		require('telescope').setup{
			defaults = {
				mappings = {
					i = {
						["<C-h>"] = "which_key"
					}
				}
			},
			pickers = {
				-- picker_name = {
				-- }
			},
			extensions = {
				-- extension_name = {
				-- }
			}
		}

		local builtin = require('telescope.builtin')

		vim.keymap.set('n', '<leader>gf', builtin.find_files, { desc = '[G]o to [F]ile' })
		vim.keymap.set('n', '<leader>gb', builtin.buffers, { desc = '[G]o to [B]uffer' })
		vim.keymap.set('n', '<leader>gr', builtin.lsp_references, { desc = '[G]o to [R]eference' })
		vim.keymap.set('n', '<leader>gs', builtin.lsp_document_symbols, { desc = '[G]o to buffer [S]ymbol' })
		vim.keymap.set('n', '<leader>gS', builtin.lsp_workspace_symbols, { desc = '[G]o to workspace [S]ymbol' })
		vim.keymap.set('n', '<leader>gi', builtin.lsp_implementations, { desc = '[G]o to [I]mplementation' })
		vim.keymap.set('n', '<leader>gd', builtin.lsp_definitions, { desc = '[G]o to [D]efinition' })
		vim.keymap.set('n', '<leader>gt', builtin.lsp_type_definitions, { desc = '[G]o to [T]ype definition' })

	end
}
