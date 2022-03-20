import requests, sys
from datetime import datetime

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
]

for fileName in files:
    try:
        data = requests.get(remote_url + fileName)
        with open(fileName, 'wb') as file:
            file.write(bytes(data.text, 'utf-8'))
    except Exception as e:
        logging(traceback.format_exc())

def logging(message):
    f = open("debug.log", "a")
    today = datetime.now()
    f.write('\n' + today.strftime("%b-%d-%Y-%T") + ' - ' + str(message))
    f.close()