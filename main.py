from Pyrogram import Client, filters

API_ID = "23091473"
API_HASE = "f9be1bdf0d12748c40b61c2b1f291e0d"
BOT_TOKEN = "5721163594:AAHye3moY_9nyppGT_n9cvJjFv-x4BWZ0kA"


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
    
