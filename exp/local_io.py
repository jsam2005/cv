"""Local file input helpers (replaces Google Colab upload)."""

import sys
from pathlib import Path

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".webp", ".tif", ".tiff"}
VIDEO_EXTENSIONS = {".mp4", ".avi", ".mov", ".mkv", ".webm"}


def get_path(prompt: str, allowed_extensions: set[str] | None = None) -> str:
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = input(prompt).strip()

    resolved = Path(path).expanduser().resolve()
    if not resolved.exists():
        raise FileNotFoundError(f"File not found: {path}")

    if allowed_extensions and resolved.suffix.lower() not in allowed_extensions:
        exts = ", ".join(sorted(allowed_extensions))
        raise ValueError(f"Expected one of [{exts}], got '{resolved.suffix}'")

    return str(resolved)


def get_image_path() -> str:
    return get_path("Enter image path: ", IMAGE_EXTENSIONS)


def get_video_path() -> str:
    return get_path("Enter video path: ", VIDEO_EXTENSIONS)
