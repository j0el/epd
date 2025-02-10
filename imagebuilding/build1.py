from PIL import Image, ImageDraw, ImageFont

# Create a new 800x600 image with a white background
image = Image.new('RGB', (800, 600), 'white')
draw = ImageDraw.Draw(image)

# Define the colors
black = (0, 0, 0)
red = (255, 0, 0)

# Define the fonts (you can specify the path to a TTF font file if needed)
font_small = ImageFont.load_default()
font_large = ImageFont.load_default().font_variant(size=24)

# Draw some text
draw.text((50, 50), "Hello, World!", fill=black, font=font_small)
draw.text((50, 100), "This is a larger text.", fill=red, font=font_large)

# Draw a rectangle
draw.rectangle([200, 200, 300, 300], outline=black, fill=red)

# Draw a line
draw.line([400, 400, 600, 500], fill=black, width=5)

# Draw small graphic icons (e.g., circles, triangles, etc.)
# Icon 1: Circle
draw.ellipse([500, 50, 550, 100], outline=black, fill=red)

# Icon 2: Triangle
draw.polygon([(600, 150), (650, 150), (625, 200)], outline=black, fill=red)

# Icon 3: Square
draw.rectangle([700, 50, 750, 100], outline=black, fill=red)

icon = Image.open('icon.png')
image.paste(icon, (50, 400))


# Save the image as a black BMP file
image_black = image.copy()
draw_black = ImageDraw.Draw(image_black)
# Replace all red pixels with black
for x in range(image_black.width):
    for y in range(image_black.height):
        if image_black.getpixel((x, y)) == red:
            image_black.putpixel((x, y), black)
image_black.save('output_black.bmp')

# Save the image as a red BMP file
image_red = image.copy()
draw_red = ImageDraw.Draw(image_red)
# Replace all black pixels with red
for x in range(image_red.width):
    for y in range(image_red.height):
        if image_red.getpixel((x, y)) == black:
            image_red.putpixel((x, y), red)
image_red.save('output_red.bmp')

print("Images saved as output_black.bmp and output_red.bmp")