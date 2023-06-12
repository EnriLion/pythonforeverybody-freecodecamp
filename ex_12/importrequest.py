import requests

url = 'https://data.pr4e.org/romeo.txt'

response = requests.get(url)

if response.status_code == 200:
    with open('romeo.txt', 'wb') as f:
        f.write(response.content)
else:
    print(response.status_code)

