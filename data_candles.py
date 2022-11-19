from websocket import create_connection
import json
from time import sleep
from csv import DictWriter,writer

ws = create_connection("wss://stream.binance.com:9443/ws/Bitcoin")

ws.send('{"method": "SUBSCRIBE","params": ["btcusdt@kline_1s"],"id": 1}')

response = ws.recv()
data = json.loads(response)

fieldNames = ['Time','Open','Close','High','Low']

with open('candle.csv', 'w', encoding='UTF8', newline='') as f:
    writer = writer(f)

    # write the header
    writer.writerow(fieldNames)
    f.close()

while True:
    
    values = []

    response = ws.recv()
    data = json.loads(response)

    kline = data["k"]
    open_time = kline["t"]
    close_time = kline["T"]
    open_price = kline["o"]
    close_price = kline["c"]
    high = kline["h"]
    low = kline["l"]

    time = (open_time + close_time) /2

    dict = {'Time':time, 'Open' : open_price, 'Close' : close_price ,'High' : high ,'Low' : low}
    with open('candle.csv','a') as f_object:
 
        dictwriter_object = DictWriter(f_object, fieldnames=fieldNames)

        dictwriter_object.writerow(dict)

        f_object.close()
    
    sleep(1)