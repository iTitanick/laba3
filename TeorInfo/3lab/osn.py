from PIL import Image, ImageDraw
from numpy import asarray
import random
popa = []


img = Image.open('two.jpg')
numpydata = asarray(img)

draw = ImageDraw.Draw(img)
width = img.size[0]
height = img.size[1]