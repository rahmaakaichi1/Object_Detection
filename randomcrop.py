import random 
TRAIN ="/content/Tensorflow_object_detector/workspace/training_OD/images/reseizedImages"
for file_name in os.listdir(TRAIN):
  print("Processing %s" % file_name)
  im = Image.open(os.path.join(TRAIN, file_name))
  size = im.size
  print(size)
  w = size[0]
  h = size[1]
  l = random.randint(0,w)
  u = random.randint(0, h)
  print(l,u)
  new_size = (l , u, w + l , h + u)
  print(new_size)
  
  
  region = im.crop(new_size)
      #save crops in a specific folder 
  output_dir = "/content/Tensorflow_object_detector/workspace/training_OD/images/crops"
  output_file_name = os.path.join(output_dir, "cropped_" + file_name)
  region.save(output_file_name)