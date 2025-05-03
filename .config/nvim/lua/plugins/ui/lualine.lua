require("lualine").setup({
	options = {
		icons_enabled = true, -- Включить иконки
		theme = "auto", -- Тема
		component_separators = { left = "", right = "" },
		section_separators = { left = "", right = "" },
		disabled_filetypes = {
			winbar = {
				"dashboard",
			},
			"snacks_dashboard",
			statusline = {
				"dashboard",
			},
			"snacks_dashboard",
		},
		ignore_focus = {
			"neo-tree",
			"dashboard",
			"snacks_dashboard",
		}, -- Игнорируем фокус в neo-tree
		always_divide_middle = true,
		always_show_tabline = true,
		globalstatus = true, -- Включаем общую статус-линию
		refresh = {
			statusline = 100,
			tabline = 100,
			winbar = 100,
		},
	},
	sections = {
		lualine_a = {
			function()
				if vim.fn.exists("b:VM_Selection") == 1 and not vim.tbl_isempty(vim.b.VM_Selection) then
					local status = vim.fn["VMInfos"]().status:lower() -- Преобразуем статус в нижний регистр
					local replacements = {
						["active"] = "󱢓 MCursor:",
					}
					return replacements[status] or status -- Заменяем, если статус найден в таблице
				else
					return ""
				end
			end,
			function()
				local mode_map = {
					n = " NORMAL",
					i = " INSERT",
					v = "󰈈 VISUAL",
					V = "󰈈 V-Line",
					[""] = "󰈈 V-Block",
					c = " COMMAND",
					t = " TERMINAL",
					r = "󰑕 REPLACE",
					R = "󰑕 REPLACE",
				}
				return mode_map[vim.fn.mode()] or "Unknown"
			end,
		},
		lualine_b = {
			{ "branch", icon = "" },
			{ "diff", icon = "" },
			{ "diagnostics", icon = "󰅚 " },
			{
				function()
					return vim.fn["db_ui#statusline"]({
						prefix = "DB: ",
						separator = " -> ",
						show = { "db_name", "schema", "table" },
					})
				end,
			},
		},
		lualine_c = {
			{
				function()
					local filename = vim.fn.expand("%:t")
					if filename == "" then
						return "[No Name]"
					end
					local max_length = 20
					if #filename > max_length then
						return filename:sub(1, max_length - 2) .. "..."
					end
					return filename
				end,
			},
		},
		lualine_x = {
			{
				function()
					local status = require("codeium.virtual_text").status()

					if status.state == "idle" then
						return "󰘦 "
					elseif status.state == "waiting" then
						return "󰘦  Waiting..."
					elseif status.state == "completions" and status.total > 0 then
						return string.format("󰘦  %d/%d", status.current, status.total)
					else
						return "󰘦  0"
					end
				end,
			},
			-- {
			-- 	"copilot",
			-- 	-- Default values
			-- 	symbols = {
			-- 		status = {
			-- 			icons = {
			-- 				enabled = " ",
			-- 				sleep = " ", -- auto-trigger disabled
			-- 				disabled = " ",
			-- 				warning = " ",
			-- 				unknown = " ",
			-- 			},
			-- 			hl = {
			-- 				enabled = "#50FA7B",
			-- 				sleep = "#AEB7D0",
			-- 				disabled = "#6272A4",
			-- 				warning = "#FFB86C",
			-- 				unknown = "#FF5555",
			-- 			},
			-- 		},
			-- 		spinners = "dots", -- has some premade spinners
			-- 		spinner_color = "#6272A4",
			-- 	},
			-- 	show_colors = false,
			-- 	show_loading = true,
			-- },
			{
				function()
					local command = require("noice").api.status.command.get()
					if command and command ~= "" then
						return command
					else
						return "🚀"
					end
				end,
			},
		},

		lualine_y = {
			"filetype",
		},
		lualine_z = {

			"progress",
			"location",
		},
	},
	inactive_sections = {
		lualine_a = {},
		lualine_b = {},
		lualine_c = { "filename" },
		lualine_x = { "location" },
		lualine_y = {},
		lualine_z = {},
	},
	tabline = {},
	winbar = {},
	inactive_winbar = {},
	extensions = {},
})
