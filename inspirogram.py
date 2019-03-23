#!/usr/bin/python3
import os, requests, time, json
from instapy_cli import client

def load_config():
    with open('config.json') as confFile:
        return json.load(confFile)

config = load_config()

def main():
    print("Initializing...")
    the_quote = generate_quote()
    send_to_ig(the_quote)

def generate_quote():
    print("Generating quote...")
    r = requests.get("https://inspirobot.me/api?generate=true")
    if r.ok:
        return r.text
    else:
        return None

def send_to_ig(quoteid):
    if quoteid is None:
        print("Quote didn't get generated!")
    else:
        print(f"Uploading {quoteid} to IG...")
        with client(config['ig_username'], config['ig_password']) as cli:
            try:
                cli.upload(quoteid, config['post_text'])
                print("Uploaded to IG!")
            except Exception as e:
                print(f"Failed to upload to IG: {e}")
                exit()

def setTimeout():
    while True:
        main()
        time.sleep(config['timeout'])

if __name__ == '__main__':
    setTimeout()
