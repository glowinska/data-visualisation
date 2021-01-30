# -*- coding: utf-8 -*-
"""
Create a jupyter notebook running locally on your computer (you can not use Google Colab as it will not have access to the faculty VPN).
"""

# done

"""In the Jupyter Noteebok just grab a single measurement (You can use requests module.) Display the measurement in JSON format.

"""

import requests
r = requests.get('http://tesla.iem.pw.edu.pl:9080/v2/monitor/2')
r.status_code
r.json()

"""In Jupter Notebook run a script (with a small sleep command) and grab a series of measurements and keep them in a Python list for a period of time equal 5 minutes.

"""

import json
from time import time,sleep

def get_request(url, monitor):
    end = time() + 60*5
    while time() < end:
        sleep(1)
        r = requests.get(url)
        monitor.append(r.json())
    return monitor
    
monitor1, monitor2, monitor3, monitor4, monitor5, monitor6 = [], [], [], [], [], []

monitor2 = get_request('http://tesla.iem.pw.edu.pl:9080/v2/monitor/2', monitor2)

"""Convert the measurements from Python list to a Pandas DataFrame with usage of json.loads() function, which converts a string representation of JSON to a Python dictionary. Assign valid names to columns and row index.

"""

import json
import datetime
import pandas as pd

def get_values(monitor):
    data = json.loads(json.dumps(monitor))
    df_time = pd.json_normalize(pd.DataFrame(monitor)['trace'])
    df_values = pd.json_normalize(data, record_path=[['trace', 'sensors']])
    L0, L1, L2, R0, R1, R2, time, anomaly = [], [], [], [], [], [], [], []
    lov = [L0, L1, L2, R0, R1, R2]
    for x in range(len(df_time.index)):
        i = x * 6
        for j in range(6):
            lov[j].append(df_values['value'][i+j])
        date_time_obj = datetime.datetime.strptime(str(df_time['id'][x]), '%H%M%S%d%m%Y')
        time.append(date_time_obj)
        anomaly.append(df_values['anomaly'][i])
    dict2 = {'L0': L0, 'L1': L1,'L2': L2, 'R0': R0,'R1': R1, 'R2': R2, 'time': time, 'anomaly' : anomaly}  
    df_finito = pd.DataFrame(dict2) 
    df_finito.drop_duplicates(keep=False,inplace=True) 
    return df_finito

mydfm2 = get_values(monitor2)
mydfm2

"""Plot using matplotlib/seaborn or plotly, in a single figure, six traces namely 3 for all two feet.

"""

import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go

def create_fig(mydf):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=mydf['time'], y=mydf['L0'], mode="markers", name="L0",))
    fig.add_trace(go.Scatter(x=mydf['time'], y=mydf['L1'], mode="markers", name="L1",))
    fig.add_trace(go.Scatter(x=mydf['time'], y=mydf['L2'], mode="markers", name="L2",))
    fig.add_trace(go.Scatter(x=mydf['time'], y=mydf['R0'], mode="markers", name="R0",))
    fig.add_trace(go.Scatter(x=mydf['time'], y=mydf['R1'], mode="markers", name="R1",))
    fig.add_trace(go.Scatter(x=mydf['time'], y=mydf['R2'], mode="markers", name="R2",))
    # fig.add_trace(go.Scatter(x=mydf['time'].loc[mydf['anomaly'] != True],y=mydf['L0'],mode="markers",name="R0",))
    # fig.add_trace(go.Scatter(x=mydf['time'].loc[mydf['anomaly'] == True],y=mydf['L0'],mode="markers",name="L0",))
    fig.update_layout(title="Figure", xaxis_title="Time", yaxis_title="Value")
    fig.show()

create_fig(mydfm2)

"""Repeat the measurements for all cases and plot the results on the Jupter Notebook for all patients.

"""

monitor1 = get_request('http://tesla.iem.pw.edu.pl:9080/v2/monitor/1', monitor1)
monitor3 = get_request('http://tesla.iem.pw.edu.pl:9080/v2/monitor/3', monitor3)
monitor4 = get_request('http://tesla.iem.pw.edu.pl:9080/v2/monitor/4', monitor4)
monitor5 = get_request('http://tesla.iem.pw.edu.pl:9080/v2/monitor/5', monitor5)
monitor6 = get_request('http://tesla.iem.pw.edu.pl:9080/v2/monitor/6', monitor6)

mydfm1 = get_values(monitor1)
mydfm3 = get_values(monitor3)
mydfm4 = get_values(monitor4)
mydfm5 = get_values(monitor5)
mydfm6 = get_values(monitor6)

create_fig(mydfm1)
create_fig(mydfm3)
create_fig(mydfm4)
create_fig(mydfm5)
create_fig(mydfm6)

"""Highlight parts of the trace where you will notice the 'anomaly', which is a parameter of single measurements.

"""

def show_anomalies(mydf, param1):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=mydf['time'].loc[mydf['anomaly'] != True], y=mydf[param1], mode="markers", name="non-anomaly",))
    fig.add_trace(go.Scatter(x=mydf['time'].loc[mydf['anomaly'] == True], y=mydf[param1], mode="markers", name="anomaly",))
    fig.update_layout(title="Anomalies", xaxis_title="Time", yaxis_title="Value")
    fig.show()

create_fig(mydfm2, 'L0')

"""Answer the question: 'How often the results change?'

"""

# Values has the date with precision to one second, however sometimes you can get two measurements per one second, so it's a time smaller or equal 1 second.

"""Can you observe any patterns? How long are the patterns."""

# Patterns usually can be seen before an anomaly, values during anomaly looks similar to the few seconds before anomaly.