require("neoscroll").setup({
	mappings = { "<C-u>", "<C-d>", "<C-b>", "<C-f>", "<C-y>", "<C-e>", "zt", "zz", "zb" },
	hide_cursor = false,
	stop_eof = true,
	respect_scrolloff = false,
	cursor_scrolls_alone = true,
	duration_multiplier = 1.0,
	performance_mode = false,
	ignored_events = { "WinScrolled", "CursorMoved" },
	telescope_scroll_opts = { duration = 250 },
})
