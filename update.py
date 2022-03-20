import requests, sys

remote_url = 'https://raw.githubusercontent.com/kevasesk/kizaru-app/master/'

files = [
    'version',
    'app.py',
    'ui/index.html',
    'ui/dashboard.html',
    'ui/login.html',
    'ui/js/functions.js',
    'ui/js/gallery.js',
    'ui/css/style.css',
    'dist/js/app.b1a79375.js',
    'dist/js/app.b1a79375.js.map',
    'dist/js/chunk-vendors.d0f847fa.js',
    'dist/js/chunk-vendors.d0f847fa.js.map',
    'dist/css/app.2e4c87eb.css',
]

for fileName in files:
    data = requests.get(remote_url + fileName)
    with open(fileName, 'wb') as file:
        file.write(bytes(data.text, 'utf-8'))