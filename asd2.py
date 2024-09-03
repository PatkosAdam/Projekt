from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = './Tesseract-OCR/tesseract'

print(pytesseract.image_to_string(Image.open("test.png"), lang='hun'))
# print(pytesseract.get_languages())
print(pytesseract.image_to_string(Image.open("angol.png")))
