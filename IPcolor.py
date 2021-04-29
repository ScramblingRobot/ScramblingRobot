import cv2;
import math;
import numpy;

#name: the name of the image to read, probably something like "stress.jpg"
#returns a list of all of the colors, from top to bottom, left to right
#import at the top of your file using "from IPcolor import *;"
def cColor(name):
	filename = name;
	img = cv2.imread(filename);

	img = cv2.resize(img, None, fx = 1/8, fy = 1/8, interpolation = cv2.INTER_NEAREST);
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
	gray = cv2.Canny(gray, 30, 200);
	gray = cv2.dilate(gray, None, iterations = 2);
	contours, hierarchy = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE);
	c = max(contours, key = cv2.contourArea);

	colors = [];
 
	#Begin code based on Miki's answer to the question "How to crop away convexity defects?" at https://stackoverflow.com/a/35252058, available under CC-BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/legalcode)
	defects = cv2.convexityDefects(c, cv2.convexHull(c, returnPoints = 0));
	while 1:
		defectsIdx = [];
		for i in range(defects.shape[0]):
			depth = defects[i][0][3] / 256;
			if depth > 2:
				defectsIdx.append(defects[i][0][2]);
		if len(defectsIdx) < 2:
			break;
		minDist = math.inf;
		startIdx = 0;
		endIdx = 0;
		for i in range(len(defectsIdx)):
			for j in range(i+1, len(defectsIdx)):
				dist = pow(c[defectsIdx[i]][0][0] - c[defectsIdx[j]][0][0], 2) + pow(c[defectsIdx[i]][0][1] - c[defectsIdx[j]][0][1], 2);
				if minDist > dist:
					minDist = dist;
					startIdx = defectsIdx[i];
					endIdx = defectsIdx[j];
		if startIdx <= endIdx:
			len1 = endIdx - startIdx;
			len2 = len(c) - endIdx + startIdx;
			if len2 < len1:
				temp = startIdx;
				startIdx = endIdx;
				endIdx = temp;
		else:
			len1 = startIdx - endIdx;
			len2 = len(c) - startIdx + endIdx;
			if len1 < len2:
				temp = startIdx;
				startIdx = endIdx;
				endIdx = temp;
		if startIdx <= endIdx:
			c = numpy.concatenate((c[:startIdx], c[endIdx:]));
		else:
			c = c[endIdx:startIdx];
		defects = cv2.convexityDefects(c, cv2.convexHull(c, returnPoints = 0));
	#End code based on Miki's answer to the question "How to crop away convexity defects?" at https://stackoverflow.com/a/35252058, available under CC-BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/legalcode)
 
	#Begin code based on DomTomCat's answer to the question "White balance algorithm [closed]" at https://stackoverflow.com/a/37854585, available under CC-BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/legalcode)
	for i in range(3):
		channel = img[..., i];
		mi, ma = numpy.percentile(img[..., i], 0.05), numpy.percentile(channel, 100.0 - 0.05);
		img[..., i] = numpy.uint8(numpy.clip((channel - mi) * 255.0/(ma-mi), 0, 255));
	#End code based on DomTomCat's answer to the question "White balance algorithm [closed]" at https://stackoverflow.com/a/37854585, available under CC-BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/legalcode)
 
	minx, miny, maxx, maxy = cv2.boundingRect(c);
	maxx += minx;
	maxy += miny;
	for y in range(7):
		for x in range(7):
			bgr = img[miny+int(6*(maxy-miny)/49*(y+1)+(maxy-miny)/98), minx+int(6*(maxx-minx)/49*(x+1)+(maxx-minx)/98)]; #y, x
			hsv = cv2.cvtColor(numpy.uint8([[bgr]]), cv2.COLOR_BGR2HSV)[0][0];
			if 20 < hsv[2] < 255:
				if hsv[1] > 51:
					if 130 < hsv[0] <= 175:
						#print("red", end=" ");
						colors.append("red");
					elif hsv[0] <= 25 or hsv[0] > 175:
						#print("orange", end=" ");
						colors.append("orange");
					elif 25 < hsv[0] <= 35 or (35 < hsv[0] <= 45 and hsv[1] < 204):
						#print("yellow", end=" ");
						colors.append("yellow");
					elif 45 < hsv[0] <= 80 or (35 < hsv[0] <= 45 and hsv[1] >= 204):
						#print("green", end=" ");
						colors.append("green");
					elif 80 < hsv[0] <= 130:
						#print("blue", end=" ");
						colors.append("blue");
				else:
					#print("white", end=" ");
					colors.append("white");
        	#debug
			cv2.circle(img, (minx+int(6*(maxx-minx)/49*(x+1)+(maxx-minx)/98), miny+int(6*(maxy-miny)/49*(y+1)+(maxy-miny)/98)), 0, (0, 0, 255), 3);
		#print("");

	img = cv2.resize(img, None, fx = 1.5, fy = 1.5, interpolation = cv2.INTER_NEAREST);
	#cv2.imshow('image', img);
	#cv2.imwrite("test.png", img);
	#cv2.waitKey();

	return [colors];