from PIL import Image, ImageFilter

try:
    original = Image.open("darwin.png")
    blurred = original.filter(ImageFilter.GaussianBlur())
    blurred.show()
    blurred.save("blurred.png")
except:
    print("Unable to load image")
