import requests, sys, os

def downloadUpdate():
    try:
        remote_url = 'https://raw.githubusercontent.com/kevasesk/kizaru-app/master/update.py'
        local_file = 'update.py'
        data = requests.get(remote_url)
        with open(local_file, 'wb') as file:
            file.write(data.content)
    except Exception as e:
        logging(traceback.format_exc())   
    import update


remote_url = 'https://raw.githubusercontent.com/kevasesk/kizaru-app/master/version'
local_file = 'version'
data = requests.get(remote_url)

if data.status_code == 200:
    versionFileExist = os.path.exists('./version')
    if versionFileExist:
        f = open("version", "r")
        fileText = f.read()
        if data.text != fileText:
            downloadUpdate()
    else:
        downloadUpdate()


import app



