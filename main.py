import os

from pyrogram import Client as AFK, idle

from pyrogram.enums import ChatMemberStatus, ChatMembersFilter

from pyrogram import enums

from pyrogram.types import ChatMember

import asyncio

import logging

import tgcrypto

from pyromod import listen

import logging

from tglogging import TelegramLogHandler

from aiohttp import web

import config from config



logging.basicConfig(

    level=logging.INFO,    

    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",

    datefmt='%d-%b-%y %H:%M:%S'

)

LOGGER = logging.getLogger(__name__)

LOGGER.info("Live log streaming to telegram.")



plugins = dict(root="plugins")



if __name__ == "__main__":

    bot = bot(

        "Bot",

        bot_token=Config.BOT_TOKEN,

        api_id=Config.API_ID,

        api_hash=Config.API_HASH,

        sleep_threshold=120,

        plugins=plugins,

        workers=10,

    )

    

    app = web.Application()

routes = web.RouteTableDef()



@routes.get("/")

async def home(request):

    return web.Response(text="Hello, Docker!")



app.add_routes(routes)



# Get the port from environment variables (default: 8080)

PORT = int(os.getenv("PORT", 8080))



if __name__ == "__main__":

    web.run_app(app, host="0.0.0.0", port=PORT)

   

    async def main():

        await bot.start()

        bot_info = await bot.get_me()

        LOGGER.info(f"<--- @{bot_info.username} Started --->")

        for user_id in Config.AUTH_USERS:

            try:

                await bot.send_message(chat_id=user_id, text=f"__Congrats! You Are DRM member ... if You get any error then contact me -  {Config.CREDIT}__ ")

            except Exception as e:

                LOGGER.error(f"Failed to send message to user {user_id}: {e}")

                continue

        await idle()

    asyncio.get_event_loop().run_until_complete(main())

    LOGGER.info("<---🦅 Stopped baby💞 --->")
