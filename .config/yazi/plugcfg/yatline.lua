function yatline()
	require("yatline"):setup({
		-- theme = themes,
		section_separator = { open = "", close = "" },
		part_separator = { open = "", close = "" },
		inverse_separator = { open = "", close = "" },

		style_a = {
			fg = "black",
			bg_mode = {
				normal = "blue",
				select = "brightyellow",
				un_set = "brightred",
			},
		},
		style_b = { bg = "brightblack", fg = "brightwhite" },
		style_c = { bg = "black", fg = "brightwhite" },

		permissions_t_fg = "green",
		permissions_r_fg = "yellow",
		permissions_w_fg = "red",
		permissions_x_fg = "cyan",
		permissions_s_fg = "white",

		tab_width = 20,
		tab_use_inverse = false,

		selected = { icon = "󰻭", fg = "yellow" },
		copied = { icon = "", fg = "green" },
		cut = { icon = "", fg = "red" },

		total = { icon = "󰮍", fg = "yellow" },
		succ = { icon = "", fg = "green" },
		fail = { icon = "", fg = "red" },
		found = { icon = "󰮕", fg = "blue" },
		processed = { icon = "󰐍", fg = "green" },

		show_background = false,

		display_header_line = true,
		display_status_line = true,

		component_positions = { "header", "tab", "status" },

		header_line = {
			left = {
				section_a = {
					{ type = "coloreds", custom = true, name = { { " ~~> ", "black" } } },
					{ type = "string", custom = false, name = "hovered_path" },
				},
				section_b = {},
				section_c = {},
			},
			right = {
				section_a = {},
				section_b = {
					{ type = "line", custom = false, name = "tabs", params = { "left" } },
				},
				section_c = {
					{ type = "coloreds", custom = true, name = { { "  󰇥  ", "while" } } },
				},
			},
		},

		status_line = {
			left = {
				section_a = {
					{ type = "string", custom = false, name = "tab_mode" },
				},
				section_b = {
					{ type = "string", custom = false, name = "hovered_size" },
				},
				section_c = {
					-- { type = "string", custom = false, name = "hovered_path" },
					{ type = "coloreds", custom = false, name = "count" },
				},
			},
			right = {
				section_a = {
					{ type = "string", custom = false, name = "cursor_position" },
				},
				section_b = {
					{ type = "string", custom = false, name = "cursor_percentage" },
				},
				section_c = {
					{ type = "string", custom = false, name = "hovered_file_extension", params = { true } },
					{ type = "coloreds", custom = false, name = "permissions" },
				},
			},
		},
	})
end

return yatline()
