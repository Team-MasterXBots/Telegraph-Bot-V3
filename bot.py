import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from telegraph import upload_file
from Config import Config
psycho = Client(
    "Telegraph Uploader Bot",
    bot_token = Config.TOKEN,
    api_id = Config.API_ID,
    api_hash = Config.API_HASH
)
DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/")

START_TEXT = """
H![✨](https://telegra.ph/file/1434d9d0eb6a8bf00456a.jpg)
I am Telegraph Media Converter🧳 Create by Telegraph v3
I can create Pictures under 5MB

~ @Master_X_Updates ~
"""
HELP_TEXT = """
- Just give me a media under 5MB
- Then I will download it
- I will then upload it to the telegra.ph link

Support ~ @Master_X_Updates ~
"""
ABOUT_TEXT = """
- **Bot :** `Telegraph Uploader v3`
- **Python3 :** `3.9.6`
- **Updates Channel: **[Master X Bot's Updates](t.me/Master_X_Updates)
- **Support :** [Best Friends](t.me/Best_Friends15)

"""
START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('About', callback_data='about'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('About', callback_data='about'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Support', url="t.me/Best_Friends15"),
        InlineKeyboardButton('Updates', url='https://t.me/Master_X_Updates')
        ],
        [
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )

@psycho.on_callback_query()
async def cb_data(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            disable_web_page_preview=False,
            reply_markup=START_BUTTONS
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            disable_web_page_preview=True,
            reply_markup=ABOUT_BUTTONS
        )
    else:
        await update.message.delete()
    

@psycho.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    text = START_TEXT.format(update.from_user.mention)
    reply_markup = START_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=False,
        quote=True,
        reply_markup=reply_markup
    )

@psycho.on_message(filters.private & filters.media)
async def getmedia(bot, update):
    medianame = DOWNLOAD_LOCATION + str(update.from_user.id)
    try:
        message = await update.reply(
            text="`Processing...`",
            quote=True,
            disable_web_page_preview=True
        )
        await bot.download_media(
            message=update,
            file_name=medianame
        )
        response = upload_file(medianame)
        try:
            os.remove(medianame)
        except:
            pass
    except Exception as error:
        print(error)
        text=f"Error :- <code>{error}</code>"
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton('More Help', callback_data='help')
            ]]
        )
        await message.edit_text(
            text=text,
            disable_web_page_preview=True,
            reply_markup=reply_markup
        )
        return
    text=f"**Link :-** `https://telegra.ph{response[0]}`\n\n**Join :-** @Master_X_Updates"
    reply_markup=InlineKeyboardMarkup(
        [[
        InlineKeyboardButton(text="Open Link", url=f"https://telegra.ph{response[0]}"),
        InlineKeyboardButton(text="Share Link", url=f"https://telegram.me/share/url?url=https://telegra.ph{response[0]}")
        ],[
        InlineKeyboardButton(text="Join Updates Channel", url="https://telegram.me/Master_X_Updates")
        ]]
    )
    await message.edit_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

psycho.run()

# © @Master_X_Updates # 

