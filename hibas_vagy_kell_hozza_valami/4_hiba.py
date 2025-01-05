import barcode
from barcode.writer import ImageWriter
from IPython.display import Image, display

barcode_format = barcode.get_barcode_class('ean13')

barcode_number = '123456789012'

barcode_image = barcode_format