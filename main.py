from PIL import Image

image = Image.open("svaston.jpg")

box = (64, 64, 128, 128)
region= image.crop(box)
r, g, b = region.split()
region = Image.merge("RGB", (g, b, r))
image.paste(region, box)

box = (64, 0, 128, 64)
region = image.crop(box)
region = region.rotate(45)
image.paste(region, box)
region.show()
image.show()

image = Image.open("svaston.jpg")
box = (64, 64, 128, 128)
region= image.crop(box)
r, g, b = region.split()
region = Image.merge("RGB", (g, b, r))
image.paste(region, box)

box = (0, 64, 64, 128)
region = image.crop(box)
region = region.rotate(117)
r, g, b = region.split()
region = Image.merge("RGB", (b, r, g))
image.paste(region, box)

image.show()
image.save("svaston.jpg")