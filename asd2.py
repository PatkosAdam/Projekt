from PIL import Image
import pytesseract
import pdf2image
import tabula
from pdf2image import convert_from_path
pytesseract.pytesseract.tesseract_cmd = './Tesseract-OCR/tesseract'


#print(pytesseract.get_languages())
#print(pytesseract.image_to_string(Image.open("angol.png")))
#print(pytesseract.image_to_string(Image.open('tabla.png')))

images = convert_from_path("valami.pdf", poppler_path= "site-packages\\poppler-24.07.0\\Library\\bin")

for i in range(len(images)):
  # Save pages as images in the pdf
  images[i].save('page'+ str(i) +'.jpg', 'JPEG')

print(pytesseract.image_to_string(Image.open("page9.jpg"), lang='hun'))
#b =print(pytesseract.image_to_string(Image.open("page10.jpg"), lang='hun'))
#c =print(pytesseract.image_to_string(Image.open("page11.jpg"), lang='hun'))
#d =print(pytesseract.image_to_string(Image.open("page12.jpg"), lang='hun'))
