#Libraries

from __future__ import division
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style
import urllib 
import csv
import os
import time
import sys
import csv2json

os.system('clear')
def update_progress(progress):
    barLength = 100 # Modify this to change the length of the progress bar
    status = " "
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
        status = "error: progress var must be float\r\n"
    if progress < 0:
        progress = 0
        status = "Halt...\r\n"
    if progress >= 1:
        progress = 1
        status = "Done...\r\n"
    block = int(barLength*progress)
    text = (Fore.YELLOW + Back.BLUE + Style.BRIGHT + "\rPercent: [{0}] {1:.2f}% ".format( "="*block + " "*(barLength-block), progress*100))
    sys.stdout.write(text)
    sys.stdout.flush()

print (Fore.YELLOW + Back.BLUE + "\t\t    |---------------------------------------------------------------------------|    ")
print ("\t\t    |---------------------  S C R A P E   T U B E v2  --------------------------|    ")
print ("\t\t    |---------------------------------------------------------------------------|    \n")

#Receive search input from user
var = raw_input(Fore.RESET + Back.RESET + "\t   |Enter search string: " + Fore.GREEN)
pages = raw_input(Fore.RESET + "\t   |Enter number of pages to search: " + Fore.GREEN)
filename = raw_input(Fore.RESET + "\t   |Enter name of file to save data: " + Fore.GREEN)
print

#create list of URLS to be scraped like a muthafucka
urls = []
for x in range(1, int(pages)+1):
  y = str(x)
  searchurl = "http://www.youtube.com/results?search_sort=video_view_vount&filters=video&search_query="+ var + "&page=" + y
  urls.append(searchurl)

#create names for CSV/JSON files
csvfile = filename + '.csv'
jsonfile = filename + '.json'

#lists for URLS/Titles to be put into HoodRoulette
urllist= []
titles = []

#Necessary because Niggas put weird Unicode symbols at the beginning of Video Titles
def normalize(s):
    if type(s) == unicode: 
        return s.encode('utf8', 'ignore')
    else:
        return str(s)

#Function for pulling info from URLs
i = 0
while i<len(urls):
  url = urllib.urlopen(urls[i])
  content = url.read()
  soup = BeautifulSoup(content)
  links = soup.select('h3 > a')

  for a in links:
    temptitle = a.get('title')
    title = normalize(temptitle)
    temphrefs = a.get('href')
    hrefs = normalize(temphrefs)
    if hrefs[9] == "-":
      newrefs = "-" + hrefs[10:]
      titles.append((title,newrefs))
    else:
      titles.append([title,hrefs[9:]])
  #  urllist.append(hrefs[9:])
  i+=1
  print (update_progress(float(i/int(pages)))),

print('\n' + Fore.RESET + Back.RESET + Style.RESET_ALL + "\t   Append to master csv? [y or n]\n\t   " + Fore.GREEN)

masterAppend = raw_input('\t   ')
print Fore.RESET

if masterAppend.lower() == "y":
  if os.path.isfile('hood_roulette_master.csv'):
    with open('hood_roulette_master.csv', 'a+') as masterfile:
      appender = csv.writer(masterfile, dialect = 'excel', lineterminator='\n')
      for val in titles:
        appender.writerow(val)
    masterfile.close()
  else:
    print Fore.RED + 'Master file not found.'

#Function for writing information to CSVfile
with open(csvfile, "w+") as csvfile:
    writer = csv.writer(csvfile, lineterminator='\n')
    writer.writerow(['title','youtubeId'])
    for val in titles:
        writer.writerow(val)
csvfile.close()

#Function from csv2json.py for turning csv directly into a json file
csv2json.convert(csvfile)

time.sleep(1)
raw_input(Fore.YELLOW + Back.BLUE + "\n\t   VICTORY!!!!! -_-   \n")
