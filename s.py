import configparser
import requests
import json
import time
config = configparser.ConfigParser()
config.read('config.ini')
#17589 last in Mirquurius_bot
my_chat_id = '1844570822'

def tg_msg_monitor():
    try:       
        api_key = '5278048008:AAGJ9zK9YOaskrrdEr2lvrdw7hAZ9T5FQ_Y'
        from_chat_id = '5123042871'
        i=int(config['DEFAULT']['i'])
        last_message = i
        without_messages = 0
        while True:
            try:  
                url = ('https://api.telegram.org/bot'+api_key+'/forwardMessage?chat_id='+my_chat_id+'&from_chat_id='+from_chat_id+'&disable_notification=true&message_id='+str(i))
                x = requests.get(url)
                if x.status_code == 200:
                    resp = json.loads(x.text)
                    text_message = resp["result"]["text"]
                    print(f"message_id =", i, x, text_message)
                    i=i+1
                    last_message = i
                    config['DEFAULT']['i'] = str(last_message)
                    with open('config.ini', 'w') as configfile:
                        config.write(configfile)
                else:
                    if x.status_code == 400:
                        without_messages = without_messages + 1
                        print(f"message_id =", i," ",x)
                        i=i+1
                    else:
                        if x.status_code == 429:
                            print('Много запросов.. Таймаут 1 минута..')
                            time.sleep(60)
                        else:
                            if x.status_code == 401:
                                print('Pizda Strausam')

                if without_messages == 10000:
                    i = last_message
                    without_messages = 0
                time.sleep(2)
            except:
                print('wait')
                i=i+1
                time.sleep(10)
    except:
        time.sleep(10)


tg_msg_monitor()