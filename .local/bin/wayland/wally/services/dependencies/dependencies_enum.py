from enum import Enum


class X11(Enum):
    WALLPAPER_RENDERER = "feh"
    MPV_PLAYER = "mpv"
    GET_YOUR_SCREEN_RESOLUTION = "xrandr"
    VIDEO_WALLPAPER_RENDERER = "xwinwrap"
    VIDEO_CONVERTER = "ffmpeg"
    MENU = "rofi"
    IMAGE_CONVERTER = "magick"


class Wayland(Enum):
    WALLPAPER_RENDERER = "swww"
    GET_YOUR_SCREEN_RESOLUTION = "wlr-randr"
    MPV_PLAYER = "mpv"
    VIDEO_WALLPAPER_RENDERER = "mpvpaper"
    VIDEO_CONVERTER = "ffmpeg"
    MENU = "rofi"
    IMAGE_CONVERTER = "magick"
