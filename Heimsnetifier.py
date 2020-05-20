from PIL import Image, ImageDraw, ImageFilter

mask = Image.open("images/heimsnet_logo_template_tp.png")

directory = input("Please specify the full path of the image you want converted: ")

img = Image.open(directory).resize(mask.size)
background = Image.open("images/background_tp.png").resize(mask.size)

im = Image.composite(img, background, mask)
im.save("img.png")