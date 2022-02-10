import requests, sys, os

def downloadUpdate():
    remote_url = 'https://raw.githubusercontent.com/kevasesk/kizaru-app/master/update.py'
    local_file = 'update.py'
    data = requests.get(remote_url)
    with open(local_file, 'wb') as file:
        file.write(data.content)

        
remote_url = 'https://raw.githubusercontent.com/kevasesk/kizaru-app/master/version'
local_file = 'version'
data = requests.get(remote_url)

if data.status_code == 200:
    versionFileExist = os.path.exists('./version')
    if versionFileExist:
        f = open("version", "r")
        if data.content != f.read():
            downloadUpdate()
    else:
        downloadUpdate()

    import update

print('before app')
sys.exit()
import app



