import requests


print('executed update')
sys.exit()

remote_url = 'https://raw.githubusercontent.com/kevasesk/kizaru-app/master/app.py'
local_file = 'app.py'
data = requests.get(remote_url)
with open(local_file, 'wb') as file:
    file.write(data.content)