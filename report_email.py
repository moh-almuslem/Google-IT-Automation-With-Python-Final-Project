#!/usr/bin/env python3
import os
import reports
import datetime
import emails

def contents(dir):
  dir = "supplier-data/descriptions/"
  list_files = os.listdir(dir)
  paragraph =""
  for files in list_files:
    if files.endswith(".txt"):
      with open(dir + files) as text_file:
        contents = text_file.read().split("\n")
        format = {
                    "name": contents[0].strip(),
                    "weight": contents[1].strip()}
        paragraph+= "name: " + format["name"] + "<br/" + "weight: " + format["weight"] + "<br/><br/>"
  return paragraph

if __name__ == "__main__":
  dir = "supplier-data/descriptions/"
  #generate title with today's date
  title ="Processed Update on {}".format(datetime.date.today())
  #generate report
  paragraph = contents(dir)
  reports.generate("/tmp/processed.pdf", title, paragraph)
  #generate and send email emails.generate(From, To, Subject line, E-mail Body, Attachment)
  gen_email = emails.generate("automation@example.com", "student-04-63373d24b8be@example.com", "Upload Completed- Online Fruit Store", "All fruits are uploaded to our website successfully. A detailed list is attached to this email.", "/tmp/processed.pdf")
  emails.send(gen_email)
