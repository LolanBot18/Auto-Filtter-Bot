from pyrogram import Client, filters
from pyrogram.types import Message

Muhammad=Client(
    "Auto Filter Bot",
    bot_token="5128376307:AAEnMFvurvU2lpdhHsvJC0G-pJRf_Rdt5bs",
    api_id="6327652",
    api_hash="6c2ee4bf150d9f3cd3e3d64aad0772c8"
)

@Muhammad.on_message(filters.command("start"))
async def start_message(bot, message):
    await message.reply_text("👋 Hey How are You")

@Muhammad.on_message(filters.command("help"))
async def help(bot: Muhammad message: Message):
    await message.reply_text("❌ Not Help You Ok 😐")

Muhammad.run()
