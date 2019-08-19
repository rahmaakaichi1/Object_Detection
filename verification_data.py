import csv
import cv2
import os
import numpy as np
 
FOLDER = '/content/Tensorflow_object_detector/workspace/training_OD/images/RGBImages'
CSV_FILE = '/content/Tensorflow_object_detector/workspace/training_OD/annotations/train.csv'
 
with open(CSV_FILE, 'r') as fid:
   
    print('Checking file:', CSV_FILE, 'in folder:', FOLDER)
   
    file = csv.reader(fid, delimiter=',')
    first = True
   
    cnt = 0
    error_cnt = 0
    error = False
    for row in file:
        if error == True:
            error_cnt += 1
            error = False
           
        if first == True:
            first = False
            continue
       
        cnt += 1
       
        name, width, height, xmin, ymin, xmax, ymax = row[0], float(row[1]), float(row[2]), float(row[4]), float(row[5]), float(row[6]), float(row[7])
       
        path = os.path.join(FOLDER, name)
        img = cv2.imread(path)
       
       
        if type(img) == type(None):
            error = True
            print('Could not read image', img)
            continue
       
        org_height, org_width = img.shape[:2]
       
        if org_width != width:
            error = True
            print('Width mismatch for image: ', name, width, '!=', org_width)
        if org_height != height:
            error = True
            print('Height mismatch for image: ', name, height, '!=', org_height)
       
        if xmin > org_width:
            error = True
            print('XMIN=' , xmin, '>' , org_width, 'for filename', name)

        if xmax > org_width:
            error = True
            print('XMAX=', xmax, '>', org_width, 'for filename', name)
       
        if ymin > org_height:
            error = True
            print('YMIN=', ymin, '>', org_height, 'for filename', name)
       
        if ymax > org_height:
            error = True
            print('YMAX=', ymax, '>', org_height, 'for filename', name)
       
        if error == True:
            print('Error for file: %s' % name)
            print()
       
    print('Checked %d files and realized %d errors' % (cnt, error_cnt))