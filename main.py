import requests
import json
import time
import random
from http.server import SimpleHTTPRequestHandler, HTTPServer
import threading
import os

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"CREDIT: DEVIL INSIDE<br><br>OWNER: DEVIIL<br><br>CONTACT: +918384817424")

def run_server():
    PORT = int(os.environ.get('PORT', 4000))
    with HTTPServer(("", PORT), MyHandler) as httpd:
        print(f"Server running at http://localhost:{PORT}")
        httpd.serve_forever()

def load_cookies(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def send_message_with_cookies(cookies, recipient_id, message):
    headers = {
        'authority': 'www.facebook.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.facebook.com',
        'referer': f'https://www.facebook.com/messages/t/{recipient_id}',
        'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        'cookie': cookies
    }

    # First request to get fb_dtsg token
    session = requests.Session()
    response = session.get(f'https://www.facebook.com/messages/t/{recipient_id}', headers=headers)
    fb_dtsg = response.text.split('"token":"')[1].split('"')[0]

    # Construct the message request
    form_data = {
        'fb_dtsg': fb_dtsg,
        'body': message,
        'send': 'Send',
        'tids': f'cid.c.{recipient_id}',
        'wwwupp': 'C3',
        'platform': 'web',
        'source': 'messages_web',
        'specific_to': f'["messaging:{recipient_id}"]',
        'is_forward': 'false',
        'has_attachment': 'false',
        'replied_to_message_id': '',
        'timestamp': str(int(time.time() * 1000)),
        'client': 'web_messenger'
    }

    # Send the message
    response = session.post('https://www.facebook.com/messages/send/', data=form_data, headers=headers)
    return response.ok

def main():
    # Start server in a separate thread
    server_thread = threading.Thread(target=run_server)
    server_thread.daemon = True
    server_thread.start()

    # Load configuration
    with open('Devilconvo.txt', 'r') as f:
        recipient_id = f.read().strip()
    
    with open('Devilfile.txt', 'r') as f:
        messages = [line.strip() for line in f if line.strip()]
    
    with open('Devilname.txt', 'r') as f:
        name_prefix = f.read().strip()
    
    with open('Devilspeed.txt', 'r') as f:
        delay = int(f.read().strip())
    
    cookies_list = load_cookies('Devilcookies.txt')

    print("Starting message sending...")
    
    while True:
        try:
            for i, message in enumerate(messages):
                cookies = random.choice(cookies_list)
                full_message = f"{name_prefix} {message}"
                
                if send_message_with_cookies(cookies, recipient_id, full_message):
                    current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                    print(f"\033[1;32m[✓] Message {i+1} sent successfully at {current_time}: {full_message}")
                else:
                    print(f"\033[1;31m[✗] Failed to send message {i+1}")
                
                time.sleep(delay)
            
            print("\n[+] All messages sent. Restarting cycle...\n")
        except Exception as e:
            print(f"\033[1;31m[!] Error: {str(e)}")
            time.sleep(10)

if __name__ == '__main__':
    main()
