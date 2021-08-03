from callsmusic.callsmusic import client as USER
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
import config
from config import BOT_USERNAME
from pyrogram.errors import UserAlreadyParticipant
from helpers.decorators import errors, authorized_users_only

@Client.on_message(filters.group & filters.command(["userbotjoin"]))
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>Məni əvvəlcə qrupda admin olaraq əlavə edin</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name =  "Music"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id,"İstədiyiniz kimi bura qatıldım")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>Köməkçi bot artıq söhbətinizdədir.</b>",
        )
        pass
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🛑 Flood Wait Error 🛑 \n İstifadəçi {user.first_name} userbot üçün ağır qoşulma istəklərinə görə qrupunuza qoşula bilmədi! İstifadəçinin qrupda qadağan edilmədiyinə əmin olun."
            f"\n\ya da əl ilə qrupunuza əlavə edin və yenidən cəhd edin</b>",
        )
        return
    await message.reply_text(
            "<b>köməkçi userbot söhbətinizə qoşuldu</b>",
        )
    
@USER.on_message(filters.group & filters.command(["userbotleave"]))
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:  
