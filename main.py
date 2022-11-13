from Pyrogram import Client, filters

API_ID = ""
API_HASE = ""
BOT_TOKEN = ""


ANUVIND = Client(
    name="TelegramBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


@ANUVIND.on_message(filters.command("start"))
async def start_cmd(client, message):
    await message.reply_text("Hello")



print("Bot Working🥵")

ANUVIND.run()
    
