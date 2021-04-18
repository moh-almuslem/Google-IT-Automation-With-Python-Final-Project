#!/usr/bin/env python3
import requests
import os
#initialize the url we want to upload the files to
url = "http://localhost/upload/"
#set the path of saved files
dir = "supplier-data/images/"
#list all files
list_files = os.listdir(dir)
#iterate through files
for files in list_files:
  if files.endswith('.jpeg'):
  #open all files
    with open(dir + files, 'rb') as opened:
      #upload the files using the requests module
      response = requests.post(url, files={'file':opened})
      #print the upload's status code
      print("Status code:{}".format(response.status_code))
