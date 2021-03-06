from datetime import datetime
import calendar
import requests
import threading
import json
import time
import random
from flask import flash, redirect, url_for
from flask import render_template
from basics import app
from basics import db, data
from basics.latdat import final_data



def findDay(date): 
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday() 
    return (calendar.day_name[born]) 


def get_data(uri, format="json"):
    """
        Method description:
        Gets data from the specified container(data_CIN)
        in the OneM2M framework/tree

        Parameters:
        uri : [str] URI for the parent DATA CON appended by "la" or "ol"
        fmt_ex : [str] payload format (json/XML)
    """
    headers = {
        'X-M2M-Origin': 'admin:admin',
        'Content-type': 'application/json'}

    response = requests.get(uri, headers=headers)
    # print('Return code : {}'.format(response.status_code))
    # print('Return Content : {}'.format(response.text))
    _resp = json.loads(response.text)
    return response.status_code, _resp["m2m:cin"]["con"]


def pushData():
	#threading.Timer(300,pushData).start()
	print("Push Data Started")
	i = final_data()
	if i[5] == '':
		i[5] = 0
	if i[6] == '':
		i[6] = 0
	if i[4] == '':
		i[4] = 0
	efficiency = 0
	if float(i[6]) >0.5:
			efficiency = (float(i[3])*20*60)/(367*float(i[6]))
	data1 = data(temperature = i[1], humidity = i[2], flow = i[3], voltage = i[4], 
		current = i[5], power=i[6], efficiency = efficiency, 
		Time = i[0])
	print(i[0])
	db.session.add(data1)
	db.session.commit()
	print("commited")


#routes are what we type into browser to get from one webpage to another 
@app.route("/")
def home():
	#pushData()
	print("Bello World")
	count = 0
	data1 = data.query.all()
	for j in data1:
		count+=1
	temper   = [data1[i].temperature for i in range(count)]
	humidity = [data1[i].humidity for i in range(count)]
	power    = [data1[i].power for i in range(count)]
	current	 = [data1[i].current for i in range(count)]
	efficiency = [data1[i].efficiency for i in range(count)]
	flow     = [data1[i].flow for i in range(count)] 
	time   	 = [str(data1[i].Time.year)+'-'+str(data1[i].Time.month)+'-'+
				str(data1[i].Time.day) + ' ' + str(data1[i].Time.hour) + ':' + 
				str(data1[i].Time.minute) + ':' + str(data1[i].Time.second)
				for i in range(count)]
	print(data1[count-1].Time.minute)
	# days	 = [str(data[i].weekday()) for i in range(count)]
	weekday = []
	for i in range(count):
		sample = datetime(data1[i].Time.year, data1[i].Time.month, data1[i].Time.day,
			data1[i].Time.hour,data1[i].Time.minute, data1[i].Time.second, 1)
		weekday.append(sample.weekday())
	return render_template('home.html', time = time, temper= temper, humidity= humidity, 
		power=power, current= current, efficiency= efficiency, flow=flow, weekday=weekday)



@app.route("/contact")
def contact():
	 return render_template('contact.html', title='Contact')













