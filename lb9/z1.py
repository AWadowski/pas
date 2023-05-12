import requests

url = 'http://httpbin.org/html'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Safari/7.0.3'}

response = requests.get(url, headers=headers)

with open('output.html', 'w') as f:
    f.write(response.text)
