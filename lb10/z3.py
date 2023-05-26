import websocket

try:
    ws = websocket.WebSocket()
    ws.connect("ws://echo.websocket.org")
    message_to_send = "Hello, WebSocket server!"  # Your message here
    ws.send(message_to_send)
    print("Message sent: {}".format(message_to_send))
finally:
    ws.close()
