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
        text="👋 𝙷𝙴𝙻𝙾 {u.mention}\n\n⎆ 𝙼𝚈 𝙽𝙰𝙼𝙴 𝙸𝚂 {message.chat.title}\n\n🕵️ 𝙸 𝙲𝙰𝙽 𝙿𝚁𝙾𝚅𝙸𝙳𝙴 𝙼𝙾𝚅𝙸𝙴𝚂,\n\n➕ 𝙹𝚄𝚂𝚃 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙴𝙽𝙹𝙾𝚈 😍\n\n👮‍♂ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁 : <a href='https://t.me/Rafeeq_Kunnimon'>★ 𝚁𝚊𝚏𝚎𝚚 ★</a>",
        reply_markup=InlineKeyboardMarkup( [[
             InlineKeyboardButton('➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘs ➕', url='http://t.me/Movie_Roster_bot?startgroup=true')
            ],[
            InlineKeyboardButton('✨ ᴡᴏʀᴋɪɴɢ ɢʀᴏᴜᴘ ✨', url='https://t.me/MovieRosterGroup')
            ],[
            InlineKeyboardButton('🕵‍♂ ᴅᴇᴠᴇʟᴏᴘᴇʀ 🕵‍♂', url='https://t.me/Rafeeq_Kunnimon'),
            InlineKeyboardButton('❤️ sᴜᴘᴘᴏʀᴛ ❤️', url='https://t.me/MovieRosterOfficial')
            ],[
            InlineKeyboardButton('📚 ʜᴇʟᴘ 📚', callback_data='help'),
            InlineKeyboardButton('🔰 ᴀʙᴏᴜᴛ 🔰', callback_data='about')
        ]]
            )
       )

@Rafeek.on_message(filters.command("help"))
async def start_message(bot, message):
    await message.reply_text(
        text="👋 ʜᴇʟʟᴏᴡ {mention}\n\n}\nʜᴇʀᴇ ɪᴅ ᴛʜᴇ ʜᴇʟᴘ ғᴏʀ ᴍʏ\nᴄᴏᴍᴍᴀɴᴅᴀ.",
        reply_markup=InlineKeyboardMarkup( [[
             InlineKeyboardButton('👮‍♂ ᴀᴅᴍɪɴ 👮‍♂', callback_data='admin'),
            InlineKeyboardButton('🔌 ᴄᴏɴɴᴇᴄᴛ 🔌', callback_data='coct'),
            ],[
            InlineKeyboardButton('🖥️ ғɪʟᴛᴇʀs 🖥️', callback_data='auto_manual'),      
            InlineKeyboardButton('🖨️ ɢᴛʀᴀɴs 🖨️', callback_data='gtrans'),
            ],[
            InlineKeyboardButton('ℹ️ ɪɴғᴏ ℹ️', callback_data='info'),
            InlineKeyboardButton('🧾 ᴍᴇᴍᴇs 🧾', callback_data='memes'),
            ],[
            InlineKeyboardButton('🔖 ᴘᴀsᴛᴇ 🔖', callback_data='paste'),
            InlineKeyboardButton('📟 ᴘᴀssᴡᴏʀᴅ ɢᴇɴ 📟', callback_data='genpassword'),
            ],[
            InlineKeyboardButton('📌 ᴘɪɴ 📌', callback_data='pin'),
            InlineKeyboardButton('🎧 ᴘᴜʀɢᴇ 🎧', callback_data='purge'),
            ],[
            InlineKeyboardButton('🎯 ʀᴇsᴛʀɪᴄ 🎯', callback_data='restric'),
            InlineKeyboardButton('🔎 sᴇᴀʀᴄʜ 🔍', callback_data='search'),
            ],[
            InlineKeyboardButton('⭕ sʜᴀʀᴇ ᴛᴇxᴛ ⭕', callback_data='sharetext'),
            InlineKeyboardButton('🎶 ᴍᴜsɪᴄ 🎶', callback_data='music'),
            ],[
            InlineKeyboardButton('🎵 ᴛᴛ-sᴘᴇᴇᴄʜ 🎵', callback_data='tts'),
            InlineKeyboardButton('📋 ᴛɢʀᴀᴘʜ 📋', callback_data='tgraph'),
            ],[
            InlineKeyboardButton('🔸 ᴛᴇxᴛ sʜᴏʀᴛɴᴇʀ 🔹', callback_data='shortner'),
            InlineKeyboardButton('🧟 ᴢᴏᴍʙɪᴇs 🧟', callback_data='zombies'),
            ],[
            InlineKeyboardButton('✖️ ʙᴀᴄᴋ ✖️', callback_data='start')
        ]]
            )
       )

Rafeek.run()
