from PIL import Image

im = Image.open('1.jpg')
w,h=im.size
print('Original image size: %sx%s' % (w, h))
im.thumbnail((w//2,h//2))
print('Resize image to: %s*%s' % (w//2,h//2))
im.save('thumbnail.jpg','jpeg')

from PIL import Image,ImageFilter

im2=Image.open('1.jpg')
im3=im2.filter(ImageFilter.BLUR)
im3.save('blur.jpg','jpeg')

