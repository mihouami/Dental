from PIL import Image

# Open the image file
image = Image.open("main/static/main/images/about-2.jpg")

# Get the width and height of the image
width, height = image.size

print("Width:", width)
print("Height:", height)
