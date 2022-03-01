import asyncio
from pyrogram import Client, filters
from pyrogram.types import Dialog, Chat, Message
from pyrogram.errors import UserAlreadyParticipant
from Music.config Import OWNER_ID
from Music.MusicUtilities.tgcallsrun import ASS_ACC as USER



@Client.on_message(filters.command("broadcast") & filters.user(OWNER_ID) & ~filter.edited)
async def gcast(_, message: Message):
    if not message.reply_to_message:
        pass
    else :
        x = message.reply_to_message.message_id   
        y = message.chat.id
        sent = 0
        pin = 0
        chats = []
        schats = await get_served_chats()
        for chat in schats:
            chats.append(int(chat["chat_id"]))
        for i in chats:
            try:
                m = await app.forward_messages(i, y, x)
                try:
                    await m.pin(disable_notification=False)
                    pin += 1
                except Exception:
                    pass
                await asyncio.sleep(.3)
                sent += 1
            except Exception:
                pass
        await message.reply_text(f"✅ **Pesan yang disiarkan di {sent} obrolan\n\n📌 dengan {pin} pin.**")  
        return
    if len(message.command) < 2:
        await message.reply_text("**Penggunaan**:\n/broadcast (message)")
        return  
    text = message.text.split(None, 1)[1]
    sent = 0
    pin = 0
    chats = []
    schats = await get_served_chats()
    for chat in schats:
        chats.append(int(chat["chat_id"]))
    for i in chats:
        try:
            m = await app.send_message(i, text=text)
            try:
                await m.pin(disable_notification=False)
                pin += 1
            except Exception:
                pass
            await asyncio.sleep(.3)
            sent += 1
        except Exception:
            pass
    await message.reply_text(f"✅ **Pesan yang disiarkan di {sent} obrolan\n📌 dengan {pin} pin.**")


@app.on_message(filters.command("broadcast") & filters.user(OWNER))
async def broadcast_message_nopin(_, message):
    if not message.reply_to_message:
        pass
    else:
        x = message.reply_to_message.message_id
        y = message.chat.id
        sent = 0
        chats = []
        schats = await get_served_chats()
        for chat in schats:
            chats.append(int(chat["chat_id"]))
        for i in chats:
            try:
                m = await app.forward_messages(i, y, x)
                await asyncio.sleep(0.3)
                sent += 1
            except Exception:
                pass
        await message.reply_text(f"✅ **Pesan yang disiarkan dalam {sent} obrolan")
        return
    if len(message.command) < 2:
        await message.reply_text(
            "**usage**:\n/broadcast (message)"
        )
        return
    text = message.text.split(None, 1)[1]
    sent = 0
    chats = []
    schats = await get_served_chats()
    for chat in schats:
        chats.append(int(chat["chat_id"]))
    for i in chats:
        try:
            m = await app.send_message(i, text=text)
            await asyncio.sleep(0.3)
            sent += 1
        except Exception:
            pass
    await message.reply_text(f"✅ **Pesan yang disiarkan dalam {sent} obrolan")
