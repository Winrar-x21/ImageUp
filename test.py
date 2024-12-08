from PIL import Image, ImageFilter

image = Image.open('jenny.png')
image = image.filter(ImageFilter.UnsharpMask())

image.show()