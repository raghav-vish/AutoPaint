from PIL import Image, ImageOps
import pyautogui
import time

pyautogui.PAUSE=0.001 #Lower the number, faster the program will work.
img=Image.open("cs.jpg") #Replace with path of image you want painted
img=ImageOps.scale(img, factor=0.7) #To scale down huge images
img=ImageOps.posterize(img,4) #To reduce the number of colors. (Between 1 and 8)
pixels = img.load()

time.sleep(3)
colors={}

'''Creates a dictinoary of all colors and what positions they are at'''
for i in range(img.size[0]):
	for j in range(img.size[1]):
		if(pixels[i,j] in colors):
			colors[pixels[i,j]].append((i,j))
		else:
			colors[pixels[i,j]]=[(i,j)]

'''To find out which color occurs most. If one color 
occurs a lot, it saves time to set the Paint background
to that color before starting.'''			
maxn=0
for c in colors:
	if(len(colors[c])>maxn):
		maxn=len(colors[c])
		maxc=c


'''Defines all the required locations on screen. Currently hardcoded
to a 1080p (1920x1080) screen.

startx and starty can be changed to start painting from another place.
Ensure that the location is on the paint window and entire image will
fit in the paint window
'''
startx=16
starty=190
changecx=1173
changecy=83
rx=1225
ry=604
gx=1225
gy=635
bx=1225
by=360

'''
Logic for the actual painting. Remove the commented code 
if the majority color as described above is set as the background.
'''
for c in colors:
	r,g,b=c
	'''if(c==maxc):
		continue'''
	pyautogui.PAUSE=0.1
	pyautogui.click(changecx, changecy)
	pyautogui.click(rx,ry)
	pyautogui.hotkey('backspace')
	pyautogui.hotkey('backspace')
	pyautogui.hotkey('backspace')
	pyautogui.typewrite(str(r))
	pyautogui.hotkey('tab')
	pyautogui.typewrite(str(g))
	pyautogui.hotkey('tab')
	pyautogui.typewrite(str(b))
	pyautogui.hotkey('enter')
	pyautogui.PAUSE=0.01
	for pos in colors[c]:
		x,y=pos
		print(c,pos)
		pyautogui.click(startx+x, starty+y)