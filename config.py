import os
from flask import Flask

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", '')
    API_ID = int(os.environ.get("API_ID", '26148784'))
    API_HASH = os.environ.get("API_HASH", 'e1428799c0aeccd0a3cd1f15606e7a80')
    AUTH_USER = os.environ.get('AUTH_USERS','7148824590').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    WEBHOOK = True  # Don't change this
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = "🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌"#Here You Can Change with Your Name  or any custom name or title you prefer
    port = int(os.environ.get('PORT', 8080))  # Default to 5000 for local testing

app = Flask(__name__)  # Initialize the Flask app

@app.route('/')
def home():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
