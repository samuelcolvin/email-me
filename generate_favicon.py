#!/usr/bin/env python3
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "pillow",
# ]
# ///
from PIL import Image, ImageDraw, ImageFont

# Create a 48x48 image with a white background
size = 48
img = Image.new("RGBA", (size, size), color=(255, 255, 255, 0))
draw = ImageDraw.Draw(img)

# Try to use a system font that supports emoji
emoji = "✉️"
font_size = 48

# Try different fonts that might support emoji on macOS
font_paths = [
    "/System/Library/Fonts/Apple Color Emoji.ttc",
    "/System/Library/Fonts/Supplemental/Apple Color Emoji.ttc",
]

font = None
for font_path in font_paths:
    try:
        font = ImageFont.truetype(font_path, font_size)
        break
    except:
        continue

if font is None:
    # Fallback to default font
    font = ImageFont.load_default()

# Get text bounding box to center it
bbox = draw.textbbox((0, 0), emoji, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]

# Center the emoji
x = (size - text_width) // 2 - bbox[0]
y = (size - text_height) // 2 - bbox[1]

# Draw the emoji
draw.text((x, y), emoji, font=font, fill=(0, 0, 0, 255), embedded_color=True)

# Save as favicon.ico
img.save("site/favicon.ico", format="ICO", sizes=[(48, 48)])
print("✓ Generated favicon.ico (48x48)")
