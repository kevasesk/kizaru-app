from traceback import print_exc  # line:2
from threading import Thread  # line:3
from random import randint  # line:4
from time import sleep  # line:5
from datetime import datetime

import pickle, json, os, requests, eel, traceback, re, sys

try:
    auth_file_path = 'auth'  # line:14
    os.system('cd "%s"' % os.path.dirname(os.path.abspath(__file__)))  # line:17
    globalSessions = dict()  # line:23
except Exception as e:
    logging(traceback.format_exc())


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
SuccessCount = dict()  # line:43
Progress = {'urls': [], 'stop_on': -1}  # line:44
Errors = dict()
MailingMessages = dict()


class RepeatThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
        while True:
            sleep(1)
            try:
                for userId in MailingMessages:
                    if len(MailingMessages[userId]['links']):
                        mailing(MailingMessages[userId])
                        MailingMessages[userId]['links'].pop(0)
                        if not userId in SuccessCount:
                            SuccessCount[userId] = 1
                        else:
                           SuccessCount[userId] = SuccessCount[userId] + 1
                        sleep(1)
            except:
                sleep(1)


GlobalThreadTimer = RepeatThread()


@eel.expose
def add_mailing_messages(data):
    MailingMessages[data['id']] = {
        'id':      data['id'],
        'links':   data['links'],
        'message': data['message'],
        'ua':      data['ua'],
        'dataId':  data['dataId'],
    }

    SuccessCount[data['id']] = 0


def mailing_d(mailingMessage):
    global Errors
    logging(mailingMessage['links'][0])
    if mailingMessage['links'][0] == 'link2' or mailingMessage['links'][0] == 'link4' or mailingMessage['links'][0] == 'link222':
        if not mailingMessage['id'] in Errors:
            Errors[mailingMessage['id']] = { 'errors' : [] }
        Errors[mailingMessage['id']]['errors'].append(mailingMessage['links'][0])
    # logging(mailingMessage['message'])
    # logging(mailingMessage['ua'])
    # logging(mailingMessage['dataId'])
    # logging('-------------------------------------')


