from websocket import create_connection
import json
from time import sleep
from csv import DictWriter,writer
import pandas as pd

ws = create_connection("wss://stream.binance.com:9443/ws/Bitcoin")

ws.send('{"method": "SUBSCRIBE","params": ["btcusdt@trade"],"id": 1}')

response = ws.recv()
data = json.loads(response)
fieldNames = ['Time','Price']

with open('scatter.csv', 'w', encoding='UTF8', newline='') as f:
    writer = writer(f)

    # write the header
    writer.writerow(fieldNames)
    f.close()

def getData():
    response = ws.recv()
    data = json.loads(response)
    
    time = data["T"]
    price = float(data["p"])

    return time,price

def csvApp(time,price):
    dict = {'Time':time, 'Price' : price}
    with open('scatter.csv','a') as f_object:
 
        dictwriter_object = DictWriter(f_object, fieldnames=fieldNames)

        dictwriter_object.writerow(dict)

        f_object.close()

def csvPop():
    data = pd.read_csv('scatter.csv')
    data = data[data.index != 0]
    data.to_csv('scatter.csv', index = False)

for i in range(30):
    time, price = getData()
    csvApp(time, price)

while True:

    time, price = getData()
    csvApp(time, price)
    csvPop()
    
    sleep(1)