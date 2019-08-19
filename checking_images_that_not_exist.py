#test if filenames of dataset_out exists in reseized folder
FOLDER = '/content/Tensorflow_object_detector/workspace/training_OD/images/RGBImages'
CSV_FILE = '/content/Tensorflow_object_detector/workspace/training_OD/annotations/dataset_out.csv'
with open(CSV_FILE, 'r') as fid:
   
                 print('Checking file:', CSV_FILE, 'in folder:', FOLDER)
   
                 file = csv.reader(fid, delimiter=',')
                 for row in file:
                    name = row[0]
                    file_name = os.path.join(FOLDER, name)
                    if os.path.isfile(file_name) == False:
                      print('image', file_name , 'doesnt exist!')