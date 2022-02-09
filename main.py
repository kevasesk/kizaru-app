from traceback import print_exc  # line:2
from threading import Thread  # line:3
from random import randint  # line:4
from time import sleep  # line:5
import pickle  # line:6
import json  # line:7
import os  # line:8
import requests  # line:11
import eel  # line:12

auth_file_path = 'auth'  # line:14
os.system('cd "%s"' % os.path.dirname(os.path.abspath(__file__)))  # line:17
cfg = {
	"DELAY_BETWEEN_URLS": [1, 3],
	"DELAY_BETWEEN_ACTIONS": [3, 6]
}
#with open('config.json', 'r', encoding='utf8') as f:  # line:19
#    cfg = json.loads(f.read())  # line:20
s = requests.Session()  # line:23


def auth_file(obj=None):  # line:26
    if obj is None:  # line:28
        if os.path.exists(auth_file_path):  # line:29
            with open(auth_file_path, 'rb') as OO0OO00O00OOO0O00:  # line:30
                return pickle.load(OO0OO00O00OOO0O00)  # line:31
        else:  # line:32
            return None  # line:33
    else:  # line:36
        with open(auth_file_path, 'wb+') as OO0OO00O00OOO0O00:  # line:37
            pickle.dump(obj, OO0OO00O00OOO0O00)  # line:38
        return obj  # line:39


Working = False  # line:42
SuccessCount = 0  # line:43
Progress = {'urls': [], 'stop_on': -1}  # line:44