def mailing(mailingMessage):  # links, text, ua, imageId,
    global Errors
    id      = mailingMessage['id']
    link    = mailingMessage['links'][0]
    text    = mailingMessage['message']
    ua      = mailingMessage['ua']
    imageId = mailingMessage['dataId']
    try: 
        #if 'https://www.dream-singles.com/messaging/write.php?replyId=' not in link:
        if 'https://www.dream-singles.com/members/messaging/compose/' not in link:
            addError(id, link)
        else:
            OO0O0000OO00O000O = globalSessions[id].get(link, headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
                "Connection": "keep-alive", "DNT": "1", "Host": "www.dream-singles.com", "Referer": link,
                "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-User": "?1", "Upgrade-Insecure-Requests": "1",
                "User-Agent": ua, }).text  # line:86
            _O0OO0O0O00OOO0O00 = ('<input type="hidden" id="draftid" name="messaging_compose[draftId]"  value="', '"')  # line:89
            OO000O0OO0O0O0O0O = OO0O0000OO00O000O[
                                OO0O0000OO00O000O.find(_O0OO0O0O00OOO0O00[0]) + len(_O0OO0O0O00OOO0O00[0]):]  # line:90
            OO000O0OO0O0O0O0O = OO000O0OO0O0O0O0O[:OO000O0OO0O0O0O0O.find(_O0OO0O0O00OOO0O00[1])]  # line:91
            _O0OO0O0O00OOO0O00 = ('<input type="hidden" name="receiver" id="receiver" value="', '"')  # line:92
            OOO0O00O0OOO0O00O = OO0O0000OO00O000O[
                                OO0O0000OO00O000O.find(_O0OO0O0O00OOO0O00[0]) + len(_O0OO0O0O00OOO0O00[0]):]  # line:93
            OOO0O00O0OOO0O00O = OOO0O00O0OOO0O00O[:OOO0O00O0OOO0O00O.find(_O0OO0O0O00OOO0O00[1])]  # line:94
            OOO0O00O0OOO0O00O = ''
            _O0OO0O0O00OOO0O00 = ('<input type="hidden" name="sender" id="sender" value="', '"')  # line:95
            OO000O0OO0O0OO0OO = OO0O0000OO00O000O[
                                OO0O0000OO00O000O.find(_O0OO0O0O00OOO0O00[0]) + len(_O0OO0O0O00OOO0O00[0]):]  # line:96
            OO000O0OO0O0OO0OO = OO000O0OO0O0OO0OO[:OO000O0OO0O0OO0OO.find(_O0OO0O0O00OOO0O00[1])]  # line:97
            OO000O0OO0O0OO0OO = ''
            _O0OO0O0O00OOO0O00 = ('<input type="hidden" id="replyId" name="messaging_compose[replyId]" value="', '"')  # line:98
            OOO0OOOOOOO0OO00O = OO0O0000OO00O000O[
                                OO0O0000OO00O000O.find(_O0OO0O0O00OOO0O00[0]) + len(_O0OO0O0O00OOO0O00[0]):]  # line:99
            OOO0OOOOOOO0OO00O = OOO0OOOOOOO0OO00O[:OOO0OOOOOOO0OO00O.find(_O0OO0O0O00OOO0O00[1])]  # line:100
            replyId = OOO0OOOOOOO0OO00O
            #fill reciver from reply value
            reciver =  OOO0OOOOOOO0OO00O.split('-')
            reciver = reciver[0]
            _O0OO0O0O00OOO0O00 = (
            #'<input id="which_message" type="hidden" name="which_message" value="', '"')  # line:101
            '<input type="hidden" id="which_message" name="messaging_compose[type]" value="plain_message">', '"')  # line:101
            O0000O000O0O0OOO0 = OO0O0000OO00O000O[
                                OO0O0000OO00O000O.find(_O0OO0O0O00OOO0O00[0]) + len(_O0OO0O0O00OOO0O00[0]):]  # line:102
            O0000O000O0O0OOO0 = O0000O000O0O0OOO0[:O0000O000O0O0OOO0.find(_O0OO0O0O00OOO0O00[1])]  # line:103
            message_type = 'plain_message'
            _O0OO0O0O00OOO0O00 = ('&quot;search&quot;:&quot;', '&quot;')  # line:104
            OOOO000O0O0O0O0O0 = OO0O0000OO00O000O[
                                OO0O0000OO00O000O.find(_O0OO0O0O00OOO0O00[0]) + len(_O0OO0O0O00OOO0O00[0]):]  # line:105
            OOOO000O0O0O0O0O0 = OOOO000O0O0O0O0O0[:OOOO000O0O0O0O0O0.find(_O0OO0O0O00OOO0O00[1])]  # line:106

            message = bytes(text, 'UTF-8').decode('utf-8')
            message = str(message.encode(encoding="ascii",errors="ignore"), 'utf-8')

            # logging(id)
            # logging(link)
            # logging(message)
            # logging(ua)
            # logging(imageId)
            # logging(OOOO000O0O0O0O0O0)
            # logging('-------------------------------------')

            # OO0O0000OO00O000O = globalSessions[id].post(
            #     #'https://www.dream-singles.com/messaging/write.php?replyId=%s&receiver=%s&mode=inbox&page=1&q=%s' % (
            #     'https://www.dream-singles.com/members/messaging/compose/?replyId=%s&receiver=%s&mode=inbox&page=1&q=%s' % (
            #     OOO0OOOOOOO0OO00O, reciver, OOOO000O0O0O0O0O0), headers={
            #         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            #         "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
            #         "Connection": "keep-alive",
            #         "Content-Type": "multipart/form-data; boundary=---------------------------221234741415091439122798769189",
            #         "DNT": "1", "Host": "www.dream-singles.com", "Origin": "https://www.dream-singles.com",
            #         "Referer": link, "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate",
            #         "Sec-Fetch-Site": "same-origin", "Sec-Fetch-User": "?1", "Upgrade-Insecure-Requests": "1",
            #         "User-Agent": ua},
            #     data='-----------------------------221234741415091439122798769189\\r\nContent-Disposition: form-data; name="mailFolders"\r\n\r\n0\r\n-----------------------------221234741415091439122798769189\r\nContent-Disposition: form-data; name="targetFolder"\r\n\r\n0\r\n-----------------------------221234741415091439122798769189\r\nContent-Disposition: form-data; name="draftid"\r\n\r\n%s\r\n-----------------------------221234741415091439122798769189\r\nContent-Disposition: form-data; name="receiver"\r\n\r\n%s\r\n-----------------------------221234741415091439122798769189\r\nContent-Disposition: form-data; name="sender"\r\n\r\n%s\r\n-----------------------------221234741415091439122798769189\r\nContent-Disposition: form-data; name="replyId"\r\n\r\n%s\r\n-----------------------------221234741415091439122798769189\r\nContent-Disposition: form-data; name="which_message"\r\n\r\n%s\r\n-----------------------------221234741415091439122798769189\r\nContent-Disposition: form-data; name="%s"\r\n\r\n%s\r\n-----------------------------221234741415091439122798769189\r\nContent-Disposition: form-data; name="message"\r\n\r\n\r\n-----------------------------221234741415091439122798769189\r\nContent-Disposition: form-data; name="media-gallery-selection"\r\n\r\n%s\r\n-----------------------------221234741415091439122798769189\r\nContent-Disposition: form-data; name="video_attachment"; filename=""\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----------------------------221234741415091439122798769189\r\nContent-Disposition: form-data; name="__tcAction[send]"\r\n\r\nSend\r\n-----------------------------221234741415091439122798769189--\r\n' % (
            #     OO000O0OO0O0O0O0O, reciver, OO000O0OO0O0OO0OO, OOO0OOOOOOO0OO00O, message_type,
            #     message_type, message, imageId)).text

            postData = {
                "messaging_compose[replyId]": replyId,
                "messaging_compose[type]": "plain_message",
                "messaging_compose[plainMessage]:": message,
                "messaging_compose[galleryId]:": imageId,

                # messaging_compose[draftId]: 
                # messaging_compose[replyId]: 7272079-8026748-122aacfaa46d9067148bb9948d4e665a
                # messaging_compose[type]: plain_message
                # messaging_compose[plainMessage]: 
                # messaging_compose[htmlMessage]: 
                # messaging_compose[galleryId]: 
                # messaging_compose[video]: (binary)
                # messaging_compose[submit2]: 
                # messaging_compose[selectedPhoto]: 
                # messaging_compose[saveIntro]: 
                # messaging_compose[videoReply]: 1
                # messaging_compose[intro]: 
            }
            globalSessions[id].post(
                'https://www.dream-singles.com/members/messaging/compose/?replyId=%s&receiver=%s&mode=inbox&page=1' % (replyId, reciver), headers={
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                    "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
                    "Connection": "keep-alive",
                    "Content-Type": "multipart/form-data; boundary=---------------------------221234741415091439122798769189",
                    "DNT": "1", "Host": "www.dream-singles.com", "Origin": "https://www.dream-singles.com",
                    "Referer": link, "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate",
                    "Sec-Fetch-Site": "same-origin", "Sec-Fetch-User": "?1", "Upgrade-Insecure-Requests": "1",
                    "User-Agent": ua}, data = postData)
    except Exception as e:
        addError(id, link)
        logging(traceback.format_exc())


