import requests
import json
import random
from onem2m import *
from datetime import datetime
from datetime import timedelta

def get_data_grp(group_name):
    headers = {
    'X-M2M-Origin': 'admin:admin',
    'Content-type': 'application/json'
    }

    group_uri = group_name
    print(group_uri)
    response = requests.get(group_uri, headers=headers)
    # print('Return code : {}'.format(response.status-code))
    # print('Return Content : {}'.format(response.text))
    _resp = json.loads(response.text)
    print("Get " + group_name)
    return _resp['m2m:cin']['ct'], _resp['m2m:cin']['con'];
    # # spliced-string = output-string.split()
    # # for con in spliced-string:
    #     # if spliced-string.index(con) == 2:
    #         # data.append(con)
    #     # if spliced-string.index(con) == 7:
    #         # meow.append(con)

    # # data.append(loli)
    # # print(oe_temp)
    # # print("==========================")
    # return response.status_code, _resp

def convert_to_time(ctime):
	date = ctime[0:8]
	time = ctime[9:15]
	datetime_object = datetime.strptime(ctime, '%Y%m%dT%H%M%S')
	return datetime_object + timedelta(hours=5,minutes=30)

def final_data():
    time = convert_to_time(get_data_grp("https://onem2m.iiit.ac.in:443/~/in-cse/in-name/Team9_Pumps_performance_monitoring/pr_4_esp32_1/oe/oe_1_temperature/la")[0])
    temperature = get_data_grp("https://onem2m.iiit.ac.in:443/~/in-cse/in-name/Team9_Pumps_performance_monitoring/pr_4_esp32_1/oe/oe_1_temperature/la")[1]
    humidity = get_data_grp("https://onem2m.iiit.ac.in:443/~/in-cse/in-name/Team9_Pumps_performance_monitoring/pr_4_esp32_1/oe/oe_1_rh/la")[1]
    flow = get_data_grp("https://onem2m.iiit.ac.in:443/~/in-cse/in-name/Team9_Pumps_performance_monitoring/pr_4_esp32_1/fm/fm_1_pump_flowrate/la")[1]
    power = get_data_grp("https://onem2m.iiit.ac.in:443/~/in-cse/in-name/Team9_Pumps_performance_monitoring/pr_4_esp32_1/em/em_1_watts_total/la")[1]
    current = get_data_grp("https://onem2m.iiit.ac.in:443/~/in-cse/in-name/Team9_Pumps_performance_monitoring/pr_4_esp32_1/em/em_1_current_total/la")[1]
    voltage = get_data_grp("https://onem2m.iiit.ac.in:443/~/in-cse/in-name/Team9_Pumps_performance_monitoring/pr_4_esp32_1/em/em_1_vll_avg/la")[1]
    return [time, temperature, humidity, flow, voltage, current, power]