def mailing(OOO00OOOO0O0OOOOO, O0O0OOO00O00000OO, O0OOO00OOOO00OOOO, old_urls=[]):  # line:47
    global Working, SuccessCount, Progress, s  # line:48
    for OO00O000OO0O000OO, O0O00O0O0OOOO00OO in enumerate(OOO00OOOO0O0OOOOO):  # line:49
        if not Working:  # line:50
            break  # line:51
        if old_urls == OOO00OOOO0O0OOOOO and OO00O000OO0O000OO < Progress['stop_on'] + 1:  # line:52
            SuccessCount += 1  # line:53
            continue  # line:54
        try:  # line:55
            if 'https://www.dream-singles.com/messaging/write.php?replyId=' not in O0O00O0O0OOOO00OO:  # line:56
                SuccessCount += 1  # line:57
                continue  # line:58
            sleep(randint(cfg['DELAY_BETWEEN_URLS'][0], cfg['DELAY_BETWEEN_URLS'][1]))  # line:66
            OO0O0000OO00O000O = s.get(O0O00O0O0OOOO00OO, headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
                "Connection": "keep-alive", "DNT": "1", "Host": "www.dream-singles.com", "Referer": O0O00O0O0OOOO00OO,
                "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-User": "?1", "Upgrade-Insecure-Requests": "1",
                "User-Agent": O0OOO00OOOO00OOOO, }).text  # line:86
            _O0OO0O0O00OOO0O00 = ('<input type="hidden" name="draftid" id="draftid" value="', '"')  # line:89
            OO000O0OO0O0O0O0O = OO0O0000OO00O000O[
                                OO0O0000OO00O000O.find(_O0OO0O0O00OOO0O00[0]) + len(_O0OO0O0O00OOO0O00[0]):]  # line:90
            OO000O0OO0O0O0O0O = OO000O0OO0O0O0O0O[:OO000O0OO0O0O0O0O.find(_O0OO0O0O00OOO0O00[1])]  # line:91
            _O0OO0O0O00OOO0O00 = ('<input type="hidden" name="receiver" id="receiver" value="', '"')  # line:92
            OOO0O00O0OOO0O00O = OO0O0000OO00O000O[
                                OO0O0000OO00O000O.find(_O0OO0O0O00OOO0O00[0]) + len(_O0OO0O0O00OOO0O00[0]):]  # line:93
            OOO0O00O0OOO0O00O = OOO0O00O0OOO0O00O[:OOO0O00O0OOO0O00O.find(_O0OO0O0O00OOO0O00[1])]  # line:94
            _O0OO0O0O00OOO0O00 = ('<input type="hidden" name="sender" id="sender" value="', '"')  # line:95
            OO000O0OO0O0OO0OO = OO0O0000OO00O000O[
                                OO0O0000OO00O000O.find(_O0OO0O0O00OOO0O00[0]) + len(_O0OO0O0O00OOO0O00[0]):]  # line:96
            OO000O0OO0O0OO0OO = OO000O0OO0O0OO0OO[:OO000O0OO0O0OO0OO.find(_O0OO0O0O00OOO0O00[1])]  # line:97
            _O0OO0O0O00OOO0O00 = ('<input type="hidden" name="replyId" value="', '"')  # line:98
            OOO0OOOOOOO0OO00O = OO0O0000OO00O000O[
                                OO0O0000OO00O000O.find(_O0OO0O0O00OOO0O00[0]) + len(_O0OO0O0O00OOO0O00[0]):]  # line:99
            OOO0OOOOOOO0OO00O = OOO0OOOOOOO0OO00O[:OOO0OOOOOOO0OO00O.find(_O0OO0O0O00OOO0O00[1])]  # line:100
            _O0OO0O0O00OOO0O00 = (
            '<input id="which_message" type="hidden" name="which_message" value="', '"')  # line:101
            O0000O000O0O0OOO0 = OO0O0000OO00O000O[
                                OO0O0000OO00O000O.find(_O0OO0O0O00OOO0O00[0]) + len(_O0OO0O0O00OOO0O00[0]):]  # line:102
            O0000O000O0O0OOO0 = O0000O000O0O0OOO0[:O0000O000O0O0OOO0.find(_O0OO0O0O00OOO0O00[1])]  # line:103
            _O0OO0O0O00OOO0O00 = ('&quot;search&quot;:&quot;', '&quot;')  # line:104
            OOOO000O0O0O0O0O0 = OO0O0000OO00O000O[
                                OO0O0000OO00O000O.find(_O0OO0O0O00OOO0O00[0]) + len(_O0OO0O0O00OOO0O00[0]):]  # line:105
            OOOO000O0O0O0O0O0 = OOOO000O0O0O0O0O0[:OOOO000O0O0O0O0O0.find(_O0OO0O0O00OOO0O00[1])]  # line:106
            sleep(randint(cfg['DELAY_BETWEEN_ACTIONS'][0], cfg['DELAY_BETWEEN_ACTIONS'][1]))  # line:109
            OO0O0000OO00O000O = s.get(
                'https://www.dream-singles.com/members/gallery.php?__tcAction=loadImages&selectable=1',
                headers={"Accept": "*/*", "Accept-Encoding": "gzip, deflate, br",
                         "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3", "Connection": "keep-alive",
                         "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "DNT": "1",
                         "Host": "www.dream-singles.com", "Referer": O0O00O0O0OOOO00OO, "Sec-Fetch-Dest": "empty",
                         "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "User-Agent": O0OOO00OOOO00OOOO,
                         "X-Requested-With": "XMLHttpRequest", }).text  # line:128
            _O0OO0O0O00OOO0O00 = (
            r'<div class=\"col-xs-6 col-sm-6 col-md-4 col-xl-3 text-center gallery-media-wrapper\" data-id=\"',
            r'\"')  # line:129
            OO0O0O0O0O000OO0O = OO0O0000OO00O000O[
                                OO0O0000OO00O000O.find(_O0OO0O0O00OOO0O00[0]) + len(_O0OO0O0O00OOO0O00[0]):]  # line:130
            OO0O0O0O0O000OO0O = OO0O0O0O0O000OO0O[:OO0O0O0O0O000OO0O.find(_O0OO0O0O00OOO0O00[1])]  # line:131
            sleep(randint(cfg['DELAY_BETWEEN_ACTIONS'][0], cfg['DELAY_BETWEEN_ACTIONS'][1]))  # line:136
            OO0O0000OO00O000O = s.post(
                'https://www.dream-singles.com/messaging/write.php?replyId=%s&receiver=%s&mode=inbox&page=1&q=%s' % (
                OOO0OOOOOOO0OO00O, OOO0O00O0OOO0O00O, OOOO000O0O0O0O0O0), headers={
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                    "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
                    "Connection": "keep-alive",
                    "Content-Type": "multipart/form-data; boundary=---------------------------221234741415091439122798769189",
                    "DNT": "1", "Host": "www.dream-singles.com", "Origin": "https://www.dream-singles.com",
                    "Referer": O0O00O0O0OOOO00OO, "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate",
                    "Sec-Fetch-Site": "same-origin", "Sec-Fetch-User": "?1", "Upgrade-Insecure-Requests": "1",
                    "User-Agent": O0OOO00OOOO00OOOO},
                data='-----------------------------221234741415091439122798769189\\r\nContent-Disposition: form-data; name="mailFolders"\r\n\r\n0\r\n-----------------------------221234741415091439122798769189\r\nContent-Disposition: form-data; name="targetFolder"\r\n\r\n0\r\n-----------------------------221234741415091439122798769189\r\nContent-Disposition: form-data; name="draftid"\r\n\r\n%s\r\n-----------------------------221234741415091439122798769189\r\nContent-Disposition: form-data; name="receiver"\r\n\r\n%s\r\n-----------------------------221234741415091439122798769189\r\nContent-Disposition: form-data; name="sender"\r\n\r\n%s\r\n-----------------------------221234741415091439122798769189\r\nContent-Disposition: form-data; name="replyId"\r\n\r\n%s\r\n-----------------------------221234741415091439122798769189\r\nContent-Disposition: form-data; name="which_message"\r\n\r\n%s\r\n-----------------------------221234741415091439122798769189\r\nContent-Disposition: form-data; name="%s"\r\n\r\n%s\r\n-----------------------------221234741415091439122798769189\r\nContent-Disposition: form-data; name="message"\r\n\r\n\r\n-----------------------------221234741415091439122798769189\r\nContent-Disposition: form-data; name="media-gallery-selection"\r\n\r\n%s\r\n-----------------------------221234741415091439122798769189\r\nContent-Disposition: form-data; name="video_attachment"; filename=""\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----------------------------221234741415091439122798769189\r\nContent-Disposition: form-data; name="__tcAction[send]"\r\n\r\nSend\r\n-----------------------------221234741415091439122798769189--\r\n' % (
                OO000O0OO0O0O0O0O, OOO0O00O0OOO0O00O, OO000O0OO0O0OO0OO, OOO0OOOOOOO0OO00O, O0000O000O0O0OOO0,
                O0000O000O0O0OOO0, O0O0OOO00O00000OO, OO0O0O0O0O000OO0O)).text  # line:168
            SuccessCount += 1  # line:171
        except:  # line:173
            print_exc()  # line:174
    sleep(1)  # line:175
    Working = False  # line:176
    SuccessCount = 0  # line:177


