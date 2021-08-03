from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_USERNAME


@Client.on_message(filters.command(["start", "start@HypeMuzikBot"]) & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        text="**Salam 👋🏻 {}!**\n\nI **Mən Telegram Qruplarının Səsli Söhbətlərində Musiqi İfa Edirəm. ** Məni qrupa əlavə zaman vaxtını xoş gələ bilərsən.**\n\n** /cmdlist İstifadəm haqqında daha çox kömək üçün toxun ❤**".format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton("➕ Qrupa əlavə et ➕", url="https://t.me/HypeMuzikBot?startgroup=true")
            ],[
            InlineKeyboardButton("💬 Qrup", url="https://t.me/HypeGroupAz"),
            InlineKeyboardButton("Kanal 🔊", url="https://t.me/HypeMusicAz")
            ],[
            InlineKeyboardButton("Komandalar 🛠", url="https://telegra.ph/Music-Bot-05-07")
            ]]
        ),
        disable_web_page_preview=True
    )
        
@Client.on_message(filters.command(["start", "start@HypeMuzikBot"]) & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        text="**Musiqi Botu Onlayndır ✅**",
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton(text="🎙️ Köməkçi Admin 🎙️", url="https://t.me/parvzh")
            ]]
        )
    )


@Client.on_message(filters.command(["cmdlist", "start@HypeMuzikBot"]) & filters.private & ~filters.channel)
async def cmdlist(_, message: Message):
    await message.reply_text(
        text="""**Hype Music Bot : Yardım Menyusu**

__× Əvvəlcə məni qrupunuza əlavə edin..
× Məni bütün icazələrlə qrupunuzda admin olaraq tanıdın..__

**🏷 Ümumi əmrlər.**

• `/play` - Musiqi adı : __Youtube vasitəsilə oynayır__
• `/dplay` - Musiqi adı : __Deezer vasitəsi ilə oynayır__
• `/splay` - Musiqi adı : __Saavn vasitəsi ilə oynayır__
• `/playlist` - __Playlisti göstərin__
• `/current` - __Oxuyan musiqini göstərin__

• `/song` - Song Name : __Mahnını YouTube -dan alın__
• `/vid` - Video Name : __Videonu YouTube -dan alın__
