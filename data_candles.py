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

greenCount = 0
redCount = 0

def getData(greenCount, redCount):

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
    
    difference = float(close_price) - float(open_price)
    print(difference)
    if difference > 0:
        greenCount += 1
        redCount = 0
        print("green",greenCount)
        if greenCount == 3:
            greenCount = 0
            with open('memeCodes.txt', 'w') as f:
                f.write('3Green\n')
        elif difference > 2:
            with open('memeCodes.txt', 'w') as f:
                f.write('bigGreen\n')
        else:
            with open('memeCodes.txt', 'w') as f:
                f.write('blank\n')
    
    elif difference < 0:
        redCount += 1
        greenCount = 0
        print("red",redCount)
        if redCount == 3:
            redCount = 0
            with open('memeCodes.txt', 'w') as f:
                f.write('3Red\n')   
        elif difference < -2:
            with open('memeCodes.txt', 'w') as f:
                f.write('bigRed\n')
        else:
            with open('memeCodes.txt', 'w') as f:
                f.write('blank\n')
    
    elif difference == 0:
        with open('memeCodes.txt', 'w') as f:
                f.write('crazyMeme\n')


    return time, open_price, close_price, high, low, greenCount, redCount

def csvApp(time, open_price, close_price, high, low):
    dict = {'Time':time, 'Open' : open_price, 'Close' : close_price ,'High' : high ,'Low' : low}
    with open('candle.csv','a') as f_object:
 
        dictwriter_object = DictWriter(f_object, fieldnames=fieldNames)

        dictwriter_object.writerow(dict)

        f_object.close()

for i in range(30):
    time, open_price, close_price, high, low, greenCount, redCount= getData(greenCount, redCount)
    csvApp(time, open_price, close_price, high, low)

def csvPop():
    data = pd.read_csv('candle.csv')
    print(data)
    #minTime = data[data.Time == min(data.Time)]
    data = data[data.index != 0]
    print(data)
    data.to_csv('candle.csv', index = False)

while True:

    time, open_price, close_price, high, low = getData(greenCount, redCount)
    csvApp(time, open_price, close_price, high, low)
    csvPop()

    

    

    
    
    sleep(1)