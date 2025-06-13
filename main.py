import os
import requests
import time
import random
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "CREDIT: DEVIL INSIDE<br><br>OWNER: DEVIIL<br><br>CONTACT: +918384817424"

def load_config():
    config = {
        'cookies': os.getenv('COOKIES', '').split('|'),
        'recipient_id': os.getenv('RECIPIENT_ID', ''),
        'messages': os.getenv('MESSAGES', '').split('|'),
        'name_prefix': os.getenv('NAME_PREFIX', ''),
        'delay': int(os.getenv('DELAY', '5'))
    }
    return config

def send_message(cookies, recipient_id, message):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Cookie': cookies
    }
    
    try:
        # Implement your message sending logic here
        # This is a placeholder for actual implementation
        print(f"Sending message to {recipient_id}: {message}")
        return True
    except Exception as e:
        print(f"Error sending message: {e}")
        return False

def message_loop():
    config =
