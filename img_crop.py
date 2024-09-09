# Importing Image class from PIL module
from PIL import Image
 
# Opens a image in RGB mode
im = Image.open("1725356316685-c6707062-78f7-4dca-9c34-3027e181796ce 3 aug_1.jpg")
 
# Size of the image in pixels (size of original image)
# (This is not mandatory)
width, height = im.size
 
# Setting the points for cropped image
left = 85
top = 100
right = 600
bottom = 600
 
# Cropped image of above dimension
# (It will not change original image)
im1 = im.crop((left, top, right, bottom))
 
# Shows the image in image viewer
im1.show()