from PIL import Image
from PIL import ImageDraw
from math import sqrt, atan2, pi, isnan

"""
A simplified version of the HSL color picker. H can be a number from 0 to 1
(representing the percentage of the way around the color wheel) and L represents
lightness. However, it only goes from 0% to 50% lightness, as the program doesn't
use anything lighter than that.
"""
def color_picker(H, L):
    
    if isnan(H): return (255, 255, 255)
    
    if 0 <= H < 1/6:
        R = 255
        G = 255 * H * 6
        B = 0
    if 1/6 <= H < 1/3:
        R = 255 - 255 * (H - 1/6) * 6
        G = 255
        B = 0
    if 1/3 <= H < 1/2:
        R = 0
        G = 255
        B = 255 * (H - 1/3) * 6
    if 1/2 <= H < 2/3:
        R = 0
        G = 255 - 255 * (H - 1/2) * 6
        B = 255
    if 2/3 <= H < 5/6:
        R = 255 * (H - 2/3) * 6
        G = 0
        B = 255
    if 5/6 <= H <= 1:
        R = 255
        G = 0
        B = 255 - 255 * (H - 5/6) * 6
        
    R = int(R * L)
    G = int(G * L)
    B = int(B * L)

    return (R, G, B)

"""
This function creates the real and imaginary axes, placing tick marks
at every 50 pixels to represent one unit.
"""
def make_axes():
    
    global image
    global R, G, B
    
    R, G, B = 255, 255, 255
    
    for i in range(1000):
        
        image.putpixel((499, i), (R, G, B))
        image.putpixel((500, i), (R, G, B))
        image.putpixel((i, 499), (R, G, B))
        image.putpixel((i, 500), (R, G, B))
        
        if i % 50 in [0, 49]:
            for j in range(495, 506):
                image.putpixel((i, j), (R, G, B))
                image.putpixel((j, i), (R, G, B))
                
    I1 = ImageDraw.Draw(image)
    I1.text((965, 480), "Re(x)", fill = (R, G, B))
    I1.text((510, 5), "Im(x)", fill = (R, G, B))
    
    for i in range(-8, 10, 2):
        if i < 0: I1.text((i * 50 + 495, 482), str(i), fill = (255, 255, 255))
        if i > 0: I1.text((i * 50 + 498, 482), str(i), fill = (255, 255, 255))
    for j in range(-8, 10, 2):
        if j != 0: I1.text((510, j * -50 + 495), str(j) + "i", fill = (255, 255, 255))

"""
Used for the make_box function. If a value on the abs() axis is very large, this
function shortens it so that it fits.
"""
def shorten(s):
    s = str(s)
    if len(s) <= 6: return s
    return s[0] + "." + s[1] + "e" + str(len(s) - 1) 
    
