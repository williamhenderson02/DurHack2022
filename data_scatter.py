from websocket import create_connection
import json
from time import sleep
from csv import DictWriter,writer

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

while True:

    values = []

    response = ws.recv()
    data = json.loads(response)
    
   
    time = data["T"]
    price = float(data["p"])
    
    dict = {'Time':time, 'Price':price}
    with open('scatter.csv','a') as f_object:
 
        dictwriter_object = DictWriter(f_object, fieldnames=fieldNames)

        dictwriter_object.writerow(dict)

        f_object.close()
    
    sleep(1)