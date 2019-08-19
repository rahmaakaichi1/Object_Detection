
directory ="/content/Tensorflow_object_detector/workspace/training_OD/images/jpg"

for file_name in os.listdir(directory):
  print("Processing %s" % file_name)
  image = Image.open(os.path.join(directory, file_name))

  
  new_dimensions = (224, 224)
  output = image.resize(new_dimensions, Image.ANTIALIAS)
  folder = '/content/Tensorflow_object_detector/workspace/training_OD/images/reseizedImages'
  if not os.path.exists(folder):
    os.makedirs(folder)
  output_file_name = os.path.join(folder, file_name)
  #output.save(output_file_name, "JPEG", quality = 95)
  output.save(output_file_name)

print("All done")

