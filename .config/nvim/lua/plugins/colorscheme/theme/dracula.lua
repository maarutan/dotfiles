require("dracula").setup({
	style = "default", -- The theme comes in three styles, `default`, a darker variant `soft` and `day`
	light_style = "day", -- The theme is used when the background is set to light
	transparent = false, -- Enable this to disable setting the background color
	terminal_colors = true, -- Configure the colors used when opening a `:terminal` in Neovim
	styles = {
		-- Style to be applied to different syntax groups
		-- Value is any valid attr-list value for `:help nvim_set_hl`
		comments = { italic = true },
		keywords = { italic = true },
		functions = {},
		variables = {},
		-- Background styles. Can be "dark", "transparent" or "normal"
		sidebars = "dark", -- style for sidebars, see below
		floats = "dark", -- style for floating windows
	},
	sidebars = { "qf", "help" }, -- Set a darker background on sidebar-like windows. For example: `["qf", "vista_kind", "terminal", "packer"]`
	day_brightness = 0.3, -- Adjusts the brightness of the colors of the **Day** style. Number between 0 and 1, from dull to vibrant colors
	hide_inactive_statusline = false, -- Enabling this option, will hide inactive statuslines and replace them with a thin border instead. Should work with the standard **StatusLine** and **LuaLine**.
	dim_inactive = false, -- dims inactive windows
	lualine_bold = false, -- When `true`, section headers in the lualine theme will be bold

	--- You can override specific color groups to use other groups or a hex color
	--- function will be called with a ColorScheme table
	on_colors = function() end,

	--- You can override specific highlights to use other groups or a hex color
	--- function will be called with a Highlights and ColorScheme table
	on_highlights = function() end,
	use_background = true, -- can be light/dark/auto. When auto, background will be set to vim.o.background

	cache = true, -- When set to true, the theme will be cached for better performance

	prefer_undercurl = true, -- When set to true, the undercurl will be used place of underline in specific contexts.

	plugins = {
		-- enable all plugins when not using lazy.nvim
		-- set to false to manually enable/disable plugins
		all = package.loaded.lazy == nil,
		-- uses your plugin manager to automatically enable needed plugins
		-- currently only lazy.nvim is supported
		auto = true,
		-- add any plugins here that you want to enable
		-- for all possible plugins, see:
		--   * https://github.com/folke/tokyonight.nvim/tree/main/lua/tokyonight/groups
		-- telescope = true,
	},
})
