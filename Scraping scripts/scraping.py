import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import requests
import csv
from bs4 import BeautifulSoup
 
with open('data.csv', 'wb') as csvfile:
	filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
	filewriter.writerow(['Name', 'Address','Rate per sq ft','Price',' Area','Years',' Bathrooms','Floor'])
	url = ""	#Enter URL here
	for counter in range(2,100):
		url2 = url + str(counter)
		r =requests.get(url2)
		soup = BeautifulSoup(r.content,"lxml")

		g_data = soup.find_all("div",{"class" : "infoWrap"})
		for item in g_data:
			try: 
				a = item.contents[0].contents[0].text
			except:
				a = NaN
			try:		
				b = item.contents[0].contents[1].text.replace(',','')
			except:
				b = NaN
			try:		
				x = item.contents[1].contents[1].contents[0].contents[0].contents[1].text.encode('utf-8')
			except:	
				x = NaN
			try:	
				y = item.contents[1].contents[1].contents[0].contents[0].contents[2].text.encode('utf-8')
			except:
				y = NaN	
			pr = x+' '+y
			try:
				c = item.contents[1].contents[2].contents[0].text
			except:
				c = NaN
			try:	
				d = item.contents[2].contents[0].contents[0].text
			except:
				d = NaN	
			try:
				e = item.contents[2].contents[1].text
			except:
				e = NaN
			try:
				f = item.contents[2].contents[2].text
			except:
				f = NaN 
			try:		
				g = item.contents[1].contents[1].contents[1].text.encode('utf-8')
			except:
				g = NaN	
			filewriter.writerow((a,b,g,pr,c,d,e,f))
