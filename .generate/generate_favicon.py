#!/usr/bin/env python3
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "pillow",
#     "cairosvg",
# ]
# ///
from PIL import Image
import cairosvg
import io

# Create a 48x48 favicon with transparent background
size = 48

# Convert SVG to PNG at full size (no padding)
png_data = cairosvg.svg2png(
    url=".generate/envelope.svg",
    output_width=size,
    output_height=size
)

# Load the PNG data
img = Image.open(io.BytesIO(png_data))

# Save as favicon.ico
img.save("favicon.ico", format="ICO", sizes=[(48, 48)])
print("✓ Generated favicon.ico (48x48)")
