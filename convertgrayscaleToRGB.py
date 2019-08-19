
#folder containg the images 
RESEIZE ='/content/Tensorflow_object_detector/workspace/training_OD/images/jpg'
for file_name in os.listdir(RESEIZE):
  print("Processing %s" % file_name)
  
  image = Image.open(os.path.join(RESEIZE, file_name))
  image.show()
  rgb_image = image.convert('RGB')
  rgb_image.show()
  print(rgb_image.mode)

  dir = '/content/Tensorflow_object_detector/workspace/training_OD/images/RGBImages'
  if not os.path.exists(dir):
       os.makedirs(dir)
  #output_file_name = os.path.join(dir, "rgb_" + file_name)
  output_file_name = os.path.join(dir,file_name)
  rgb_image.save(output_file_name)
print("All done")