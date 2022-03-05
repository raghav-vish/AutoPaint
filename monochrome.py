from PIL import Image, ImageOps
import pyautogui
import time

pyautogui.PAUSE=0.001 #Lower the number, faster the program will run

img=Image.open("cs.jpg") # Replace with the path of the image you want painted
img=ImageOps.scale(img, factor=0.5) #To scale down huge images
pixels = img.load()


'''Defines starting location.
startx and starty can be changed to start painting from another place.
Ensure that the location is on the paint window and entire image will
fit in the paint window'''
startx=16
starty=190

time.sleep(3)
for i in range(img.size[0]):
	for j in range(img.size[1]):
		if(grscl_pixels[i,j]>85):
			pyautogui.click(startx+i, starty+j)