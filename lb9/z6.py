import requests

url = 'http://212.182.24.27:8080/image.jpg'
headers = {'If-Modified-Since': 'Sat, 29 Oct 2023 19:43:31 GMT'}  # Ustaw na datę ostatniego pobrania

response = requests.get(url, headers=headers)

if response.status_code == 200:
    with open('output.jpg', 'wb') as f:
        f.write(response.content)
else:
    print('Obrazek nie został zmieniony od ostatniego pobrania.')
