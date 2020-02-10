import operator
import command_parser

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

    print(message_text)

    response = command_parser.parse_command(message_text, data)
    db_manipulator.DataBase.write_data()

    chat_id = request.get_json()['message']['chat']['id']
    res = requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'"
                       .format(TOKEN, chat_id, response))
    return Response("success")


if __name__ == '__main__':
    app.run(port=5002)
