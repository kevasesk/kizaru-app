import requests, sys, os

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
    'ui/dist/js/app.b1a79375.js',
    'ui/dist/js/app.b1a79375.js.map',
    'ui/dist/js/chunk-vendors.d0f847fa.js',
    'ui/dist/js/chunk-vendors.d0f847fa.js.map',
    'ui/dist/css/app.2e4c87eb.css',
    'ui/img/loader_4.gif'
]

for fileName in files:
    data = requests.get(remote_url + fileName)
    if not os.path.exists('ui/dist/js'):
        os.makedirs('ui/dist/js')
    if not os.path.exists('ui/dist/css'):
        os.makedirs('ui/dist/css')
    with open(fileName, 'wb+') as file:
        file.write(bytes(data.text, 'utf-8'))

