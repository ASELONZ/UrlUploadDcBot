# MIT License

# Copyright (c) 2022 Hash Minner

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class Translation(object):

    START_TEXT = """
Hi {} 

I ᴀᴍ Pᴏᴡᴇʀғᴜʟ Uʀʟ Uᴘʟᴏᴀᴅᴇʀ Bᴏᴛ. Mᴜʟᴛiᴘʟᴇ Sᴏᴜʀᴄᴇ Sᴜᴘᴘᴏʀᴛ. Tᴏ sᴇᴇ /help ᴍᴏʀᴇ inғᴏʀᴍᴀᴛʜᴏɴ.
 
"""

    HELP_TEXT = """

# Sᴇɴᴅ ᴍᴇ ᴛᕼᴇ Gᴏᴏɢʟᴇ Dʀiᴠᴇ | ʏᴛᴅʟ | ᴅiʀᴇᴄᴛ ʟʜɴᴋs.

# Sᴇʟᴇᴄᴛ ᴛᕼᴇ ᴅᴇsiʀᴇᴅ ᴏᴘᴛiᴏɴ.

# Tᕼᴇɴ ʙᴇ ʀᴇʟᴀxᴇᴅ ʏᴏᴜʀ ғiʟᴇ ᴡʜʟʟ ʙᴇ ᴜᴘʟᴏᴀᴅᴇᴅ sᴏᴏɴ..

"""


    ABOUT_TEXT = """
<b>♻️ Mʏ Nᴀᴍᴇ</b> : Url Uploader

<b>🌀 Cᕼᴀɴɴᴇʟ</b> : <a href="https://t.me/defenderofthemultiverse">Cᕼᴀɴɴᴇʟ</a>

<b>🌺 Heroku</b> : <a href="https://thewarriorsreal">Gʀᴏᴜᴘ</a>

<b>  Oᴡɴᴇʀ :</b> <a href="https://Saurav3BV6SA9LLElon7Musk">Sᴀᴜʀᴀᴠ</a>

<b>👲 Oᴡɴᴇʀ :</b> <a href="https://t.me/ANKIT3690">Aɴᴋiᴛ</a>

"""

    PROGRESS = """
🔰 Speed : {3}/s\n\n
🌀 Done : {1}\n\n
🎥 Tᴏᴛᴀʟ sɪᴢᴇ  : {2}\n\n
⏳ Tɪᴍᴇ ʟᴇғᴛ : {4}\n\n
"""
    ID_TEXT = """
🆔 Your Telegram ID 𝐢𝐬 :- <code>{}</code>
"""

    INFO_TEXT = """

 🤹 First Name : <b>{}</b>

 🚴‍♂️ Second Name : <b>{}</b>

 🧑🏻‍🎓 Username : <b>@{}</b>

 🆔 Telegram Id : <code>{}</code>

 📇 Profile Link : <b>{}</b>

 📡 Dc : <b>{}</b>

 📑 Language : <b>{}</b>

 👲 Status : <b>{}</b>
"""

    START_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('❓ Help', callback_data='help'),
            InlineKeyboardButton('🦊 About', callback_data='about')
        ], [
            InlineKeyboardButton('📛 Close', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('🏠 Home', callback_data='home'),
            InlineKeyboardButton('🦊 About', callback_data='about')
        ], [
            InlineKeyboardButton('📛 Close', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('🏠 Home', callback_data='home'),
            InlineKeyboardButton('❓ Help', callback_data='help')
        ], [
            InlineKeyboardButton('📛 Close', callback_data='close')
        ]]
    )
    BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('📛 Close', callback_data='close')
        ]]
    )
    FORMAT_SELECTION = "Now Select the desired formats below."
    SET_CUSTOM_USERNAME_PASSWORD = """"""
    DOWNLOAD_START = "Trying to Download ⌛\n\n <i>{} </i>"
    UPLOAD_START = "<i>{} </i>\n\n📤 Uploading Please Wait "
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 2GB due to Telegram API limitations."
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Dᴏᴡɴʟᴏᴀᴅᴇᴅ ɪɴ {} sᴇᴄᴏɴᴅs.\n\nTʜᴀɴᴋs Fᴏʀ Usɪɴɢ Mᴇ\n\nUᴘʟᴏᴀᴅᴇᴅ ɪɴ {} sᴇᴄᴏɴᴅs"
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Media cleared succesfully."
    CUSTOM_CAPTION_UL_FILE = " "
    NO_VOID_FORMAT_FOUND = "ERROR... <code>{}</code>"
    FREE_USER_LIMIT_Q_SZE = """Cannot Process Free users only 1 request per 4 hrs\n
Upgrade your /plans to Remove Time Gaps and For link Processing"""
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
