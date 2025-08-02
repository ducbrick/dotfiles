return {
	{
		'xeluxee/competitest.nvim',
		dependencies = 'MunifTanjim/nui.nvim',
		config = function()
			require('competitest').setup({
				maximum_time = 1500,

				received_contests_directory = "$(HOME)/Code/Personal/CP/$(JUDGE)",
				received_contests_problems_path = "$(HOME)/Code/Personal/CP/$(JUDGE)/$(PROBLEM)/main.$(FEXT)",
				received_problems_path = "$(HOME)/Code/Personal/CP/$(JUDGE)/$(PROBLEM)/main.$(FEXT)",

				evaluate_template_modifiers = true,
				template_file = "~/.config/nvim/lua/plugins/cp-template.$(FEXT)",

				-- compile_command = {
				-- 	cpp = { 
				-- 		exec = 'g++',
				-- 		args = {'$(FNAME)', '-o', '$(FNOEXT).exe'} },
				-- },
			})
		end,
	}
}
