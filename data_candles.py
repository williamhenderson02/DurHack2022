from websocket import create_connection
import json
from time import sleep
from csv import DictWriter,writer,reader
import pandas as pd

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

def getData():

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
    '''
    difference = float(close_price) - float(open_price)
    if difference > 0:
        greenCount += 1
        redCount = 0
        if greenCount == 3:
            greencount = 0
            'run meme'
        elif difference > 2:
            'run meme'
        else:
            'blank meme'
    
    elif difference < 0:
        redCount += 1
        greenCount = 0
        if redCount == 3:
            redcount = 0
            'run meme'   
        elif difference < -2:
            'run meme'
        else:
            'blank meme'
    
    elif difference == 0:
        'run meme'

     '''

    return time, open_price, close_price, high, low

def csvApp(time, open_price, close_price, high, low):
    dict = {'Time':time, 'Open' : open_price, 'Close' : close_price ,'High' : high ,'Low' : low}
    with open('candle.csv','a') as f_object:
 
        dictwriter_object = DictWriter(f_object, fieldnames=fieldNames)

        dictwriter_object.writerow(dict)

        f_object.close()

for i in range(30):
    time, open_price, close_price, high, low = getData()
    csvApp(time, open_price, close_price, high, low)

def csvPop():
    data = pd.read_csv('candle.csv')
    print(data)
    #minTime = data[data.Time == min(data.Time)]
    data = data[data.index != 0]
    print(data)
    data.to_csv('candle.csv', index = False)

while True:

    time, open_price, close_price, high, low = getData()
    csvApp(time, open_price, close_price, high, low)
    csvPop()

    

    

    
    
    sleep(1)