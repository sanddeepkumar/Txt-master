import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", '7929130193:AAFJswIMtSV_CPazyAPKW4BQ58ijov3t-5I')
    API_ID = int(os.environ.get("API_ID", '28094744'))
    API_HASH = os.environ.get("API_HASH", 'a75af4285edc7747c57bb19147ca0b9b')
    AUTH_USER = os.environ.get('AUTH_USERS','5680454765').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    WEBHOOK = True  # Don't change this
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = "🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌"#Here You Can Change with Your Name  or any custom name or title you prefer
    port = int(os.environ.get('PORT', 8080))  # Default to 5000 for local testing
    app.run(host='0.0.0.0', port=port)