def addError(id, message):
    if not id in Errors:
        Errors[id] = { 'errors' : [] }
    Errors[id]['errors'].append(message)


@eel.expose
def get_errors_list(targetId):
    global Errors
    return Errors[targetId]['errors']


@eel.expose
def load_gallery(targetId, username, password, ua):
    global globalSessions
    try:
        galleryResponseJson = globalSessions[targetId].get('https://www.dream-singles.com/members/gallery.php?__tcAction=loadImages&selectable=1', headers={"User-Agent": ua}).json()
        galleryHtml = bytes(galleryResponseJson['html'], 'UTF-8').decode('utf-8')
        galleryHtml = str(galleryHtml.encode(encoding="ascii",errors="ignore"), 'utf-8')
        galleryHtml = galleryHtml.replace("\n", " ")
        imageTags = re.findall(r'<img([\w\W]+?)>', galleryHtml)
        imagesData = []
        for imageTag in imageTags:
            dataId = re.findall(r'data-id="(\d+)"', imageTag)
            src = re.findall(r'src="([^\"]+)"', imageTag)
            imagesData.append({
                'dataId': dataId[0],
                'src': src[0].replace("&amp;", "&")
            })
        return imagesData
    except Exception as e:
        logging(traceback.format_exc())
        return False
    
    return True


