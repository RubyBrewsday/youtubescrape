import csv
import sys
import json

#EDIT THIS LIST WITH YOUR REQUIRED JSON KEY NAMES
fieldnames=["title", "youTubeId"]

def __unicode__(self):
  return self.name

def convert(filename):
  csv_filename = str(filename.name)
  print "Opening CSV file: ",csv_filename 
  f=open(csv_filename, 'r+')
  csv_reader = csv.DictReader(f,fieldnames)
  json_filename = csv_filename.split(".")[0]+".json"
  print "Saving JSON to file: ",json_filename
  jsonf = open(json_filename,'w+') 
  data = json.dumps([r for r in csv_reader])
  jsonf.write(data) 
  f.close()
  jsonf.close()
 
if __name__ == "__main__":
  convert(sys.argv[1:])

#Original basis for this code: http://jaranto.blogspot.com/2012/12/transform-csv-file-to-json-file-with.html
