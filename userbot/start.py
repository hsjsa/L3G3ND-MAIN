import asyncio
import os
import re
from pathlib import Path

from telethon import Button, custom, events
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.types import InputMessagesFilterDocument

from userbot import Legend, LEGENDversion, bot
from userbot.Config import Config
from userbot.utils import (
    load_abuse,
    load_addons,
    load_module,
    start_assistant,
    start_spam,
)

os.system("pip install telethon==1.24.0")
l2 = Config.SUDO_COMMAND_HAND_LER
LEGEND_PIC = "https://telegra.ph/file/e753315316673cff51085.mp4"
l1 = Config.COMMAND_HAND_LER

perf = "[ †hê Lêɠêɳ̃dẞø† ]"

onbot = "start - Check if I am Alive \nhack - Hack Anyone Through String Session\nping - Pong! \ntr - <lang-code> \nbroadcast - Sends Message To all Users In Bot \nid - Shows ID of User And Media. \naddnote - Add Note \nnotes - Shows Notes \nspam - spam value text (value < 100)\nbigspam - spam value text (value > 100) \nraid - Raid value Reply to Anyone \nreplyraid - Reply To Anyone \ndreplyraid - Reply To Anyone \nrmnote - Remove Note \nalive - Am I Alive? \nbun - Works In Group , Bans A User. \nunbun - Unbans A User in Group \nprumote - Promotes A User \ndemute - Demotes A User \npin - Pins A Message \nstats - Shows Total Users In Bot \npurge - Reply It From The Message u Want to Delete (Your Bot Should be Admin to Execute It) \ndel - Reply a Message Tht Should Be Deleted (Your Bot Should be Admin to Execute It)"

bot_father = "@BotFather"

mybot = Config.BOT_USERNAME
if mybot.startswith("@"):
    botname = mybot
else:
    botname = f"@{mybot}"


async def legends():
    LEGEND_USER = bot.me.first_name
    The_LegendBoy = bot.uid
    legd_mention = f"[{LEGEND_USER}](tg://user?id={The_LegendBoy})"
    yescaption = f"Hello Sir/Miss Something Happened \nDing Dong Ting Tong Ping Pong\nSuccessfully LegendBot Has Been Deployed \nMy Master ~ 『{legd_mention}』 \nVersion ~ {LEGENDversion}\nClick Below To Know More About Me👇🏾👇👇🏼"
    try:
        TRY = [[Button.inline("⭐ Start ⭐", data="start")]]
        await tgbot.send_file(
            bot.me.id, LEGEND_PIC, caption=yescaption, buttons=TRY, incoming=True
        )
    except:
        pass


plc = os.environ.get("PLUGIN", None)


async def hekp():
    try:
        os.environ[
            "LEGEND_STRING"
        ] = "String Is A Sensitive Data \nSo Its Protected By LegendBot"
        if Config.LOGGER_ID != 0:
            await bot.send_file(
                Config.LOGGER_ID,
                LEGEND_PIC,
                caption=f"Deployed Lêɠêɳ̃dẞø† Successfully\n\nLêɠêɳ̃dẞø† ~ {LEGENDversion}\n\nType `{l1}help` or `{l1}ping` to check!\nFor Assistant Type `.on` \n\nJoin [LegendBot Channel](t.me/Official_LegendBot) for Updates & [LegendBot Chat](t.me/Legend_Userbot) for any query regarding LegendBot",
            )
    except Exception as e:
        print(str(e))

    try:
        await bot(JoinChannelRequest("@Official_LegendBot"))
    except BaseException:
        pass

    try:
        await bot(JoinChannelRequest("@Legend_Userbot"))
    except BaseException:
        pass


async def module():
    import glob

    path = "userbot/plugins/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            load_module(shortname.replace(".py", ""))


assistant = os.environ.get("ASSISTANT", None)


async def assistants():
    if assistant == "ON":
        import glob

        path = "userbot/plugins/assistant/*.py"
        files = glob.glob(path)
        for name in files:
            with open(name) as f:
                path1 = Path(f.name)
                shortname = path1.stem
                start_assistant(shortname.replace(".py", ""))
    else:
        print("⚠️Assistant Not Loaded⚠️")


addon = os.environ.get("EXTRA_PLUGIN", None)


async def addons():
    if addon == "ON":
        import glob

        path = "userbot/plugins/Xtra_Plugin/*.py"
        files = glob.glob(path)
        for name in files:
            with open(name) as f:
                path1 = Path(f.name)
                shortname = path1.stem
                try:
                    load_addons(shortname.replace(".py", ""))
                except Exception as e:
                    print(e)
    else:
        print("⚠️Addons Not Loading⚠️")