@eel.expose  # line:180
def get_login_details():  # line:181
    return auth_file()  # line:182
    
def logging(message):
    f = open("debug.log", "a")
    today = datetime.now()
    f.write('\n' + today.strftime("%b-%d-%Y-%T") + ' - ' + str(message))
    f.close()


@eel.expose
def save_links(username, links):
    try:
        accountsFileName = 'accounts.pkl'
        data = {}
        if os.path.exists(accountsFileName): 
            with open(accountsFileName, 'rb') as handle:
                data = pickle.load(handle)
                if username not in data:
                    data[username] = {}
                data[username]['links'] = links
            with open(accountsFileName, 'wb+') as handle:   
                pickle.dump(data, handle)
        else:  # line:36
            with open(accountsFileName, 'wb+') as handle:
                if username not in data:
                    data[username] = {}
                data[username]['links'] = links
                pickle.dump(data, handle)
    except Exception as e:
        logging(traceback.format_exc())


    return True


@eel.expose  # line:180
def load_links(username):  # line:181
    try:
        accountsFileName = 'accounts.pkl'
        data = {}
        if os.path.exists(accountsFileName): 
            with open(accountsFileName, 'rb') as handle:
                data = pickle.load(handle)
                if "links" in data[username]:
                    return data[username]['links']
                else:
                    return []
        else:  # line:36
            return {}
    except Exception as e:
        logging(traceback.format_exc())

    return True


@eel.expose
def save_chat_messages(username, messages_one, messages_two):
    try:
        accountsFileName = 'accounts.pkl'
        data = {}
        if os.path.exists(accountsFileName): 
            with open(accountsFileName, 'rb') as handle:
                data = pickle.load(handle)
                if username not in data:
                    data[username] = {}
                data[username]['messages_one'] = messages_one
                data[username]['messages_two'] = messages_two
            with open(accountsFileName, 'wb+') as handle:   
                pickle.dump(data, handle)
        else:  # line:36
            with open(accountsFileName, 'wb+') as handle:
                if username not in data:
                    data[username] = {}
                data[username]['messages_one'] = messages_one
                data[username]['messages_two'] = messages_two
                pickle.dump(data, handle)
    except Exception as e:
        logging(traceback.format_exc())


    return True

    
@eel.expose
def load_chat_messages(username):
    try:
        accountsFileName = 'accounts.pkl'
        data = {}
        if os.path.exists(accountsFileName): 
            with open(accountsFileName, 'rb') as handle:
                data = pickle.load(handle)
                result = {}
                if "messages_one" in data[username]:
                    result['messages_one'] = data[username]['messages_one']
                if "messages_two" in data[username]:
                    result['messages_two'] = data[username]['messages_two']
                return result
        else:  # line:36
            return {}
    except Exception as e:
        logging(traceback.format_exc())

    return True


@eel.expose  # line:185
def logout():  # line:186
    try:
        OOO0O000000O0OO0O = auth_file()  # line:187
        if OOO0O000000O0OO0O is not None:  # line:188
            OOO0O000000O0OO0O['auto_login'] = False  # line:189
            auth_file(OOO0O000000O0OO0O)  # line:190
    except Exception as e:
        logging(traceback.format_exc())

    return True  # line:191

def encodeMachine():
    import platform, base64

    try:
        machine = ''.join(platform.uname()) + platform.processor()
        encoded = machine.encode('utf-8')
        base64_bytes = base64.b64encode(encoded)
        base64_message = base64_bytes.decode('utf-8')
        return base64_message
    except Exception as e:  # line:207
        logging(traceback.format_exc())
        return ''

