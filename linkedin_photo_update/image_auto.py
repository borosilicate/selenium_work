from PIL import Image
import random
import cv2
#import numpy as np
#import selenium
#cv2.namedWindow('Mid_test',cv2.WINDOW_NORMAL)

#                       WHERE I STORE MY IMAGES
image = cv2.imread('/home/pi/Pictures/me.full.png',cv2.IMREAD_UNCHANGED)
#print('HEIGHT:',image.shape[0],' ',"WIDTH:",image.shape[1])
height = image.shape[0]
hh=1380#height//3
width = image.shape[1]
hw=width//2
#c1,c2,c3=random.randint(0,255),random.randint(0,255),random.randint(0,255)
#random loop
for i in range(0,125):
	rh=random.randint(0,800) #random Height
	rw=random.randint(0,hw) #random Width
	c1,c2,c3=255,255,255
	chance=random.randint(0,6)
	if(chance>1):
		c1,c2,c3=random.randint(0,255),random.randint(0,255),random.randint(0,255)
	elif(chance):
		c1,c2,c3=0,0,0
	size=6 #random.randint(1,10)
	cv2.line(image, (0,hh-rh), (hw,hh+rh), (c1,c2,c3), size)
	cv2.line(image, (0,hh+rh), (hw,hh-rh), (c1,c2,c3), size)
	cv2.line(image, (width,hh-rh), (hw,hh+rh), (c1,c2,c3), size)
	cv2.line(image, (width,hh+rh), (hw,hh-rh), (c1,c2,c3), size)
	#print(f'line{i}')
#			WHERE I STORE MY IMAGES
#			This photo is of me cut out with gimp
foreground= Image.open('/home/pi/Pictures/me.gone_alpha.png')
image_test=cv2.resize(image,(960,540))
#cv2.imshow('Mid_test',image_test)
#cv2.waitKey(0)
#print('Almost Done')
image=Image.fromarray(image)
final2=Image.new('RGBA',image.size)
final2=Image.alpha_composite(final2,image.convert('RGBA'))
#final2.show()
final2=Image.alpha_composite(final2,foreground)
#final2.show()
#			Final Product
final2.save('/home/pi/Pictures/me.linkedin.png')
cv2.destroyAllWindows()
