from websocket import create_connection
import json

ws = create_connection("wss://stream.binance.com:9443/ws/Bitcoin")

ws.send('{"method": "SUBSCRIBE","params": ["btcusdt@kline_1s"],"id": 1}')

response = ws.recv()
data = json.loads(response)

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
    
    values.append(open_time)
    values.append(close_time)
    values.append(float(open_price))
    values.append(float(close_price))
    values.append(float(high))
    values.append(float(low))
    print(values)

       
   