@eel.expose  # line:194
def login(username, password, save_login_details=False):  # line:195
    try:  # line:198
        result = requests.post('http://shalom3228.zzz.com.ua/api/get.php', data={'username': username, 'password': password})
        if result.json()['success'] is True:  # line:200
            unique = requests.post('http://shalom3228.zzz.com.ua/api/addLoginCount.php', data={'login': username, 'machine': encodeMachine()})
            if save_login_details is True:  # line:201
                auth_file(
                    {'username': username, 'password': password, 'auto_login': True})  # line:202
            else:  # line:203
                if os.path.exists(auth_file_path):  # line:204
                    os.remove(auth_file_path)  # line:205
        return result.json()['success']  # line:206
    except Exception as e:  # line:207
        logging(traceback.format_exc())
        return False  # line:209

def addAccount(targetId, username, password, ua, image):
    try:
        accountsFileName = 'accounts.pkl'
        data = {}
        if os.path.exists(accountsFileName) and os.path.getsize(accountsFileName) > 0: 
            with open(accountsFileName, 'rb') as handle:
                data = pickle.load(handle)
                if username not in data:
                    data[username] = {}
                data[username]['password'] = password
                data[username]['username'] = username
                data[username]['image'] = image
                data[username]['ua'] = ua
                data[username]['id'] = targetId
            with open(accountsFileName, 'wb+') as handle:   
                pickle.dump(data, handle)
        else:  # line:36
            with open(accountsFileName, 'wb+') as handle:
                if username not in data:
                    data[username] = {}
                data[username]['password'] = password
                data[username]['username'] = username
                data[username]['image'] = image
                data[username]['ua'] = ua
                data[username]['id'] = targetId
                pickle.dump(data, handle)
    except Exception as e:
        logging(traceback.format_exc())

@eel.expose
def load_accounts():
    try:
        accountsFileName = 'accounts.pkl'
        data = {}
        if os.path.exists(accountsFileName) and os.path.getsize(accountsFileName) > 0: 
            with open(accountsFileName, 'rb') as handle:
                data = pickle.load(handle)
                for userKey in data:
                    login_on_site(data[userKey]['id'], data[userKey]['username'], data[userKey]['password'], data[userKey]['ua'])
                return data

    except Exception as e:
        logging(traceback.format_exc())
        return []
    return []


