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

# Create icons in multiple sizes
sizes = [192, 512]

for size in sizes:
    # Create a square image with transparent background
    img = Image.new("RGBA", (size, size), color=(0, 0, 0, 0))

    # Calculate envelope dimensions (70% of image size, centered)
    envelope_size = int(size * 0.7)
    padding = (size - envelope_size) // 2

    # Convert SVG to PNG at the desired size
    png_data = cairosvg.svg2png(
        url="envelope.svg",
        output_width=envelope_size,
        output_height=envelope_size
    )

    # Load the PNG data
    envelope_img = Image.open(io.BytesIO(png_data))

    # Paste the envelope onto the background (centered)
    img.paste(envelope_img, (padding, padding), envelope_img)

    # Save as PNG
    img.save(f"icon-{size}.png", format="PNG")
    print(f"✓ Generated icon-{size}.png ({size}x{size})")