@eel.expose  # line:180
def get_login_details():  # line:181
    return auth_file()  # line:182


@eel.expose  # line:185
def logout():  # line:186
    OOO0O000000O0OO0O = auth_file()  # line:187
    if OOO0O000000O0OO0O is not None:  # line:188
        OOO0O000000O0OO0O['auto_login'] = False  # line:189
        auth_file(OOO0O000000O0OO0O)  # line:190
    return True  # line:191


@eel.expose  # line:194
def login(O0O0OOO00OOO00OOO, OOOOOO0O0O000O0OO, save_login_details=False):  # line:195
    global s  # line:196
    s = requests.Session()  # line:197
    try:  # line:198
        OOOO0O0O000O00OOO = requests.post('http://shalom3228.zzz.com.ua/api/get.php', data={'username': O0O0OOO00OOO00OOO,
                                                                         'password': OOOOOO0O0O000O0OO})  # line:199
        if OOOO0O0O000O00OOO.json()['success'] is True:  # line:200
            if save_login_details is True:  # line:201
                auth_file(
                    {'username': O0O0OOO00OOO00OOO, 'password': OOOOOO0O0O000O0OO, 'auto_login': True})  # line:202
            else:  # line:203
                if os.path.exists(auth_file_path):  # line:204
                    os.remove(auth_file_path)  # line:205
        return OOOO0O0O000O00OOO.json()['success']  # line:206
    except:  # line:207
        print_exc()  # line:208
        return False  # line:209


