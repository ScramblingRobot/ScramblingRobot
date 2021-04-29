import cv2;
import math;
import numpy;

#name: the name of the image to read, probably something like "new1.jpg"
#returns the width of the cube in millimeters as a decimal
#import at the top of your file using "from IPmeasure import *;"
def cMeasure(name):
	filename = name;
	img = cv2.imread(filename);
	height, width, channels = img.shape;

	#height = math.trunc(height/2.5);
	orig = img.copy()
	grayimg = orig.copy()
	img = img[320:420,670:1680]
	
	img = cv2.resize(img, None, fx = 1/8, fy = 1/8, interpolation = cv2.INTER_NEAREST);
	grayimg = cv2.resize(grayimg, None, fx = 1/8, fy = 1/8, interpolation = cv2.INTER_NEAREST);

	img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	grayimg = cv2.cvtColor(grayimg, cv2.COLOR_BGR2HSV)

	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
	gray = cv2.Canny(gray, 50, 200);
	gray = cv2.dilate(gray, None, iterations = 2);
	contours, hierarchy = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE);
	c = max(contours, key = cv2.contourArea);

	grayorig = cv2.cvtColor(grayimg, cv2.COLOR_BGR2GRAY);
	grayorig = cv2.Canny(grayorig, 50, 200);
	grayorig = cv2.dilate(grayorig, None, iterations = 2);
	contours2, hierarchy = cv2.findContours(grayorig, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE);
	c2 = max(contours2, key = cv2.contourArea);

	minx, miny, maxx, maxy = cv2.boundingRect(c);
	cv2.rectangle(img, (minx, miny), (maxx, maxy), (0, 255, 0), 1);
	minx += 2
	maxx -= 4
	distance = max(maxx - 1, minx - 1);
	distanceact = distance*8 + 3
	cent = (math.trunc((distance/10.1)*10))/10;
	#print("distance (pixels crop): ", distance);
	#print("distance (pixels actual): ", distanceact);
	#print("distance (centimeters): ", cent,"cm");
	cv2.circle(img, (maxx, miny+1), 0, (0, 0, 255), 2);
	cv2.circle(img, (minx, miny+1), 0, (255, 0, 0), 2);

	endpoint = distanceact + 671;
	cv2.circle(orig, (671, 320), 0, (0, 0, 255), 10);
	cv2.circle(orig, (endpoint, 320), 0, (0, 0, 255), 10);

	img = cv2.resize(img, None, fx = 3, fy = 3, interpolation = cv2.INTER_NEAREST);
	orig = cv2.resize(orig, None, fx = 1/3, fy = 1/3, interpolation = cv2.INTER_NEAREST);
	#cv2.imshow('image', img);
	#cv2.imshow('original', orig);
	#cv2.waitKey();

	return cent*10