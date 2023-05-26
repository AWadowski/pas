import websocket

try:
    ws = websocket.WebSocket()
    ws.connect("ws://echo.websocket.org")
    message_to_send = "Hello, WebSocket server!"
    if len(message_to_send.encode('utf-8')) <= 125:
        ws.send(message_to_send)
        print("Message sent: {}".format(message_to_send))
    else:
        print("Message is too long. Please keep it under 125 bytes.")
finally:
    ws.close()
