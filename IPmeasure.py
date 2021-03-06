import cv2;
import math;
import numpy;

#name: the name of the image to read, probably something like "new1.jpg"
#returns the width of the cube in milimeters as a decimal
#import at the top of your file using "from IPmeasure import *;"
def cMeasure(name):
    filename = name;
    img = cv2.imread(filename);
    img = cv2.rotate(img, cv2.cv2.ROTATE_180);
    height, width, channels = img.shape;

    #height = math.trunc(height/2.5);
    orig = img.copy()
    grayimg = orig.copy()
    #img = img[320:420,670:1680]
    img = img[355:445,800:1480]
    
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
    cent = (math.trunc((distance/10.4)*10))/10;
    #print("distance (pixels crop): ", distance);
    #print("distance (pixels actual): ", distanceact);
    #print("distance (centimeters): ", cent,"cm");
    #cv2.circle(img, (maxx, miny+1), 0, (0, 0, 255), 2);
    #cv2.circle(img, (minx, miny+1), 0, (255, 0, 0), 2);
    
    mm = round (cent * 10)
    if (mm > 46) & (mm < 52):
        rightLine = round(811 + (76 / 9) * 49)
        string = "49mm"
        mm = 49
        
    elif (mm > 51) & (mm < 57):
        rightLine = round(811 + (76 / 9) * 54)
        string = "54mm"
        mm = 54

    elif (mm > 57) & (mm < 63):
        rightLine = round(811 + (76 / 9) * 60)
        string = "60mm"
        mm = 60
        
    elif (mm > 64) & (mm < 73):
        rightLine = round(811 + (76 / 9) * 68)
        string = "68mm"
        mm = 68
        
    else:
        rightLine = round(811 + (76 / 9) * mm)
        string = "%dmm" % (mm)

    endpoint = distanceact + 811;
    #cv2.circle(orig, (671, 320), 0, (0, 0, 255), 10);
    #cv2.circle(orig, (811, 320), 0, (0, 255, 255), 10);
    #cv2.circle(orig, (endpoint, 320), 0, (0, 0, 255), 10);
    cv2.line(orig, (811,450), (811,100), (0, 255, 255), 3);
    #cv2.line(orig, (1267,440), (1267,90), (0, 255, 255), 3); change 1
    cv2.line(orig, (rightLine,440), (rightLine,90), (0, 255, 255), 3); #change 1

    cv2.line(orig, (811,320), (811,360), (0, 0, 255), 3);
    #cv2.line(orig, (811,340), (1267,340), (0, 0, 255), 3); #change 2
    cv2.line(orig, (811,340), (rightLine,340), (0, 0, 255), 3); #change 2
    #cv2.line(orig, (1267,320), (1267,360), (0, 0, 255), 3); #change 3
    cv2.line(orig, (rightLine,320), (rightLine,360), (0, 0, 255), 3); #change 3
    
        
    #cv2.putText(orig, '54mm', (1267,360), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA) #change 4
    cv2.putText(orig, string, (rightLine,360), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA) #change 4
    orig = orig[0:750,500:1600]
    
    img = cv2.resize(img, None, fx = 3, fy = 3, interpolation = cv2.INTER_NEAREST);
    orig = cv2.resize(orig, None, fx = 1/2, fy = 1/2, interpolation = cv2.INTER_NEAREST);
    #cv2.imshow('image', img);
    cv2.imshow('Cube Dimensions', orig);
    cv2.waitKey();

    return mm
