# @greyyvbss

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, bot
from userbot.events import cilik_cmd


@bot.on(cilik_cmd(outgoing=True, pattern=r"thanks(?: |$)(.*)"))
async def _(typew):
    await typew.edit("●▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬●\n"
                     "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄\n"
                     "╔══╦╗────╔╗─╔╗╔╗\n"
                     "╚╗╔╣╚╦═╦═╣╚╗║╚╝╠═╦╦╗\n"
                     "─║║║║║╬║║║╩║╚╗╔╣║║║║\n"
                     "─╚╝╚╩╩╩╩╩╩╩╝─╚╝╚═╩═╝\n"
                     "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄\n"
                     "●▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬●")


@bot.on(cilik_cmd(outgoing=True, pattern=r"malam(?: |$)(.*)"))
async def _(typew):
    await typew.edit("╔═╦═╦╗╔═╦══╦═╦══╗\n"
                     "║═╣═╣║║╬║║║║╬╠╗╔╝\n"
                     "╠═║═╣╚╣║║║║║║║║║\n"
                     "╚═╩═╩═╩╩╩╩╩╩╩╝╚╝\n\n"
                     "╔══╦═╦╗╔═╦══╗\n"
                     "║║║║╬║║║╬║║║║\n"
                     "║║║║║║╚╣║║║║║\n"
                     "╚╩╩╩╩╩═╩╩╩╩╩╝")


@bot.on(cilik_cmd(outgoing=True, pattern=r"rumah(?: |$)(.*)"))
async def _(typew):
    await typew.edit("**GAMBAR RUMAH**\n"
                     "╱◥◣\n"
                     "│∩ │◥███◣ ╱◥███◣\n"
                     "╱◥◣ ◥████◣▓∩▓│∩ ║\n"
                     "│╱◥█◣║∩∩∩ ║◥█▓ ▓█◣\n"
                     "││∩│ ▓ ║∩田│║▓ ▓ ▓∩ ║\n"
                     "๑۩๑๑۩๑๑ ۩๑๑۩๑▓๑۩๑๑۩๑")


@bot.on(cilik_cmd(outgoing=True, pattern=r"join(?: |$)(.*)"))
async def _(typew):
    await typew.edit("_/﹋\\_\n"
                     "(҂`_´)\n"
                     "<,︻╦╤─ ҉\n"
                     r"_/﹋\_"
                     "\n**ᴊᴏɪɴ ʟɪɴᴋ ᴅɪ ʙɪᴏ😡**")
    
    
@bot.on(cilik_cmd(outgoing=True, pattern=r"lari(?: |$)(.*)"))
async def _(typew):
    await typew.edit("──▄█▀█▄─────────██\n"
                     "▄████████▄───▄▀█▄▄▄▄\n"
                     "██▀▼▼▼▼▼─▄▀──█▄▄\n"
                     "█████▄▲▲▲─▄▄▄▀───▀▄\n"
                     "██████▀▀▀▀─▀────────▀▀\n"
                     " **LARI IPINN**\n")
    
    
@bot.on(cilik_cmd(outgoing=True, pattern=r"mobil(?: |$)(.*)"))
async def _(typew):
    await typew.edit("──────▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▌\n"
                     "───▄▄██▌█░░░░░░░░░░░░▐\n"
                     "▄▄▄▌▐██▌█░░░░░░░░░░░░▐\n"
                     "███████▌█▄▄▄▄▄▄▄▄▄▄▄▄▌\n"
                     "▀❍▀▀▀▀▀▀▀❍❍▀▀▀▀▀▀❍❍▀\n")
    
      
CMD_HELP.update(
    {
        "animasi5": f"**Plugin : **`animasi5`\
        \n\n  •  **Syntax :** `{cmd}thanks`\
        \n  •  **Function : **Mengirim Gambar Thank You.\
        \n\n  •  **Syntax :** `{cmd}malam`\
        \n  •  **Function : **Mengirim Gambar Selamat Malam.\
        \n\n  •  **Syntax :** `{cmd}rumah`\
        \n  •  **Function : **Mengirim Gambar Rumah.\
        \n\n  •  **Syntax :** `{cmd}join`\
        \n  •  **Function : **Mengirim Gambar Join Link Di Bio.\
        \n\n  •  **Syntax :** `{cmd}lari`\
        \n  •  **Function : **Mengirim Gambar Lari Ipin.\
        \n\n  •  **Syntax :** `{cmd}mobil`\
        \n  •  **Function : **Mengirim Gambar Mobil Optimus.\
    "
    }
)
