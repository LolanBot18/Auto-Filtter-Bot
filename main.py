from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

Rafeek=Client(
    "Auto Filter Bot",
    bot_token="5128376307:AAEnMFvurvU2lpdhHsvJC0G-pJRf_Rdt5bs",
    api_id="6327652",
    api_hash="6c2ee4bf150d9f3cd3e3d64aad0772c8"
)

@Rafeek.on_message(filters.command("start"))
async def start_message(bot, message):
    await message.reply_text(
        text="👋 𝙷𝙴𝚈 𝙷𝙾𝚆 𝙰𝚁𝙴 𝚈𝙾𝚄?",
        reply_markup=InlineKeyboardMarkup
             InlineKeyboardButton("😎 𝙹𝙾𝙸𝙽 𝚄𝙿𝙳𝙰𝚃𝙴 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 😎", url="https://t.me/MovieRosterOfficial")
            ]]
            )
       )

@Rafeek.on_message(filters.command("help"))
async def start_message(bot, message):
    await message.reply_text(
        text="🤠 𝚙𝚘𝚍𝚎 𝚖𝚎𝚢𝚛𝚎 🤠",
        reply_markup=InlineKeyboardMarkup
             InlineKeyboardButton("😎 𝙹𝙾𝙸𝙽 𝚄𝙿𝙳𝙰𝚃𝙴 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 😎", url="https://t.me/MovieRosterOfficial"),
             InlineKeyboardButton ("😋 𝚊 𝚠𝚘𝚎𝚛 😋", url=https://t.me/MovieRosterOfficial")
            ]]
            )
       )

Rafeek.run()
