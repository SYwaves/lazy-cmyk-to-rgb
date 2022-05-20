def floor(color):
    """Convert from % to 0-255"""
    color=color/100*255
    if color>255:
        return 255
    elif color<0:
        return 0
    else:
        return int(color)

def threshold(color):
    if color>50:
        return colorspace * color*(1+(color-75)/100)**0.5 * colorspace**2 *0.9
    else:
        return colorspace * color*(color/50)**(colorspace)

print('c=')
c = int(input())
print('m=')
m = int(input())
print('y=')
y = int(input())
print('k=')
k = int(input())


rgb = [0,0,0]
bias = [1.04,0.96,1.05] #weighted conversion for each color channel
colorspace = 0.79 #simulate cmyk's narrower color gamut
bright_mul = 1 - k/100 #inverting black channel for convenience

rgb[0] = (100-c*colorspace) * (bright_mul+(bias[0]*colorspace*0.45))*bias[0]
rgb[1] = (100-m*colorspace) * (bright_mul+(bias[1]*colorspace*0.45))*bias[1]
rgb[2] = (100-y*colorspace) * (bright_mul+(bias[2]*colorspace*0.45))*bias[2]

rgb[0] = threshold(rgb[0])
rgb[1] = threshold(rgb[1])
rgb[2] = threshold(rgb[2])

rgb[0] = floor(rgb[0])
rgb[1] = floor(rgb[1])
rgb[2] = floor(rgb[2])

print('cmyk(',int(c),',',int(m),',',int(y),',',int(k), ') roughly equates to rgb',rgb[0:])