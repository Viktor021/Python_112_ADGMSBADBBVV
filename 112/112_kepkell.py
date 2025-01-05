from PIL import Image

Original_Image = 'pushpa.jpg'

img = Image.open(Original_Image)

Mirror_Image = img.transpose(Image.FLIP_LEFT_RIGHT)

Mirrored_Image = 'pushpa_mirror.png'
Mirror_Image.save(Mirrored_Image)

Image.open(Mirrored_Image)