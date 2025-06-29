from core.paths.path_list import WALLY_THUMBNAIL
from services import shell
from pathlib import Path
from utils import log_exceptions
from time import localtime


class ThumbnailConverter:
    @log_exceptions
    def image_convert(
        self,
        input: Path,
        output: Path,
    ) -> None:
        shell(
            f"magick {input} -resize 600x600^ -gravity center -crop 500x500+0+0 +repage {output}"
        )

    @log_exceptions
    def video_convert(
        self,
        input: Path,
        output: Path,
    ) -> None:
        now = localtime()
        time = f"{now.tm_mday:02d}.{now.tm_mon:02d}.{now.tm_year}_{now.tm_hour:02d}-{now.tm_min:02d}-{now.tm_sec:02d}"

        thumbnail_name = f"video_thumbnail_{input.stem}_{time}.jpg"
        current_thumbnail = WALLY_THUMBNAIL / thumbnail_name

        shell(f"ffmpeg -i {input} -vframes 1 {current_thumbnail}")
        self.image_convert(current_thumbnail, output)
        current_thumbnail.unlink(missing_ok=True)


thumbnail_video_convert = ThumbnailConverter().video_convert
thumbnail_image_convert = ThumbnailConverter().image_convert
