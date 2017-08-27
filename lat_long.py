import urllib
import sys
import csv
import requests
import requests

out=open('Location.csv','wb')	
with open('Unique_add.csv', 'rb') as in1:
	reader = csv.reader(in1)
	writer = csv.writer(out)
	for row in reader:
		print row[0]
		url="https://maps.googleapis.com/maps/api/geocode/json?address="	#add API key here
	 	url1=url+row[0]
	 	response = requests.get(url1)
        location = response.json()
        writer.writerow((row[0],response['results'][0]['geometry']['location']['lng'],response['results'][0]['geometry']['location']['lat']))
        print (response['results'][0]['geometry']['location'])




