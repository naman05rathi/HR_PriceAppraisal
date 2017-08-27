import csv
from geopy.distance import great_circle
in1 = open('Last.csv','rb')
reader1 = csv.reader(in1)
#reader2 = csv.reader(in2)
with open('Air_Dis.csv','wb') as out1:
	filewriter = csv.writer(out1, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
	for row1 in reader1:
		source=(float(row1[1]),float(row1[2]))
		destination = (28.554089,77.084723)
		p = great_circle(source,destination).miles
		filewriter.writerow((row1[0],p))	