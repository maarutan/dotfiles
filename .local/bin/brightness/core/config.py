from modules import JsonManager, FileManager
from core.path.list import JSONC_CONFIG


class Config:
    def __init__(self):
        self.jm = JsonManager(JSONC_CONFIG)
        self.fm = FileManager
        self.indent = 2

        self.generate()

    def generate(self) -> None:
        try:
            r = self.fm(JSONC_CONFIG).read()
            if not r:
                self.fm(JSONC_CONFIG).write(
                    """// ┬  ┬┌─┐┬  ┬ ┬┌┬┐┌─┐  ┌─┐┌─┐┌┐┌┌─┐┬┌─┐
// └┐┌┘│ ││  │ ││││├┤   │  │ ││││├┤ ││ ┬
//  └┘ └─┘┴─┘└─┘┴ ┴└─┘  └─┘└─┘┘└┘└  ┴└─┘
//--------------------------------------------------------------------
// Copyright (c) 2025 maarutan \ Marat Arzymatov. All Rights Reserved.
// https://github.com/maarutan/volume
//
{
  // ┬─┐┌─┐┌┐┌┌┬┐┌─┐┬─┐
  // ├┬┘├┤ │││ ││├┤ ├┬┘
  // ┴└─└─┘┘└┘─┴┘└─┘┴└─

  // Theme settings
  "theme": "twist",  // Add custom themes (default options: "default" | "twist")
  
  // Volume display settings
  "redner_brightness": "  *･ﾟ✧ {volume}% ✧･ﾟ*",  // Customize volume output (use {volume} placeholder)
  
  // ┌┐┌┌─┐┌┬┐┬┌─┐┬ ┬  ┌─┐┌─┐┌┐┌┌┬┐
  // ││││ │ │ │├┤ └┬┘  └─┐├┤ │││ ││
  // ┘└┘└─┘ ┴ ┴└   ┴   └─┘└─┘┘└┘─┴┘
  
  // Notification settings
  "notify_id": 9999,          // Unique notification ID (prevents stacking)
  "notify_timeout": 1000,     // Notification display duration (milliseconds)
  "notify_icon": true,        // Show theme icons in notifications
  "notify_progress_bar": true, // Display volume progress bar
  
  // ┌─┐┌─┐┌┐┌┌┬┐┬─┐┌─┐┬
  // │  │ ││││ │ ├┬┘│ ││
  // └─┘└─┘┘└┘ ┴ ┴└─└─┘┴─┘

  // Volume control parameters
  "turn_add": 5,              // Volume increase step (--up command)
  "turn_sub": 5,              // Volume decrease step (--down command)
  "turn_smooth": true,        // Enable smooth volume transitions
  "turn_delay": 0.001          // Smooth transition speed (seconds per step)
}"""
                )
        except Exception as e:
            print(f"Config.generate: {e}")

    def get_option(self, option) -> str:
        try:
            return self.jm.get_data()[option]
        except Exception as e:
            print(f"Config.get_option: {e}")
            return ""
