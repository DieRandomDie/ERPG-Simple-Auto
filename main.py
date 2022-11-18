# code sourced from YouTube account CodeDict.
# video source https://www.youtube.com/watch?v=dR9n1zmw-Go
# written for the sole purpose of practice
# use at your own risk

import websocket
import json
import threading
import time
import text

token = input("Auth code: ")


def send_json_request(ws, request):
    ws.send(json.dumps(request))


def receive_json_response(ws):
    response = ws.recv()
    if response:
        return json.loads(response)


def heartbeat(interval, ws):
    print('Heartbeat begin')
    while True:
        time.sleep(interval)
        heartbeatJSON = {
            "op": 1,
            "d": "null"
        }
        send_json_request(ws, heartbeatJSON)

ws = websocket.WebSocket()
ws.connect('wss://gateway.discord.gg/?v=6&encoding=json')
event = receive_json_response(ws)

heartbeat_interval = event['d']['heartbeat_interval'] / 1000
threading._start_new_thread(heartbeat, (heartbeat_interval, ws))

payload = {
    'op': 2,
    'd': {
        'token': token,
        'properties': {
            '$os': 'windows',
            '$browser': 'chrome',
            '$device': 'pc'
        }
    }
}

send_json_request(ws, payload)

while True:
    event = receive_json_response(ws)

    try:
        text.parse(event)
        op_code = event['op']
        if op_code == 11:
            print("Heartbeat received")
    except websocket.WebSocketConnectionClosedException as e:
        ws = websocket.WebSocket()
        ws.connect('wss://gateway.discord.gg/?v=6&encoding=json')
    except:
        pass
