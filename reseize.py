%matplotlib inline 
import cv2
import csv

from matplotlib import pyplot as plt
import numpy as np

#fucntio, to draw boxes corresponding to the given coordinates
def drawBox(boxes, image):
    for i in range(0, len(boxes)):
        # changed color and width to make it visible
        cv2.rectangle(image, (boxes[i][2], boxes[i][3]), (boxes[i][4], boxes[i][5]), (255, 0, 0), 1)
    #cv2.imshow("img", image)
    plt.imshow(image)
    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def cvTest():
    
        FOLDER = '/content/Tensorflow_object_detector/workspace/training_OD/images/RGBImages'
        CSV_FILE = '/content/Tensorflow_object_detector/workspace/training_OD/annotations/dataset_in.csv'
        new_rows = []
        rows_to_delete = []
        
 
        with open(CSV_FILE, 'r') as fid:
   
                print('Checking file:', CSV_FILE, 'in folder:', FOLDER)
   
                file = csv.reader(fid, delimiter=',')
                first = True
   
                cnt = 0
                error_cnt = 0
                error = False
                for row in file:
                    new_row = row
                    if error == True:
                         error_cnt += 1
                         error = False
           
                    if first == True:
                        first = False
                        continue
       
                    cnt += 1

                    name = row[0]
                    file_name = os.path.join(FOLDER, name)
                    print("Processing %s" % file_name)
                    #image = Image.open(os.path.join(directory, file_name))

                    imageToPredict = cv2.imread(file_name, 3)
                    if type(imageToPredict) == type(None):
                           error = True
                           print('Could not read image', imageToPredict)
                           changes = { }
                
                           for key ,value in changes.items():
                                new_row = [x.replace(key,str(value)) for x  in new_row ]
                           new_rows.append(new_row)
                           continue
                    print(imageToPredict.shape)
                    # Note: flipped comparing to your original code!
                    # x_ = imageToPredict.shape[0]
                    # y_ = imageToPredict.shape[1]
                    y_ = imageToPredict.shape[0]
                    x_ = imageToPredict.shape[1]
                    #reseizing the image
                    targetSize = 224
                    x_scale = targetSize / x_
                    y_scale = targetSize / y_
                    print(x_scale, y_scale)
                    img = cv2.resize(imageToPredict, (targetSize, targetSize));
                    print(img.shape)
                    #img = np.array(img);
        
                    folder = '/content/Tensorflow_object_detector/workspace/training_OD/images/reseizedImages'
                    if not os.path.exists(folder):
                        os.makedirs(folder)
                    output_file_name = os.path.join(folder, name)
                    #output.save(output_file_name, "JPEG", quality = 95)
                    cv2.imwrite(output_file_name,img)
                    #img.save(output_file_name) with pil
                    print("Reseized one image done")
                    # original frame as named values
                    (origLeft, origTop, origRight, origBottom) = (float(row[4]), float(row[5]), float(row[6]), float(row[7]))
                    #reseizing the bbox
                    xmin = int(np.round(origLeft * x_scale))
                    ymin = int(np.round(origTop * y_scale))
                    xmax = int(np.round(origRight * x_scale))
                    ymax = int(np.round(origBottom * y_scale))
                    
                    width, height, xmin, ymin, xmax, ymax = float(row[1]), float(row[2]), float(row[4]), float(row[5]), float(row[6]), float(row[7])
                    
      
                    org_height, org_width = img.shape[:2]
                    #checking for mismatches between image dimensions and reseized bbox coordinates 
                    if org_width != width:
                          error = True
                          print('Width mismatch for image: ', name, width, '!=', org_width)
                          width = org_width
                    if org_height != height:
                          error = True
                          print('Height mismatch for image: ', name, height, '!=', org_height)
                          height = org_height
       
                    if xmin > org_width:
                          error = True
                          print('XMIN=' , xmin, '>' , org_width, 'for filename', name)
                          xmin = org_width

                    if xmax > org_width:
                          error = True
                          print('XMAX=', xmax, '>', org_width, 'for filename', name)
                          xmax = org_width
       
                    if ymin > org_height:
                          error = True
                          print('YMIN=', ymin, '>', org_height, 'for filename', name)
                          ymin = org_height
       
                    if ymax > org_height:
                          error = True
                          print('YMAX=', ymax, '>', org_height, 'for filename', name)
                          ymax = org_height
                   if error == True:
                          print('Error for file: %s' % name)
                          print()
       
                    print('Checked %d files and realized %d errors' % (cnt, error_cnt))
                    changes = {row[0]:name , row[1]:width , row[2]: height, row[3]:label, row[4]: xmin , row[5]: ymin , row[6]: xmax , row[7]: ymax }
                    #replacing the row with appropriate bbox and save it in new_row
                    for key ,value in changes.items():
                         new_row = [x.replace(key,str(value)) for x  in new_row ]
                    new_rows.append(new_row)
                    #(row[4],row[5],row[6],row[7]) = (x, y , xmax , ymax)
                    # Box.drawBox([[1, 0, x, y, xmax, ymax]], img)
                    drawBox([[1, 0, xmin, ymin, xmax, ymax]], img)
                print("Done All")
        #write the filenames with their new reseized box in a new csv file : dataset_out
        OUT = '/content/Tensorflow_object_detector/workspace/training_OD/annotations/dataset_out.csv'
        with open(OUT , 'w') as f:
            writer = csv.writer(f)
            writer.writerows(new_rows)
    


cvTest()