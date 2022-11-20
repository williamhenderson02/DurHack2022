from websocket import create_connection
import json
from time import sleep
from csv import DictWriter,writer,reader
import pandas as pd
import requests
import urllib

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
    #print(difference)
   
    if difference > 0:
        greenCount += 1
        redCount = 0
        #print("green",greenCount)
        if greenCount == 3:
            greenCount = 0
            image_url = "http://29.media.tumblr.com/tumblr_lltzgnHi5F1qzib3wo1_400.jpg"
            urllib.request.urlretrieve(image_url, "meme.png")
            
        elif difference > 0.4:
            image_url = "https://i.kym-cdn.com/entries/icons/mobile/000/029/959/Screen_Shot_2019-06-05_at_1.26.32_PM.jpg"
            urllib.request.urlretrieve(image_url, "meme.png")
        '''else:
            image_url = "https://memes.co.in/memes/update/uploads/2021/12/InShot_20211209_222013681.jpg"
            urllib.request.urlretrieve(image_url, "meme.png")'''
    
    elif difference < 0:
        redCount += 1
        greenCount = 0
        #print("red",redCount)
        if redCount == 3:
            redCount = 0
            image_url = "https://i.imgur.com/i9JNNvJ.jpg"
            urllib.request.urlretrieve(image_url, "meme.png")
        elif difference < -0.4:
            image_url = "http://images7.memedroid.com/images/UPLOADED333/5fe0de2ad6e08.jpeg"
            urllib.request.urlretrieve(image_url, "meme.png")
        '''else:
            image_url = "https://memes.co.in/memes/update/uploads/2021/12/InShot_20211209_222013681.jpg"
            urllib.request.urlretrieve(image_url, "meme.png")'''
    
    else:
        image_url = "https://memes.co.in/memes/update/uploads/2021/12/InShot_20211209_222013681.jpg"
        urllib.request.urlretrieve(image_url, "meme.png")

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
    data = data[data.index != 0]
    data.to_csv('candle.csv', index = False)

while True:

    time, open_price, close_price, high, low, greenCount, redCount = getData(greenCount, redCount)
    csvApp(time, open_price, close_price, high, low)
    csvPop()
    
    sleep(1)