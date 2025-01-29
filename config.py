import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", '')
    API_ID = int(os.environ.get("API_ID", '23442913'))
    API_HASH = os.environ.get("API_HASH", '864a97e16b4ff7dc65ff5e2d1549b4a2')
    AUTH_USER = os.environ.get('AUTH_USERS','7841326954').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    WEBHOOK = True  # Don't change this
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = "🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌"#Here You Can Change with Your Name  or any custom name or title you prefer
    port = int(os.environ.get('PORT', 8080))  # Default to 5000 for local testing
    app.run(host='0.0.0.0', port=port)

