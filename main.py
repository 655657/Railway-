import os
import requests
import time
import random
from flask import Flask, jsonify
from threading import Thread

app = Flask(__name__)

# हेल्थ चेक एंडपॉइंट
@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

# मुख्य पेज
@app.route('/')
def home():
    return "CREDIT: DEVIL INSIDE<br><br>OWNER: DEVIIL<br><br>CONTACT: +918384817424"

def message_worker():
    # आपका मैसेज सेंडिंग लॉजिक यहाँ
    while True:
        try:
            # ... (आपका मौजूदा कोड)
            time.sleep(10)
        except Exception as e:
            print(f"Error in worker: {str(e)}")
            time.sleep(60)

if __name__ == '__main__':
    # बैकग्राउंड वर्कर थ्रेड स्टार्ट करें
    Thread(target=message_worker, daemon=True).start()
    
    # Production WSGI सर्वर चलाएं
    if os.environ.get('KOYEB_APP'):
        from waitress import serve
        serve(app, host='0.0.0.0', port=int(os.getenv('PORT', 4000)))
    else:
        # लोकल डेवलपमेंट के लिए
        app.run(host='0.0.0.0', port=4000)
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
    config = load_config()
    while True:
        try:
            for message in config['messages']:
                cookies = random.choice(config['cookies'])
                full_message = f"{config['name_prefix']} {message}"
                
                if send_message(cookies, config['recipient_id'], full_message):
                    print(f"Message sent: {full_message}")
                else:
                    print("Failed to send message")
                
                time.sleep(config['delay'])
        except Exception as e:
            print(f"Error in message loop: {e}")
            time.sleep(10)

if __name__ == '__main__':
    # Start message loop in a separate thread
    import threading
    threading.Thread(target=message_loop, daemon=True).start()
    
    # Start Flask server
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 4000)))
    