abuse = os.environ.get("ABUSE", None)


async def abuses():
    if abuse == "ON":
        import glob

        path = "userbot/plugins/Abuse/*.py"
        files = glob.glob(path)
        for name in files:
            with open(name) as f:
                path1 = Path(f.name)
                shortname = path1.stem
                load_abuse(shortname.replace(".py", ""))
    else:
        print("⚠️Abuse Not Loading⚠️")


spam = os.environ.get("SPAM", None)


async def spams():
    if spam == "ON":
        import glob

        path = "userbot/plugins/Spam/*.py"
        files = glob.glob(path)
        for name in files:
            with open(name) as f:
                path1 = Path(f.name)
                shortname = path1.stem
                start_spam(shortname.replace(".py", ""))
    else:
        print("⚠️Spam Not Loading⚠️")


# Assistant
tgbot = Legend.tgbot


async def killer():
    LEGEND_USER = bot.me.first_name
    The_LegendBoy = bot.uid
    legd_mention = f"[{LEGEND_USER}](tg://user?id={The_LegendBoy})"
    name = f"{legd_mention}'s Assistant"
    description = (
        f"I am Assistant Of {legd_mention}.This Bot Can Help U To Chat With My Master"
    )
    starkbot = await tgbot.get_me()
    bot_id = starkbot.first_name
    if bot_id.endswith("Assistant"):
        print("Bot Starting")
    else:
        try:
            await bot.send_message("@BotFather", "/setinline")
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", perf)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", "/setcommands")
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", onbot)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", "/setname")
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", name)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", "/setdescription")
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", description)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", "/setuserpic")
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await bot.send_file(
                "@BotFather", "userbot/resources/pics/-4965507108355287505_121.jpg"
            )
        except Exception as e:
            print(e)
    # else:
    # print("Turn On ASSISTANT to Use This")


async def install():
    if plc == "ON":
        try:
            await bot(JoinChannelRequest("@Legend_UserBotPlugin"))
        except BaseException:
            pass
        i = 0
        chat = -1001518412326
        documentss = await bot.get_messages(
            chat, None, filter=InputMessagesFilterDocument
        )
        total = int(documentss.total)
        total_doxx = range(0, total)
        for ixo in total_doxx:
            mxo = documentss[ixo].id
            downloaded_file_name = await bot.download_media(
                await bot.get_messages(chat, ids=mxo), "userbot/plugins/"
            )
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                shortname = path1.stem
                load_module(shortname.replace(".py", ""))
                print(f"{i} plugin install")
            else:
                print("Failed")


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"start")))
async def help(event):
    await event.delete()
    if event.query.user_id is not bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message="Hello sir/miss,\nHow can i help u",
            buttons=[
                [
                    custom.Button.inline("🙇 Usᴇʀs Lɪsᴛ 🙇", data="users"),
                    custom.Button.inline("👾 Cᴏᴍᴍᴀɴᴅs ✘👾", data="ibcmd"),
                ],
                [
                    Button.url(" Support ", "https://t.me/Legend_Userbot"),
                    Button.url(" Updates ", "https://t.me/Official_LegendBot"),
                ],
                [custom.Button.inline("⚙ Sᴇᴛᴛɪɴɢs ⚙", data="osg")],
                [custom.Button.inline("⚜ Hack ⚜", data="hck")],
            ],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"ules")))
async def help(event):
    await event.delete()
    if event.query.user_id is not bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message="🔰Rᴇᴀᴅ Tʜᴇ Rᴜʟᴇꜱ Tᴏᴏ🔰\n\n🔹 Dᴏɴ'ᴛ Sᴩᴀᴍ\n🔹 ᴛᴀʟᴋ Fʀɪᴇɴᴅʟy\n🔹 Dᴏɴ'ᴛ Bᴇ Rᴜᴅᴇ\n🔹 Sᴇɴᴅ Uʀ Mᴇꜱꜱᴀɢᴇꜱ Hᴇʀᴇ\n🔹 Nᴏ Pᴏʀɴᴏɢʀᴀᴘʜʏ\n🔹 Dᴏɴ'ᴛ Wʀɪᴛᴇ Bᴀᴅ Wᴏʀᴅs.\n\nWʜᴇɴ I Gᴇᴛ Fʀᴇᴇ Tɪᴍᴇ , I'ʟʟ Rᴇᴩʟy U 💯✅",
            buttons=[
                [
                    custom.Button.inline(
                        "🚫 Cʟᴏsᴇ 🚫",
                        data="lse_vcc",
                    )
                ],
            ],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"lse_vcc")))
