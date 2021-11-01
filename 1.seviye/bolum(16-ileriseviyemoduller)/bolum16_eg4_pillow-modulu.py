from PIL import Image,ImageFilter
#
image = Image.open("kuş.jpg")
#
# image.filter(ImageFilter.GaussianBlur(10)).save("kuş2.jpg")
#
kırpılacak_alan = (155,155,1500,1100)
image.crop(kırpılacak_alan).save("kus1.jpg")
# image.rotate(180).save("kuş2.jpg")
#
# image.convert(mode = "L").save("kuş22.jpg")
