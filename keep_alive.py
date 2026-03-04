from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Bot is alive and running!"

def run():
    # Start a web server on port 8080
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    # Run the web server in a separate thread so it doesn't block the Discord bot
    t = Thread(target=run)
    t.start()