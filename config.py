import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", '8667672710:AAE00K_U0nAJh6yvPCVTB9iwXxgiNJzYJps')
    API_ID = int(os.environ.get("API_ID", '32055524'))
    API_HASH = os.environ.get("API_HASH", '52777b469ffe310595012e55028d746d')
    AUTH_USER = os.environ.get('AUTH_USERS', '6231590946').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = "𝗥𝗼𝘆 𝗝𝗮𝗮𝘁™"#Here You Can Change with Your Name  or any custom name or title you prefer
