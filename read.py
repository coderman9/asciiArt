from __future__ import print_function
from PIL import Image
import math
import sys
import codecs
def mean(vals):
	m=0
	for i in vals:
		if i:
			m+=i
	return(m/len(vals))
#finds the index of the element in sorted arr closest in value to val
def closest(val, arr):
	for i in range(len(arr)):
		if(val>=arr[i] and val<=arr[i+1]):
			if abs(arr[i]-val)<abs(arr[i+1]-val):
				return i
			return i+1
	return(len(arr)-1)

#brightness of each character as a fraction of the darkest char. starts at ascii 33
fBrightness=[0.37037037037037035,0.2222222222222222,0.8148148148148148,1.0,0.7777777777777778,0.7407407407407407,0.14814814814814814,0.4444444444444444,0.4444444444444444,0.3333333333333333,0.3333333333333333,0.14814814814814814,0.18518518518518517,0.07407407407407407,0.2962962962962963,0.9629629629629629,0.7407407407407407,0.8148148148148148,0.7777777777777778,0.8148148148148148,0.8888888888888888,0.8888888888888888,0.7037037037037037,0.9259259259259259,0.8888888888888888,0.14814814814814814,0.2222222222222222,0.37037037037037035,0.2962962962962963,0.37037037037037035,0.4444444444444444,0.8888888888888888,0.8518518518518519,0.8888888888888888,0.7037037037037037,0.8888888888888888,0.8148148148148148,0.6666666666666666,0.8148148148148148,1.0,0.6153846153846154,0.6538461538461539,0.8846153846153846,0.6923076923076923,0.8076923076923077,0.9230769230769231,0.8461538461538461,0.8076923076923077,0.9230769230769231,0.9615384615384616,0.8076923076923077,0.6923076923076923,0.9230769230769231,0.6923076923076923,0.7692307692307693,0.7692307692307693,0.7692307692307693,0.8461538461538461,0.6923076923076923,0.3076923076923077,0.6923076923076923,0.3076923076923077,0.23076923076923078,0.15384615384615385,0.8076923076923077,0.9230769230769231,0.6153846153846154,1.0,0.6923076923076923,0.8076923076923077,1.0,0.9230769230769231,0.6923076923076923,0.7307692307692307,0.9230769230769231,0.7692307692307693,0.6923076923076923,0.7307692307692307,0.6923076923076923,0.9615384615384616,1.0,0.7727272727272727,0.8636363636363636,0.9090909090909091,0.9545454545454546,0.6818181818181818,0.8181818181818182,0.9090909090909091,1.0,1.0,1.0,0.4375,1.0,]
ufBrightness=list(fBrightness)
fBrightness.sort()

im=Image.open(sys.argv[1])
width, height=im.size
pixel=list(im.getdata())
brightness=[[None for x in range(width)] for y in range(height)]
for i in range(height):
	for j in range(width):
		#current pixel
		cpix=pixel[i*width+j]
		#magic numbers found online
		brightness[i][j]=(0.299*cpix[0]**2+0.587*cpix[1]**2+0.114*cpix[2]**2)**0.5
#save with the same name as fiven file but different extension
with codecs.open(((sys.argv[1].split(".")[0])+".txt"), "w", "utf-16") as ti:
	for i in range(0, height-2, 2):
		for j in range(0, width-2, 2):
			#needs to be switched for white on black
			b=(255-mean((brightness[i][j], brightness[i+1][j], brightness[i][j+1], brightness[i+1][j+1], brightness[i+2][j])))/255
			ti.write(chr(ufBrightness.index(fBrightness[closest(b,fBrightness)])+33))
		ti.write("\n")