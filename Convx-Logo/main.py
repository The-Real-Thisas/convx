from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

# importing the image
img = Image.open("convx-logo.png")
draw = ImageDraw.Draw(img)

# loading the font and providing the size
font = ImageFont.truetype("RobotoMono-Light.ttf", 50)

versionNumber = input("Version: ")
# specifying coordinates and colour of text
draw.text((65, 70), versionNumber, (0, 0, 0), font=font)

# saving the image
img.save("convx-banner.png")
