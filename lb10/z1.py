import websocket

ws = websocket.WebSocket()
ws.connect("ws://echo.websocket.org")
ws.close()
