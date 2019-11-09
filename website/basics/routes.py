import requests
import threading
import json
import time
import random
from flask import flash, redirect, url_for
from flask import render_template
from basics import app
from basics import db, data

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
	threading.Timer(5,pushData).start()
	t = get_data("http://139.59.42.21:8080/~/in-cse/in-name/Team9_Pumps_performance_monitoring/pr_4_esp32_1/oe/oe_1_temperature/la")[1]
	print(float(t))
	data1 = data(temperature = t, humidity = 25, flow = 7, power = 56, current = 21, efficiency = 1);
	db.session.add(data1)
	db.session.commit()
	print("commited")



#routes are what we type into browser to get from one webpage to another 
@app.route("/")
def home():
	# pushData()
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
	return render_template('home.html', time = time, temper= temper, humidity= humidity, 
		power=power, current= current, efficiency= efficiency, flow=flow)



@app.route("/contact")
def contact():
	 return render_template('contact.html', title='Contact')













