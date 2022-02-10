import requests, sys

remote_url = 'https://raw.githubusercontent.com/kevasesk/kizaru-app/master/'

files = [
    'app.py',
    'ui/index.html',
    'ui/dashboard.html',
    'ui/login.html',
    'js/functions.js',
    'css/style.css'
]

for fileName in files:
    data = requests.get(remote_url + fileName)
    with open(fileName, 'wb') as file:
        file.write(data.content)