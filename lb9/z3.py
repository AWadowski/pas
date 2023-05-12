import requests

url = 'http://212.182.24.27:8080/image.jpg'
headers = {'Range': 'bytes=0-999'}  # Ajust as needed

response = requests.get(url, headers=headers)

with open('output.jpg', 'wb') as f:
    f.write(response.content)
