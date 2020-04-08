
import math
from PIL import Image
imgx = 10000
imgy = 5000
image = Image.new("RGB", (imgx, imgy))

xa = 3.2388663968
xb = 4.0
maxit = 1000

for i in range(imgx):
    r = xa + (xb - xa) * float(i) / (imgx - 1)
    x = 0.00003160718
    for j in range(maxit):
        x = r * x * (1 - x)
        if j > maxit / 2:
            image.putpixel((i, int(x * imgy)), (255, 255, 255))

image.save("Bifurcation1.png", "PNG")
