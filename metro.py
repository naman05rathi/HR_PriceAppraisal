import urllib
import sys
import csv
import requests

url ="https://maps.googleapis.com/maps/api/geocode/json?key=-k&address="	#add API key here
in1=open('MetroS.csv','rb')
count=0
reader = csv.reader(in1)
with open('MetroLL.csv', 'wb') as out:
	filewriter = csv.writer(out, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
	for row in reader:
		url1=requests.get(url+row[0]+"+Metro+Station")
		response = url1.json()
		try:
			filewriter.writerow((row[0],response['results'][0]['geometry']['location']['lat'],response['results'][0]['geometry']['location']['lng']))
		except:
			filewriter.writerow([row[0]])