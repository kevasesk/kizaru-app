import eel, requests, os,sys, subprocess

def downloadUpdate():
    response = requests.get('https://raw.githubusercontent.com/kevasesk/kizaru-app/master/version')
    file_name = 'version'
    with open(file_name, "wb+") as file:
        file.write(response.content)

    response = requests.get('https://raw.githubusercontent.com/kevasesk/kizaru-app/master/dist/DSBot.exe')
    file_name = 'data'
    with open(file_name, "wb+") as file:
        file.write(response.content)


@eel.expose
def update():
    try:
        if os.path.isfile('version') and os.path.isfile('data'):
            data = requests.get('https://raw.githubusercontent.com/kevasesk/kizaru-app/master/version')
            if data.status_code == 200:
                f = open("version", "r")
                fileText = f.read()
                if data.text != fileText:
                    downloadUpdate()
                else:
                    return True
            else:
                return False
        else:
            downloadUpdate()
        return True
    except Exception as e:
        return False


@eel.expose
def run():
    exe = os.path.dirname(sys.executable) + "\data"
    script = os.path.dirname(os.path.abspath(__file__)) + "\data"
    subprocess.call(exe)


try:
    eel.init('static')  # line:332
    eel.start('launcher.html', size=(255, 255), position=(300,300), port=8001)
except Exception as e:
    pass




