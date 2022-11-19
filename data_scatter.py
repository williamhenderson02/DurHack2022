from websocket import create_connection
import json

ws = create_connection("wss://stream.binance.com:9443/ws/Bitcoin")

ws.send('{"method": "SUBSCRIBE","params": ["btcusdt@trade"],"id": 1}')

while True:

    response = ws.recv()
    data = json.loads(response)
    try:
        
        print(data["p"])

    except:
        print("no p")