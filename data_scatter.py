from websocket import create_connection
import json

ws = create_connection("wss://stream.binance.com:9443/ws/Bitcoin")

ws.send('{"method": "SUBSCRIBE","params": ["btcusdt@trade"],"id": 1}')

while True:

    values = []

    response = ws.recv()
    data = json.loads(response)
    try:
        time = data["T"]
        price = data["p"]
        values.append(time)
        values.append(float(price))
        print(values)

    except:
        print("no p")