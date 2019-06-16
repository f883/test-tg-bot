import requests, time, wget

#token = open("token.txt", "r").readline()
token = "563230039:AAHDqwRjYUdHQmzfcTug59-jPDKQBcv6w_Q"

url = "https://api.telegram.org/bot" + token + "/"


def get_updates_json(request):  
    response = requests.get(request + 'getUpdates')
    return response.json()

def get_file_path(file_id): 
    response = requests.get(url + "getFile?file_id=" + file_id)
    jsn = response.json()
    return jsn["result"]["file_path"]

def get_image_id(update):
    file_id = update["message"]["photo"][2]["file_id"]
    return file_id

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

def download_image(address, file_name): 
    wget.download(address, file_name) 


def main():  
    update_id = last_update(get_updates_json(url))['update_id']
    while True:
        if update_id == last_update(get_updates_json(url))['update_id']:
           send_mess(get_chat_id(last_update(get_updates_json(url))), 'test')
           update_id += 1
           print(last_update(get_updates_json(url)))
           addr = get_file_path(get_image_id(last_update(get_updates_json(url))))
           print(addr)
           print()
           download_image(url + addr, "fsfsgerergfds.jpg")
        time.sleep(1)

if __name__ == '__main__':  
    print("server started")
    main()
    print("server finished")