"""
This function creates a box in the bottom-right corner of the screen displaying
the scale for abs(y) and arg(y).
"""
def make_box():
    
    global image
    
    I1 = ImageDraw.Draw(image)
    
    for i in range(800, 961):
        for j in range(800, 937):
            if i in [800, 801, 959, 960] or j in [770, 771, 800, 801, 935, 936]:
                image.putpixel((i, j), (255, 255, 255))
            else:
                image.putpixel((i, j), (0, 0, 0))
    #I1.text((810, 780), "y = x^2", fill = (255, 255, 255))
    
    I1.text((810, 810), "abs(y)", fill = (255, 255, 255))
    for i in range(810, 841):
        for j in range(825, 927):
            if i in [810, 811, 839, 840] or j in [825, 826, 925, 926]:
                image.putpixel((i, j), (255, 255, 255))
            else:
                g = int((926 - j) / 101 * 256)
                image.putpixel((i, j), (g, g, g))
    r, l = funcrange()
    continuous_vals = ["inf", "2.4142", "1", "0.4142", "0"]
    for j in range(825, 927, 25):
        for i in range(841, 846):
            image.putpixel((i, j), (255, 255, 255))
            image.putpixel((i, j + 1), (255, 255, 255))
        if mode == "linear": I1.text((i + 5, j - 5), shorten(int(r - ((j - 825) / 100) * (r - l))), fill = (255, 255, 255))
        if mode == "continuous": I1.text((i + 5, j - 5), continuous_vals[(j - 825) // 25], fill = (255, 255, 255))
            
        
    I1.text((885, 810), "arg(y)", fill = (255, 255, 255))
    for i in range(885, 916):
        for j in range(825, 927):
            if i in [885, 886, 914, 915] or j in [825, 826, 925, 926]:
                image.putpixel((i, j), (255, 255, 255))
            else:
                image.putpixel((i, j), color_picker((926 - j) / 101, 1))
    for j in range(825, 927, 25):
        for i in range(916, 921):
            image.putpixel((i, j), (255, 255, 255))
            image.putpixel((i, j + 1), (255, 255, 255))
    I1.text((925, 820), "0", fill = (255, 255, 255))
    I1.text((925, 845), "pi/2", fill = (255, 255, 255))
    I1.text((925, 870), "pi", fill = (255, 255, 255))
    I1.text((925, 895), "3pi/2", fill = (255, 255, 255))
    I1.text((925, 920), "2pi", fill = (255, 255, 255))

"""
This function converts a pixel's coordinate into what it represents on the
image. Note that this function returns the value of the CENTER of the pixel,
and since there are an even number of pixels in the image, no pixel can
represent the "origin". Thus, the closest we can get is (0.01, 0.01); this
would correspond to the pixel location (500, 499) in the image.
"""   
def convertCoordinates(x, y):
    return x / 50 - 9.99 + (9.99 - y / 50) * 1j

"""
This function returns the minimum and maximum values of abs(x) for the chosen
function as a tuple. For example, if our chosen function is y = x, this function
will roughly return (0, 14.14).
"""
def funcrange():
    
    l = sqrt(func1(-9.99 - 9.99j).real ** 2 + func1(-9.99 - 9.99j).imag ** 2)
    r = l
    
    for i in range(1000):
        for j in range(1000):
            
            x = func1(convertCoordinates(i, j))
            re, im = x.real, x.imag
            abs = sqrt(re ** 2 + im ** 2)
            
            if abs < l: l = abs
            if abs > r: r = abs
            
    return (r, l)

"""
This is the chosen function we are graphing.
"""
def func1(x):

    n = x ** 2
    
    return n

"""
This graphs our chosen function onto an image by "mapping" each pixel on the
imaginary and real axes to a color corresponding to the new value.
There are two different "modes" in which the function can be graphed: In "linear"
mode, the chosen value is divided by the function's range in order to pick a value
for lightness on the color scale. This is best used with functions with small ranges,
although the program will arbitrarily choose the scale based on the range of the
function. In "continuous" mode, the function's range isn't taken into account, and
any value from 0 to infinity can be mapped as a color. This is best used when
"linear" mode doesn't capture the full geometry of a function.
"""
def make_graph():
    
    global image
    global R, G, B
    global mode
    
    r = funcrange()
    
    for i in range(1000):
        for j in range(1000):
            
            x = func1(convertCoordinates(i, j))
            re, im = x.real, x.imag
            
            abs = sqrt(re ** 2 + im ** 2)
            arg = atan2(im, re) % (2 * pi) / (2 * pi)
            if mode == "linear":
                if r[1] == r[0]: abs = 1
                else: abs = 1 - (abs - r[0]) / (r[1] - r[0])
            if mode == "continuous":
                from math import atan
                if r[1] == r[0]: abs = 0
                else: abs = atan(abs) / (2 * atan(1))
            
            image.putpixel((i, j), color_picker(arg, abs))

"""
This is the main method, where we execute all of our methods to create an image!
"""
if __name__ == "__main__":
    image = Image.new(mode="RGB", size=(1000, 1000), color = "black")
    
    mode = "linear"
    
    make_graph()
    make_axes()
    make_box()
    
    image.show()
    image.save("mapping.png", format="png")
