from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"Salam, bu musiqi köməkçisi xidmətidir .\n\n ❗️ Rules:\n   - Söhbətə icazə verilmir\n   - Spama icazə verilmir \n\n 👉 **USERBOT QRUPUNUZA QOŞULMAYACAQ QRUPU LINK VƏ İSTİFADƏÇİ DƏVƏT ETMƏYİN.**\n\n ⚠️ Əsas: Bura bir mesaj göndərirsinizsə, bu, admin mesajınızı görəcək və söhbətə qoşulacaq deməkdir\n    - Bu istifadəçini gizli qruplara əlavə etməyin.\n   - Şəxsi məlumatları burada paylaşmayın\n\n")
  return                        
