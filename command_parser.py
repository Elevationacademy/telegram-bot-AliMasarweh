import operator

import requests
from flask import request

import model
from testing import TOKEN


def parse_command(message_text: str, data):
    splited_text_message = message_text.split()

    command: str = splited_text_message[0]

    if command not in model.command_to_function:
        return "not a proper command"

    if len(splited_text_message) < 2:
        print(command)
        print(model.command_to_function[command])
        response = model.command_to_function[command](data)
    else:
        number: int = int(splited_text_message[1])
        data[number] += 1
        print(model.command_to_function[command])
        response = model.command_to_function[command](number)

    return response
