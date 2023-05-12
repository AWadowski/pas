import requests

url = 'http://httpbin.org/image/png'

response = requests.get(url)

with open('output.png', 'wb') as f:
    f.write(response.content)
