import operator

import requests
from flask import Flask, Response, request
import model
import db_manipulator

app = Flask(__name__)

TOKEN = '1045010708:AAFKq_tnqakfeAHC44M-XQqiZeKT73-G_GI'
TELEGRAM_INIT_WEBHOOK_URL = 'https://api.telegram.org/bot{}/setWebhook?url=https://d1194241.ngrok.io/message'.format(
    TOKEN)

requests.get(TELEGRAM_INIT_WEBHOOK_URL)

data = db_manipulator.DataBase.read_data()

@app.route('/sanity')
def sanity(): return "Server is running"


@app.route('/message', methods=["POST"])
def handle_message():
    print("got message")
    message_text: str = request.get_json()['message']['text']

    response = "Got it"

    splited_text_message = message_text.split()

    command: str = splited_text_message[0]

    if len(splited_text_message) < 2:
        if command == '/popular':
            response = max(data.items(), key=operator.itemgetter(1))[0]
        else:
            response = 'not a command'
    else:
        number: int = int(splited_text_message[1])
        data[number] += 1
        print(message_text)
        response = model.command_to_function[command](number)

    chat_id = request.get_json()['message']['chat']['id']
    res = requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'"
                       .format(TOKEN, chat_id, response))

    return Response("success")


if __name__ == '__main__':
    app.run(port=5002)
    db_manipulator.DataBase.write_data()
