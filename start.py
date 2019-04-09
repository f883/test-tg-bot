import requests, time

#token = open("token.txt", "r").readline()
token = "563230039:AAHUxyPmnppof7X3Ffrisb9YQyi0N-TMY-0"

url = "https://api.telegram.org/bot" + token + "/"


def get_updates_json(request):  
    response = requests.get(request + 'getUpdates')
    return response.json()

def last_update(data):  
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]

def get_chat_id(update):  
    chat_id = update['message']['chat']['id']
    return chat_id

def send_mess(chat, text):  
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response

def main():  
    update_id = last_update(get_updates_json(url))['update_id']
    while True:
        if update_id == last_update(get_updates_json(url))['update_id']:
           send_mess(get_chat_id(last_update(get_updates_json(url))), 'test')
           update_id += 1
        time.sleep(1)

if __name__ == '__main__':  
    print("server started")
    main()
    print("server finished")