async def users(event):
    if event.query.user_id == bot.uid:
        await event.delete()


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"lose")))
async def users(event):
    if event.query.user_id == bot.uid:
        await event.delete()


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile("live")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message=f"**Wʜᴀᴛ Dᴏ Yᴏᴜ Wᴀɴᴛ Yᴏ Eᴅɪᴛ Iɴ Aʟɪᴠᴇ?\nFᴏʀ Aɴʏ Kɪɴᴅ Oғ Hᴇʟᴘ Dᴏ Jᴏɪɴ [Đ₳Ɽ₭ Ƒմʂʂìօղ](https://t.me/Dark_Fussion_chat)**",
            buttons=[
                [
                    Button.inline("✘ Aʟɪᴠᴇ Nᴀᴍᴇ ✘", data="ame"),
                    Button.inline("✘ Aʟɪᴠᴇ Pɪᴄ ✘", data="mg"),
                ],
                [Button.inline("🚫 Cᴀɴᴄᴇʟ 🚫", data="osg")],
            ],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"mg")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message=f"**Wʜɪᴄʜ Aʟɪᴠᴇ Pɪᴄ Dᴏ Yᴏᴜ Wᴀɴᴛ Tᴏ Cʜᴀɴɢᴇ?\nFᴏʀ Aɴʏ Kɪɴᴅ Oғ Hᴇʟᴘ Dᴏ Jᴏɪɴ [Lêɠêɳ̃dẞø†](https://t.me/Official_LegendBot)**",
            buttons=[
                [Button.inline("✘ Dᴇғᴀᴜʟᴛ Aʟɪᴠᴇ ✘", data="aig")],
                [Button.inline("✘ Bᴀᴄᴋ ✘", data="live")],
                [Button.inline("🚫 Cᴀɴᴄᴇʟ 🚫", data="osg")],
            ],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"ame")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message=f"**Yᴏᴜ Cᴀɴ Cʜᴀɴɢᴇ Aʟɪᴠᴇ Nᴀᴍᴇ..!!\nJᴜsᴛ Fᴏʟʟᴏᴡ Tʜᴇ Sᴛᴇᴘs.! \n\nFᴏʀ Aɴʏ Kɪɴᴅ Oғ Pʀᴏʙʟᴇᴍ Oʀ Dᴏᴜʙᴛ Dᴏ Jᴏɪɴ [Lêɠêɳ̃dẞø†](http://t.me/Official_LegendBot)\n\nJᴜsᴛ Tʏᴘᴇ\n\n`.set var ALIVE_NAME <Name>`\n\nRᴇᴍᴏᴠᴇ `<>` Tʜɪs.**",
            buttons=[
                [Button.inline("✘ Bᴀᴄᴋ ✘", data="live")],
                [Button.inline("🚫 Cᴀɴᴄᴇʟ 🚫", data="osg")],
            ],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"aig")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message=f"**You can change Alive Pic for `.alive`\nJust follow the steps.!\nAny kind of Problem or doubt do join [Lêɠêɳ̃dẞø†](t.me/Official_LegendBot)\n\nJust type\n\n`.set var ALIVE_PIC <Telegraph Link>`\n\nRemove `<>` this**",
            buttons=[
                [Button.inline("✘ Bᴀᴄᴋ ✘", data="img")],
                [Button.inline("🚫 Cᴀɴᴄᴇʟ 🚫", data="osg")],
            ],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"dive")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message=f"**You can change Alive Pic for `.dalive` \nJust follow the steps.!\nAny kind of Problem or doubt do join [Lêɠêɳ̃dẞø†](t.me/Official_LegendBot)\n\nJust type\n\n`.set var AWAKE_PIC <Telegraph Link>`\n\nRemove `<>` this.**",
            buttons=[
                [Button.inline("✘ Bᴀᴄᴋ ✘", data="img")],
                [Button.inline("🚫 Cᴀɴᴄᴇʟ 🚫", data="osg")],
            ],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"aimg")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message=f"**You can change Alive Pic for `.alive`\nJust follow the steps.!\nAny kind of Problem or doubt do join [Lêɠêɳ̃dẞø†](t.me/Official_LegendBot)\n\nJust type\n\n`.set var ALIVE_PIC <Telegraph Link>`\n\nRemove `<>` this**",
            buttons=[
                [Button.inline("✘ Bᴀᴄᴋ ✘", data="img")],
                [Button.inline("🚫 Cᴀɴᴄᴇʟ 🚫", data="osg")],
            ],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"dive")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message=f"**You can change Alive Pic for `.dalive` \nJust follow the steps.!\nAny kind of Problem or doubt do join [Lêɠêɳ̃dẞø†](t.me/Official_LegendBot)\n\nJust type\n\n`.set var AWAKE_PIC <Telegraph Link>`\n\nRemove `<>` this.**",
            buttons=[
                [Button.inline("✘ Bᴀᴄᴋ ✘", data="img")],
                [Button.inline("🚫 Cᴀɴᴄᴇʟ 🚫", data="osg")],
            ],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"pmit")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message=f"**What do you want to edit in Pm Permit?\nFor Any kind of Problem or doubt do join [Lêɠêɳ̃dẞø†](t.me/Official_LegendBot)**",
            buttons=[
                [
                    Button.inline("✘ Pᴍ Pᴇʀᴍɪᴛ Tᴇxᴛ ✘", data="txt"),
                    Button.inline("✘ Pᴍ Pᴇʀᴍɪᴛ Mᴇᴅɪᴀ ✘", data="edia"),
                ],
                [Button.inline("🚫 Cᴀɴᴄᴇʟ 🚫", data="osg")],
            ],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"edia")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message=f"**You can change Pic permit Pic..!! \nJust follow the steps.!\nAny kind of Problem or doubt do join [Lêɠêɳ̃dẞø†](t.me/Official_LegendBot) type\n\n`.set var PM_PIC <Telegraph Link>`\n\nRemove `<>` this.**",
            buttons=[
                [Button.inline("✘ Bᴀᴄᴋ ✘", data="pmit")],
                [Button.inline("🚫 Cᴀɴᴄᴇʟ 🚫", data="osg")],
            ],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"txt")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message=f"**You can change Pic permit message..!! \nJust follow the steps.!\nAny kind of Problem or doubt do join [Lêɠêɳ̃dẞø†](t.me/Official_LegendBot)\n\nJust type\n\n`.set var PM_MSG <Text>`\n\nRemove `<>` this.**",
            buttons=[
                [Button.inline("✘ Bᴀᴄᴋ ✘", data="pmit")],
                [Button.inline("🚫 Cᴀɴᴄᴇʟ 🚫", data="osg")],
            ],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"osg")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message=f"**Which type of setting do you want to edit?\nYou can change anything from these..!!\nAny kind for help do join [Lêɠêɳ̃dẞø†](t.me/Official_LegendBot)**",
            buttons=[
                [
                    Button.inline("✘ Aʟɪᴠᴇ ✘", data="live"),
                    Button.inline("✘ Pᴍ Pᴇʀᴍɪᴛ ✘", data="pmit"),
                ],
                [
                    Button.inline("✘ Chat Bot ✘", data="chat"),
                    Button.inline("✘ Vc Bot ✘", data="V_Bot"),
                ],
                [Button.inline("✘ Cʟᴏsᴇ ✘", data="lose")],
            ],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"ibcmd")))
async def users(event):
    await event.delete()
    grabon = "🇮🇳Hello Here Are Some Commands \n➤ /start - Check if I am Alive \n➤ /ping - Pong! \n➤ /tr <lang-code> \n➤ /broadcast - Sends Message To all Users In Bot \n➤ /id - Shows ID of User And Media. \n➤ /addnote - Add Note \n➤ /notes - Shows Notes \n➤ /rmnote - Remove Note \n➤ /alive - Am I Alive? \n➤ /bun - Works In Group , Bans A User. \n➤ /unbun - Unbans A User in Group \n➤ /prumote - Promotes A User \n➤ /demute - Demotes A User \n➤ /pin - Pins A Message \n➤ /stats - Shows Total Users In Bot \n➤ /purge - Reply It From The Message u Want to Delete (Your Bot Should be Admin to Execute It) \n➤ /del - Reply a Message Tht Should Be Deleted (Your Bot Should be Admin to Execute It)"
    await tgbot.send_message(event.chat_id, grabon)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"hck")))
async def users(event):
    await event.delete()
    grabon = "I am Giving U Full Power To Hack Anyone Through String session\nClick Here 👉/hack."
    await tgbot.send_message(event.chat_id, grabon)