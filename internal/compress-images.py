"""
Compress images in img/routes/ for web use.
- Resizes images wider than 1200px (keeps aspect ratio)
- Converts PNG to JPEG at 85% quality
- Saves compressed files alongside originals as .jpg
- Prints before/after file sizes

Run: python compress-images.py
Requires Pillow: pip install Pillow
"""

from PIL import Image
import os

SRC_DIR = os.path.join(os.path.dirname(__file__), "img", "routes")
MAX_WIDTH = 1200
JPEG_QUALITY = 85

def format_kb(size_bytes):
    return f"{size_bytes / 1024:.0f} KB"

total_before = 0
total_after = 0

for filename in sorted(os.listdir(SRC_DIR)):
    if not filename.lower().endswith(".png"):
        continue

    src_path = os.path.join(SRC_DIR, filename)
    out_name = os.path.splitext(filename)[0] + ".jpg"
    out_path = os.path.join(SRC_DIR, out_name)

    size_before = os.path.getsize(src_path)
    total_before += size_before

    with Image.open(src_path) as img:
        # Convert RGBA/palette to RGB for JPEG
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")

        # Resize if wider than MAX_WIDTH
        if img.width > MAX_WIDTH:
            ratio = MAX_WIDTH / img.width
            new_size = (MAX_WIDTH, int(img.height * ratio))
            img = img.resize(new_size, Image.LANCZOS)

        img.save(out_path, "JPEG", quality=JPEG_QUALITY, optimize=True)

    size_after = os.path.getsize(out_path)
    total_after += size_after

    saving = (1 - size_after / size_before) * 100
    print(f"{filename}")
    print(f"  {format_kb(size_before)}  →  {format_kb(size_after)}  ({saving:.0f}% smaller)\n")

print("─" * 40)
print(f"Total: {format_kb(total_before)}  →  {format_kb(total_after)}  ({(1 - total_after/total_before)*100:.0f}% smaller)")
print("\nDone. Compressed files saved as .jpg alongside originals.")
print("Update HTML image references from .png to .jpg when ready.")
