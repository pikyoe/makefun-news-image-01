"""Entry for make.fun competition news-image-01.

Copies the bundled front-page image (entry.png) to the output
directory as entry.png. The image sums up the world news of
Friday 13 November 2026 in one editorial collage: Europe joins
the Ukraine peace talks, the Nvidia chief executive resigns as
shares plunge, a strike on a Gaza hospital kills six, and
Microsoft 365 goes down worldwide.

Standard library only. No network access is needed or used.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"

# PNG signature: the first eight bytes of every PNG file.
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def main() -> None:
    if not SOURCE.is_file():
        raise FileNotFoundError(f"bundled image missing: {SOURCE}")
    with SOURCE.open("rb") as handle:
        if handle.read(len(PNG_MAGIC)) != PNG_MAGIC:
            raise ValueError(f"bundled image is not a PNG: {SOURCE}")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, output_dir / "entry.png")


if __name__ == "__main__":
    main()