@eel.expose  # line:212
def login_on_site(O00OO0O0OOOO0OOO0, O000O000O00O0000O, OO0OO00OO000O0O00):  # line:
    global s  # line:214
    s = requests.Session()  # line:215
    try:  # line:216
        O00O0O0O000O00OOO = s.get('https://www.dream-singles.com/dating-login.php', headers={
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
            "Connection": "keep-alive", "DNT": "1", "Host": "www.dream-singles.com", "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "none", "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1", "User-Agent": OO0OO00OO000O0O00, }).text  # line:234
        O000O00O000OOOO00 = ('<input type="hidden" name="token" value="', '"')  # line:237
        O0O0O0O00O0O0OOO0 = O00O0O0O000O00OOO[
                            O00O0O0O000O00OOO.find(O000O00O000OOOO00[0]) + len(O000O00O000OOOO00[0]):]  # line:238
        O0O0O0O00O0O0OOO0 = O0O0O0O00O0O0OOO0[:O0O0O0O00O0O0OOO0.find(O000O00O000OOOO00[1])]  # line:239
        O00O0O0O000O00OOO = s.post('https://www.dream-singles.com/dating-login.php?loc=', headers={
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
            "Connection": "keep-alive", "Content-Type": "application/x-www-form-urlencoded", "DNT": "1",
            "Host": "www.dream-singles.com", "Origin": "https://www.dream-singles.com",
            "Referer": "https://www.dream-singles.com/dating-login.php", "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1", "User-Agent": OO0OO00OO000O0O00, },
                                   data={'token': O0O0O0O00O0O0OOO0, 'login': O00OO0O0OOOO0OOO0,
                                         'password': O000O000O00O0000O, '__tcAction': 'loginMember',
                                         'submit': ''}).text  # line:268
        OO000O000O0OO0O00 = (
        '<a href="#" class="dropdown-toggle photo" data-toggle="dropdown"><img src="', '"')  # line:271
        OOO0O00000OOO00OO = O00O0O0O000O00OOO[
                            O00O0O0O000O00OOO.find(OO000O000O0OO0O00[0]) + len(OO000O000O0OO0O00[0]):]  # line:272
        OOO0O00000OOO00OO = OOO0O00000OOO00OO[:OOO0O00000OOO00OO.find(OO000O000O0OO0O00[1])]  # line:273
        return OOO0O00000OOO00OO  # line:275
    except:  # line:276
        print_exc()  # line:277
        return None  # line:278


@eel.expose  # line:281
def logout_on_site():  # line:282
    global s  # line:283
    s = requests.Session()  # line:284
    return True  # line:285


@eel.expose  # line:288
def start_mailing(O00OO000O0O00O00O, O00O0OO000000OOOO, O000OO00O00OOO000):  # line:289
    global Working, SuccessCount, Progress  # line:290
    try:  # line:291
        Working = True  # line:292
        SuccessCount = 0  # line:293
        Thread(target=mailing,
               args=(O00OO000O0O00O00O, O00O0OO000000OOOO, O000OO00O00OOO000, Progress['urls'])).start()  # line:294
        Progress['urls'] = O00OO000O0O00O00O  # line:295
        return True  # line:296
    except:  # line:297
        print_exc()  # line:298
        return False  # line:299


@eel.expose  # line:302
def stop_mailing():  # line:303
    global Working, SuccessCount, Progress  # line:304
    Progress['stop_on'] = SuccessCount - 1  # line:305
    Working = False  # line:306
    SuccessCount = 0  # line:307
    return True  # line:308


@eel.expose  # line:311
def get_success_count():  # line:312
    return SuccessCount  # line:313


@eel.expose  # line:316
def set_user_agent(O0OOOO0O00OOOOO00):  # line:317
    with open('User-Agent', 'w+', encoding='utf8') as OOO0O0OO0O0O0OO00:  # line:318
        OOO0O0OO0O0O0OO00.write(O0OOOO0O00OOOOO00)  # line:319
    return True  # line:320


@eel.expose  # line:323
def get_user_agent():  # line:324
    try:  # line:325
        with open('User-Agent', 'r', encoding='utf8') as OO00OO00OOOO00OO0:  # line:326
            return (OO00OO00OOOO00OO0.read())  # line:327
    except:  # line:328
        return None  # line:329


eel.init('ui')  # line:332
eel.start('index.html', size=(1250, 750))
