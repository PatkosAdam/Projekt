""" import slate3k as slate
with open('foo.pdf', 'rb') as f:
    text = slate.PDF(f)
print(text) """

from PyPDF2 import PdfReader

reader = PdfReader("foo.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()
print(text)