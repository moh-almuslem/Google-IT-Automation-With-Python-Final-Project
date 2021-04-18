#!/usr/bin/env python3
from PIL import Image
import os
#set the main path
path_main = "supplier-data/images/"
#set the new path the images will be saved at
new_path = "supplier-data/images/"
#list all files in directrory
for file in os.listdir(path_main):
  if file.endswith('.tiff'):
    #removes file extention
    file_name = os.path.splitext(file)[0]
    #open images
    im = Image.open(path_main + file).convert("RGB").resize((600,400))
    #save the converted files into the new path as jpeg
    im.save(new_path + file_name+ ".jpeg", "jpeg")
