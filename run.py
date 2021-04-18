#!/usr/bin/env python3
import os
import requests
import json

#initialize url where content will be uploaded to
url = "http://35.222.40.70/fruits/"
#set path where files are saved
dir = "supplier-data/descriptions/"
#list all files
list_files = os.listdir(dir)
#iterate through files
for files in list_files:
  if files.endswith(".txt"):
    #open all files
    with open(dir + files) as text_file:
      #read file contents and split text wit a new line
      contents = text_file.read().split("\n")
      #set up the dictionary to be used as a json format later,
      #the dictionary format is: {"name":"fruit name",
      #"weight": weight in lbs,
      #"description": "description about the fruit",
      #"image_name": image name associated with fruit with ext .jpeg"}
      format = {
                  "name": contents[0],
                  "weight": int(contents[1].strip("lbs")),
              "description": contents[2],
              "image_name": os.path.splitext(files)[0] + ".jpeg"}
  #upload content to website
      response = requests.post(url, data = format)
  #print the upload's status code
      print("Status code:{}".format(response.status_code))
