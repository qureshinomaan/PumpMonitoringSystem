import csv 
from datetime import datetime 
from basics import data, db

with open('data.csv') as file:
	readCSV = csv.reader(file , delimiter=',')
	for i in readCSV:
		efficiency = 0
		if float(i[6]) >0.5:
			efficiency = (float(i[3])*20*60)/(367*float(i[6]))
		data1 = data(temperature = i[1], humidity = i[2], flow = i[3], voltage = i[4], current = i[5],
		power=i[6], efficiency = efficiency, 
		Time = datetime.strptime(i[0],'%Y-%m-%d %H:%M:%S'))
		db.session.add(data1)