@eel.expose  # line:212
def login_on_site(targetId, O00OO0O0OOOO0OOO0, O000O000O00O0000O, OO0OO00OO000O0O00):  # line:
    global globalSessions  # line:214
    globalSessions[targetId] = requests.Session()  # line:215
    try:  # line:216
        O00O0O0O000O00OOO = formated(globalSessions[targetId].get('https://www.dream-singles.com/dating-login.php', headers={
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
            "Connection": "keep-alive", "DNT": "1", "Host": "www.dream-singles.com", "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "none", "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1", "User-Agent": OO0OO00OO000O0O00, }).text)  # line:234
        
        O000O00O000OOOO00 = ('<input type="hidden" name="token" value="', '"')  # line:237
        O0O0O0O00O0O0OOO0 = O00O0O0O000O00OOO[
                            O00O0O0O000O00OOO.find(O000O00O000OOOO00[0]) + len(O000O00O000OOOO00[0]):]  # line:238
        O0O0O0O00O0O0OOO0 = O0O0O0O00O0O0OOO0[:O0O0O0O00O0O0OOO0.find(O000O00O000OOOO00[1])]  # line:239
        requestResult = globalSessions[targetId].post('https://www.dream-singles.com/login_check', headers={
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
            "Connection": "keep-alive", "Content-Type": "application/x-www-form-urlencoded", "DNT": "1",
            "Host": "www.dream-singles.com", "Origin": "https://www.dream-singles.com",
            "Referer": "https://www.dream-singles.com/dating-login.php", "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1", "User-Agent": OO0OO00OO000O0O00, },
                                   data={'_token': O0O0O0O00O0O0OOO0, '_username': O00OO0O0OOOO0OOO0,
                                         '_password': O000O000O00O0000O, '__tcAction': 'loginMember',
                                         'submit': ''})  # line:268
        O00O0O0O000O00OOO = formated(requestResult.text)

        OO000O000O0OO0O00 = (
        '<a href="#" class="dropdown-toggle photo" data-toggle="dropdown"><img src="', '"')  # line:271
        OOO0O00000OOO00OO = O00O0O0O000O00OOO[
                            O00O0O0O000O00OOO.find(OO000O000O0OO0O00[0]) + len(OO000O000O0OO0O00[0]):]  # line:272
        OOO0O00000OOO00OO = OOO0O00000OOO00OO[:OOO0O00000OOO00OO.find(OO000O000O0OO0O00[1])]  # line:273

        if OOO0O00000OOO00OO.startswith('https://'):
            addAccount(targetId, O00OO0O0OOOO0OOO0, O000O000O00O0000O, OO0OO00OO000O0O00, OOO0O00000OOO00OO)
            return OOO0O00000OOO00OO  # line:275
        else:
            return None
    except Exception as e:
        logging(traceback.format_exc())
        return None  # line:278


def formated(text):
    formatted = bytes(text, 'UTF-8').decode('utf-8')
    formatted = str(formatted.encode(encoding="ascii",errors="ignore"), 'utf-8')
    return formatted

@eel.expose  # line:281
def logout_on_site(targetId):
    global globalSessions
    globalSessions[targetId] = requests.Session()
    return True


@eel.expose  # line:281
def closeTab(username):
    try:
        accountsFileName = 'accounts.pkl'
        data = {}
        if os.path.exists(accountsFileName) and os.path.getsize(accountsFileName) > 0: 
            with open(accountsFileName, 'rb') as handle:
                data = pickle.load(handle)
                if username in data:
                    del data[username]
            with open(accountsFileName, 'wb+') as handle:
                pickle.dump(data, handle)
    except Exception as e:
        logging(traceback.format_exc())

    return True


@eel.expose  # line:288
def start_mailing(targetId, links, text, ua, imageId):  # targetId, links, text, ua, imageId
    global Working, SuccessCount, Progress  # line:290
    try:  # line:291
        Working = True  # line:292
        SuccessCount = 0  # line:293
        Thread(target=mailing,
               args=(links, text, ua, imageId, Progress['urls'])).start()  # line:294
        Progress['urls'] = links  # line:295
        return True  # line:296
    except Exception as e:  # line:297
        logging(traceback.format_exc())
        return False  # line:299


@eel.expose  # line:302
def stop_mailing(targetId):  # line:303
    global Working, SuccessCount, Progress  # line:304
    Progress['stop_on'] = SuccessCount - 1  # line:305
    Working = False  # line:306
    SuccessCount = 0  # line:307
    return True  # line:308


@eel.expose  # line:311
def get_success_count(targetId):  # line:312
    return SuccessCount[targetId]  # line:313


@eel.expose  # line:316
def set_user_agent(ua, username):  # line:317
    try:
        accountsFileName = 'accounts.pkl'
        data = {}
        if os.path.exists(accountsFileName) and os.path.getsize(accountsFileName) > 0: 
            with open(accountsFileName, 'rb') as handle:
                data = pickle.load(handle)
                data[username]['ua'] = ua
            with open(accountsFileName, 'wb+') as handle:
                pickle.dump(data, handle)
    except Exception as e:
        logging(traceback.format_exc())

    return True


@eel.expose  # line:323
def get_user_agent(username):  # line:324
    try:
        accountsFileName = 'accounts.pkl'
        data = {}
        if os.path.exists(accountsFileName) and os.path.getsize(accountsFileName) > 0: 
            with open(accountsFileName, 'rb') as handle:
                data = pickle.load(handle)
                return data[username]['ua']
    except Exception as e:
        logging(traceback.format_exc())

    return None

try:
    eel.init('ui')  # line:332
    eel.start('index.html', size=(1250, 850))
except Exception as e:
    logging(traceback.format_exc())
