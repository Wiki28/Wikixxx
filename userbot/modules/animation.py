import asyncio
from time import sleep

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, bot
from userbot.events import wiki_cmd
from userbot.utils import edit_or_reply
from userbot import ALIVE_NAME


@bot.on(wiki_cmd(pattern=r"(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    input_str = event.pattern_match.group(1)

    if input_str == "bulan":

        await event.edit(input_str)

        animation_chars = [
            "🌗",
            "🌘",
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖",
            "🌗",
            "🌘",
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖",
            "🌗",
            "🌘",
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖",
            "🌗",
            "🌘",
            "🌑",
            "🌒",
            "🌓",
            "🌔",
            "🌕",
            "🌖",
        ]

        animation_interval = 0.1

        animation_ttl = range(117)

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 32])


@bot.on(wiki_cmd(outgoing=True, pattern=r"sayang$"))
async def _(e):
    await e.edit("I LOVEE YOUUU 💕")
    await e.edit("💝💘💓💗")
    await e.edit("💞💕💗💘")
    await e.edit("💝💘💓💗")
    await e.edit("💞💕💗💘")
    await e.edit("💘💞💗💕")
    await e.edit("💘💞💕💗")
    await e.edit("SAYANG KAMU 💝💖💘")
    await e.edit("💝💘💓💗")
    await e.edit("💞💕💗💘")
    await e.edit("💘💞💕💗")
    await e.edit("SAYANG")
    await e.edit("KAMU")
    await e.edit("SELAMANYA 💕")
    await e.edit("💘💘💘💘")
    await e.edit("SAYANG")
    await e.edit("KAMU")
    await e.edit("SAYANG")
    await e.edit("KAMU")
    await e.edit("I LOVE YOUUUU")
    await e.edit("MY BABY")
    await e.edit("💕💞💘💝")
    await e.edit("💘💕💞💝")
    await e.edit("SAYANG KAMU💞")


@bot.on(wiki_cmd(outgoing=True, pattern=r"dino(?: |$)(.*)"))
async def _(typew):
    await typew.edit("`DIN DINNN.....`")
    sleep(1)
    await typew.edit("`DINOOOOSAURUSSSSS!!`")
    sleep(1)
    await typew.edit("`🏃                        🦖`")
    await typew.edit("`🏃                       🦖`")
    await typew.edit("`🏃                      🦖`")
    await typew.edit("`🏃                     🦖`")
    await typew.edit("`🏃   `LARII`          🦖`")
    await typew.edit("`🏃                   🦖`")
    await typew.edit("`🏃                  🦖`")
    await typew.edit("`🏃                 🦖`")
    await typew.edit("`🏃                🦖`")
    await typew.edit("`🏃               🦖`")
    await typew.edit("`🏃              🦖`")
    await typew.edit("`🏃             🦖`")
    await typew.edit("`🏃            🦖`")
    await typew.edit("`🏃           🦖`")
    await typew.edit("`🏃WOARGH!   🦖`")
    await typew.edit("`🏃           🦖`")
    await typew.edit("`🏃            🦖`")
    await typew.edit("`🏃             🦖`")
    await typew.edit("`🏃              🦖`")
    await typew.edit("`🏃               🦖`")
    await typew.edit("`🏃                🦖`")
    await typew.edit("`🏃                 🦖`")
    await typew.edit("`🏃                  🦖`")
    await typew.edit("`🏃                   🦖`")
    await typew.edit("`🏃                    🦖`")
    await typew.edit("`🏃                     🦖`")
    await typew.edit("`🏃  Huh-Huh           🦖`")
    await typew.edit("`🏃                   🦖`")
    await typew.edit("`🏃                  🦖`")
    await typew.edit("`🏃                 🦖`")
    await typew.edit("`🏃                🦖`")
    await typew.edit("`🏃               🦖`")
    await typew.edit("`🏃              🦖`")
    await typew.edit("`🏃             🦖`")
    await typew.edit("`🏃            🦖`")
    await typew.edit("`🏃           🦖`")
    await typew.edit("`🏃          🦖`")
    await typew.edit("`🏃         🦖`")
    await typew.edit("`DIA SEMAKIN MENDEKAT!!!`")
    sleep(1)
    await typew.edit("`🏃       🦖`")
    await typew.edit("`🏃      🦖`")
    await typew.edit("`🏃     🦖`")
    await typew.edit("`🏃    🦖`")
    await typew.edit("`Dahlah Pasrah Aja`")
    sleep(1)
    await typew.edit("`🧎🦖`")
    sleep(2)
    await typew.edit("`-TAMAT-`")


@bot.on(wiki_cmd(outgoing=True, pattern=r"gabut$"))
async def _(e):
    await e.edit("`PERNAAHHHHH KAHHH KAUUU MENGIRA`")
    await e.edit("`SEPEEERTIIIII APAAAA BENTUKKKKKKK CINTAAAA`")
    await e.edit("`RAMBUUUT WARNAAA WARNII`")
    await e.edit("`BAGAI GULALI`")
    await e.edit("`IMUUUTTTTT LUCUUU`")
    await e.edit("`WALAAUUUU TAK TERLALU TINGGI`")
    await e.edit("`GW GABUUTTTT`")
    await e.edit("`EMMMM BACOTNYA`")
    await e.edit("`GABUTTTT WOI GABUT`")
    await e.edit("🙈🙈🙈🙈")
    await e.edit("🙉🙉🙉🙉")
    await e.edit("🙈🙈🙈🙈")
    await e.edit("🙉🙉🙉🙉")
    await e.edit("`CILUUUKKK BAAAAA`")
    await e.edit("🙉🙉🙉🙉")
    await e.edit("🐢                       🚶")
    await e.edit("🐢                      🚶")
    await e.edit("🐢                     🚶")
    await e.edit("🐢                    🚶")
    await e.edit("🐢                   🚶")
    await e.edit("🐢                  🚶")
    await e.edit("🐢                 🚶")
    await e.edit("🐢                🚶")
    await e.edit("🐢               🚶")
    await e.edit("🐢              🚶")
    await e.edit("🐢             🚶")
    await e.edit("🐢            🚶")
    await e.edit("🐢           🚶")
    await e.edit("🐢          🚶")
    await e.edit("🐢         🚶")
    await e.edit("🐢        🚶")
    await e.edit("🐢       🚶")
    await e.edit("🐢      🚶")
    await e.edit("🐢     🚶")
    await e.edit("🐢    🚶")
    await e.edit("🐢   🚶")
    await e.edit("🐢  🚶")
    await e.edit("🐢 🚶")
    await e.edit("🐢🚶")
    await e.edit("🚶🐢")
    await e.edit("🚶 🐢")
    await e.edit("🚶  🐢")
    await e.edit("🚶   🐢")
    await e.edit("🚶    🐢")
    await e.edit("🚶     🐢")
    await e.edit("🚶      🐢")
    await e.edit("🚶       🐢")
    await e.edit("🚶        🐢")
    await e.edit("🚶         🐢")
    await e.edit("🚶          🐢")
    await e.edit("🚶           🐢")
    await e.edit("🚶            🐢")
    await e.edit("🚶             🐢")
    await e.edit("🚶              🐢")
    await e.edit("🚶               🐢")
    await e.edit("🚶                🐢")
    await e.edit("🚶                 🐢")
    await e.edit("🚶                  🐢")
    await e.edit("🚶                   🐢")
    await e.edit("🚶                    🐢")
    await e.edit("🚶                     🐢")
    await e.edit("🚶                      🐢")
    await e.edit("🚶                       🐢")
    await e.edit("🚶                        🐢")
    await e.edit("🚶                         🐢")
    await e.edit("🚶                          🐢")
    await e.edit("🚶                           🐢")
    await e.edit("🚶                            🐢")
    await e.edit("🚶                             🐢")
    await e.edit("🚶                              🐢")
    await e.edit("🚶                               🐢")
    await e.edit("🚶                                🐢")
    await e.edit("🚶                                 🐢")
    await e.edit("`AHHH MANTAP`")
    await e.edit("🙉")
    await e.edit("🙈")
    await e.edit("🙉")
    await e.edit("🙈")
    await e.edit("🙉")
    await e.edit("😂")
    await e.edit("🐢                       🚶")
    await e.edit("🐢                      🚶")
    await e.edit("🐢                     🚶")
    await e.edit("🐢                    🚶")
    await e.edit("🐢                   🚶")
    await e.edit("🐢                  🚶")
    await e.edit("🐢                 🚶")
    await e.edit("🐢                🚶")
    await e.edit("🐢               🚶")
    await e.edit("🐢              🚶")
    await e.edit("🐢             🚶")
    await e.edit("🐢            🚶")
    await e.edit("🐢           🚶")
    await e.edit("🐢          🚶")
    await e.edit("🐢         🚶")
    await e.edit("🐢        🚶")
    await e.edit("🐢       🚶")
    await e.edit("🐢      🚶")
    await e.edit("🐢     🚶")
    await e.edit("🐢    🚶")
    await e.edit("🐢   🚶")
    await e.edit("🐢  🚶")
    await e.edit("🐢 🚶")
    await e.edit("🐢🚶")
    await e.edit("🚶🐢")
    await e.edit("🚶 🐢")
    await e.edit("🚶  🐢")
    await e.edit("🚶   🐢")
    await e.edit("🚶    🐢")
    await e.edit("🚶     🐢")
    await e.edit("🚶      🐢")
    await e.edit("🚶       🐢")
    await e.edit("🚶        🐢")
    await e.edit("🚶         🐢")
    await e.edit("🚶          🐢")
    await e.edit("🚶           🐢")
    await e.edit("🚶            🐢")
    await e.edit("🚶             🐢")
    await e.edit("🚶              🐢")
    await e.edit("🚶               🐢")
    await e.edit("🚶                🐢")
    await e.edit("🚶                 🐢")
    await e.edit("🚶                  🐢")
    await e.edit("🚶                   🐢")
    await e.edit("🚶                    🐢")
    await e.edit("🚶                     🐢")
    await e.edit("🚶                      🐢")
    await e.edit("🚶                       🐢")
    await e.edit("🚶                        🐢")
    await e.edit("🚶                         🐢")
    await e.edit("🚶                          🐢")
    await e.edit("🚶                           🐢")
    await e.edit("🚶                            🐢")
    await e.edit("🚶                             🐢")
    await e.edit("🚶                              🐢")
    await e.edit("🚶                               🐢")
    await e.edit("🚶                                🐢")
    await e.edit("🐢                       🚶")
    await e.edit("🐢                      🚶")
    await e.edit("🐢                     🚶")
    await e.edit("🐢                    🚶")
    await e.edit("🐢                   🚶")
    await e.edit("🐢                  🚶")
    await e.edit("🐢                 🚶")
    await e.edit("🐢                🚶")
    await e.edit("🐢               🚶")
    await e.edit("🐢              🚶")
    await e.edit("🐢             🚶")
    await e.edit("🐢            🚶")
    await e.edit("🐢           🚶")
    await e.edit("🐢          🚶")
    await e.edit("🐢         🚶")
    await e.edit("🐢        🚶")
    await e.edit("🐢       🚶")
    await e.edit("🐢      🚶")
    await e.edit("🐢     🚶")
    await e.edit("🐢    🚶")
    await e.edit("🐢   🚶")
    await e.edit("🐢  🚶")
    await e.edit("🐢 🚶")
    await e.edit("🐢🚶")
    await e.edit("🚶🐢")
    await e.edit("🚶 🐢")
    await e.edit("🚶  🐢")
    await e.edit("🚶   🐢")
    await e.edit("🚶    🐢")
    await e.edit("🚶     🐢")
    await e.edit("🚶      🐢")
    await e.edit("🚶       🐢")
    await e.edit("🚶        🐢")
    await e.edit("🚶         🐢")
    await e.edit("🚶          🐢")
    await e.edit("🚶           🐢")
    await e.edit("🚶            🐢")
    await e.edit("🚶             🐢")
    await e.edit("🚶              🐢")
    await e.edit("🚶               🐢")
    await e.edit("🚶                🐢")
    await e.edit("🚶                 🐢")
    await e.edit("🚶                  🐢")
    await e.edit("🚶                   🐢")
    await e.edit("🚶                    🐢")
    await e.edit("🚶                     🐢")
    await e.edit("🚶                      🐢")
    await e.edit("🚶                       🐢")
    await e.edit("🚶                        🐢")
    await e.edit("🚶                         🐢")
    await e.edit("🚶                          🐢")
    await e.edit("🚶                           🐢")
    await e.edit("🚶                            🐢")
    await e.edit("🚶                             🐢")
    await e.edit("🚶                              🐢")
    await e.edit("🚶                               🐢")
    await e.edit("🚶                                🐢")
    await e.edit("🐢                       🚶")
    await e.edit("🐢                      🚶")
    await e.edit("🐢                     🚶")
    await e.edit("🐢                    🚶")
    await e.edit("🐢                   🚶")
    await e.edit("🐢                  🚶")
    await e.edit("🐢                 🚶")
    await e.edit("🐢                🚶")
    await e.edit("🐢               🚶")
    await e.edit("🐢              🚶")
    await e.edit("🐢             🚶")
    await e.edit("🐢            🚶")
    await e.edit("🐢           🚶")
    await e.edit("🐢          🚶")
    await e.edit("🐢         🚶")
    await e.edit("🐢        🚶")
    await e.edit("🐢       🚶")
    await e.edit("🐢      🚶")
    await e.edit("🐢     🚶")
    await e.edit("🐢    🚶")
    await e.edit("🐢   🚶")
    await e.edit("🐢  🚶")
    await e.edit("🐢 🚶")
    await e.edit("🐢🚶")
    await e.edit("🚶🐢")
    await e.edit("🚶 🐢")
    await e.edit("🚶  🐢")
    await e.edit("🚶   🐢")
    await e.edit("🚶    🐢")
    await e.edit("🚶     🐢")
    await e.edit("🚶      🐢")
    await e.edit("🚶       🐢")
    await e.edit("🚶        🐢")
    await e.edit("🚶         🐢")
    await e.edit("🚶          🐢")
    await e.edit("🚶           🐢")
    await e.edit("🚶            🐢")
    await e.edit("🚶             🐢")
    await e.edit("🚶              🐢")
    await e.edit("🚶               🐢")
    await e.edit("🚶                🐢")
    await e.edit("🚶                 🐢")
    await e.edit("🚶                  🐢")
    await e.edit("🚶                   🐢")
    await e.edit("🚶                    🐢")
    await e.edit("🚶                     🐢")
    await e.edit("🚶                      🐢")
    await e.edit("🚶                       🐢")
    await e.edit("🚶                        🐢")
    await e.edit("🚶                         🐢")
    await e.edit("🚶                          🐢")
    await e.edit("🚶                           🐢")
    await e.edit("🚶                            🐢")
    await e.edit("🚶                             🐢")
    await e.edit("🚶                              🐢")
    await e.edit("🚶                               🐢")
    await e.edit("🚶                                🐢")
    await e.edit("`GABUT`")


@bot.on(wiki_cmd(outgoing=True, pattern=r"terkadang(?: |$)(.*)"))
async def _(typew):
    await typew.edit("`Terkadang`")
    sleep(1)
    await typew.edit("`Mencintai Seseorang`")
    sleep(1)
    await typew.edit("`Hanya Akan Membuang Waktumu`")
    sleep(1)
    await typew.edit("`Ketika Waktumu Habis`")
    sleep(1)
    await typew.edit("`Tambah Aja 5000`")
    sleep(1)
    await typew.edit("`Bercanda`")


# Create by myself @localheart


@bot.on(wiki_cmd(outgoing=True, pattern=r"mf$"))
async def _(e):
    await e.edit("`mf g dl` **ミ(ノ;_ _)ノ=3** ")


@bot.on(wiki_cmd(pattern=r"(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    input_str = event.pattern_match.group(1)

    if input_str == "cinta":

        await event.edit(input_str)

        animation_chars = [
            "`Connecting Ke Server Cinta`",
            "`Mencari Target Cinta`",
            "`Mengirim Cintaku.. 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Mengirim Cintaku.. 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Mengirim Cintaku.. 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Mengirim Cintaku.. 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Mengirim Cintaku.. 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Mengirim Cintaku.. 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Mengirim Cintaku.. 84%\n█████████████████████▒▒▒▒ `",
            "`Mengirim Cintaku.. 100%\n█████████CINTAKU███████████ `",
            "`Cintaku Sekarang Sepenuhnya Terkirim Padamu, Dan Sekarang Aku Sangat Mencintai Mu, I Love You 💞`",
        ]

        animation_interval = 2

        animation_ttl = range(11)

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])


@bot.on(wiki_cmd(outgoing=True, pattern=r"gombal(?: |$)(.*)"))
async def _(typew):
    sleep(1)
    await typew.edit("`Hai, I LOVE YOU 💞`")
    sleep(1)
    await typew.edit("`I LOVE YOU SO MUCH!`")
    sleep(1)
    await typew.edit("`I NEED YOU!`")
    sleep(1)
    await typew.edit("`I WANT TO BE YOUR BOYFRIEND!`")
    sleep(1)
    await typew.edit("`I LOVEE YOUUUU💕💗`")
    sleep(1)
    await typew.edit("`I LOVEE YOUUUU💗💞`")
    sleep(1)
    await typew.edit("`I LOVEE YOUUUU💝💗`")
    sleep(1)
    await typew.edit("`I LOVEE YOUUUU💟💖`")
    sleep(1)
    await typew.edit("`I LOVEE YOUUUU💘💓`")
    sleep(1)
    await typew.edit("`Tapi Bo'ong`")


# Create by myself @localheart


@bot.on(wiki_cmd(outgoing=True, pattern=r"helikopter(?: |$)(.*)"))
async def _(typew):
    await typew.edit(
        "▬▬▬.◙.▬▬▬ \n"
        "═▂▄▄▓▄▄▂ \n"
        "◢◤ █▀▀████▄▄▄▄◢◤ \n"
        "█▄ █ █▄ ███▀▀▀▀▀▀▀╬ \n"
        "◥█████◤ \n"
        "══╩══╩══ \n"
        "╬═╬ \n"
        "╬═╬ \n"
        "╬═╬ \n"
        "╬═╬ \n"
        "╬═╬ \n"
        "╬═╬ \n"
        "╬═╬ Hallo Semuanya :) \n"
        "╬═╬☻/ \n"
        "╬═╬/▌ \n"
        "╬═╬/ \\ \n"
    )


@bot.on(wiki_cmd(outgoing=True, pattern=r"tembak(?: |$)(.*)"))
async def _(typew):
    await typew.edit(
        "_/﹋\\_\n" "(҂`_´)\n" "<,︻╦╤─ ҉\n" r"_/﹋\_" "\n**Mau Jadi Pacarku Gak?!**"
    )


@bot.on(wiki_cmd(outgoing=True, pattern=r"bundir(?: |$)(.*)"))
async def _(typew):
    await typew.edit(
        "`Dadah Semuanya...`          \n　　　　　|"
        "\n　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　／￣￣＼| \n"
        "＜ ´･ 　　 |＼ \n"
        "　|　３　 | 丶＼ \n"
        "＜ 、･　　|　　＼ \n"
        "　＼＿＿／∪ _ ∪) \n"
        "　　　　　 Ｕ Ｕ\n"
    )


@bot.on(wiki_cmd(outgoing=True, pattern=r"awk(?: |$)(.*)"))
async def _(typew):
    await typew.edit(
        "────██──────▀▀▀██\n"
        "──▄▀█▄▄▄─────▄▀█▄▄▄\n"
        "▄▀──█▄▄──────█─█▄▄\n"
        "─▄▄▄▀──▀▄───▄▄▄▀──▀▄\n"
        "─▀───────▀▀─▀───────▀▀\n`Awkwokwokwok..`"
    )


@bot.on(wiki_cmd(outgoing=True, pattern=r"ular(?: |$)(.*)"))
async def _(typew):
    await typew.edit(
        "░░░░▓\n"
        "░░░▓▓\n"
        "░░█▓▓█\n"
        "░██▓▓██\n"
        "░░██▓▓██\n"
        "░░░██▓▓██\n"
        "░░░░██▓▓██\n"
        "░░░░░██▓▓██\n"
        "░░░░██▓▓██\n"
        "░░░██▓▓██\n"
        "░░██▓▓██\n"
        "░██▓▓██\n"
        "░░██▓▓██\n"
        "░░░██▓▓██\n"
        "░░░░██▓▓██\n"
        "░░░░░██▓▓██\n"
        "░░░░██▓▓██\n"
        "░░░██▓▓██\n"
        "░░██▓▓██\n"
        "░██▓▓██\n"
        "░░██▓▓██\n"
        "░░░██▓▓██\n"
        "░░░░██▓▓██\n"
        "░░░░░██▓▓██\n"
        "░░░░██▓▓██\n"
        "░░░██▓▓██\n"
        "░░██▓▓██\n"
        "░██▓▓██\n"
        "░░██▓▓██\n"
        "░░░██▓▓██\n"
        "░░░░██▓▓██\n"
        "░░░░░██▓▓██\n"
        "░░░░██▓▓██\n"
        "░░░██▓▓██\n"
        "░░██▓▓██\n"
        "░██▓▓██\n"
        "░░██▓▓██\n"
        "░░░██▓▓██\n"
        "░░░░██▓▓██\n"
        "░░░░░██▓▓██\n"
        "░░░░██▓▓██\n"
        "░░░██▓▓██\n"
        "░░██▓▓██\n"
        "░██▓▓██\n"
        "░░██▓▓██\n"
        "░░░██▓▓██\n"
        "░░░░██▓▓██\n"
        "░░░░░██▓▓██\n"
        "░░░░██▓▓██\n"
        "░░░██▓▓██\n"
        "░░██▓▓██\n"
        "░██▓▓██\n"
        "░░██▓▓██\n"
        "░░░██▓▓██\n"
        "░░░░██▓▓██\n"
        "░░░░░██▓▓██\n"
        "░░░░██▓▓██\n"
        "░░░██▓▓██\n"
        "░░██▓▓██\n"
        "░██▓▓██\n"
        "░░██▓▓██\n"
        "░░░██▓▓██\n"
        "░░░░██▓▓██\n"
        "░░░░░██▓▓██\n"
        "░░░░██▓▓██\n"
        "░░░██▓▓██\n"
        "░░██▓▓██\n"
        "░░██▓▓██\n"
        "░░██▓▓██\n"
        "░░██▓▓██\n"
        "░░██▓▓██\n"
        "░░██▓▓██\n"
        "░░░██▓▓███\n"
        "░░░░██▓▓████\n"
        "░░░░░██▓▓█████\n"
        "░░░░░░██▓▓██████\n"
        "░░░░░░███▓▓███████\n"
        "░░░░░████▓▓████████\n"
        "░░░░█████▓▓█████████\n"
        "░░░█████░░░█████●███\n"
        "░░████░░░░░░░███████\n"
        "░░███░░░░░░░░░██████\n"
        "░░██░░░░░░░░░░░████\n"
        "░░░░░░░░░░░░░░░░███\n"
        "░░░░░░░░░░░░░░░░░░░\n"
    )


@bot.on(wiki_cmd(outgoing=True, pattern=r"sip(?: |$)(.*)"))
async def _(typew):
    await typew.edit(
        "‡‡‡‡‡‡‡‡‡‡‡‡▄▄▄▄\n"
        "‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█\n"
        "‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█\n"
        "‡‡‡‡‡‡‡‡‡‡█‡‡‡‡‡█\n"
        "‡‡‡‡‡‡‡‡‡█‡‡‡‡‡‡█\n"
        "██████▄▄█‡‡‡‡‡‡████████▄\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█████‡‡‡‡‡‡‡‡‡‡‡‡██\n"
        "█████‡‡‡‡‡‡‡██████████\n"
    )


@bot.on(wiki_cmd(outgoing=True, pattern=r"tank(?: |$)(.*)"))
async def _(typew):
    await typew.edit(
        "█۞███████]▄▄▄▄▄▄▄▄▄▄▃ \n"
        "▂▄▅█████████▅▄▃▂…\n"
        "[███████████████████]\n"
        "◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤\n"
    )


@bot.on(wiki_cmd(outgoing=True, pattern=r"babi(?: |$)(.*)"))
async def typewriter(typew):
    await typew.edit(
        "┈┈┏━╮╭━┓┈╭━━━━╮\n"
        "┈┈┃┏┗┛┓┃╭┫Ngok ┃\n"
        "┈┈╰┓▋▋┏╯╯╰━━━━╯\n"
        "┈╭━┻╮╲┗━━━━╮╭╮┈\n"
        "┈┃▎▎┃╲╲╲╲╲╲┣━╯┈\n"
        "┈╰━┳┻▅╯╲╲╲╲┃┈┈┈\n"
        "┈┈┈╰━┳┓┏┳┓┏╯┈┈┈\n"
        "┈┈┈┈┈┗┻┛┗┻┛┈┈┈┈\n"
    )


@bot.on(wiki_cmd(outgoing=True, pattern=r"ajg(?: |$)(.*)"))
async def _(typew):
    await typew.edit(
        "╥━━━━━━━━╭━━╮━━┳\n"
        "╢╭╮╭━━━━━┫┃▋▋━▅┣\n"
        "╢┃╰┫┈┈┈┈┈┃┃┈┈╰┫┣\n"
        "╢╰━┫┈┈┈┈┈╰╯╰┳━╯┣\n"
        "╢┊┊┃┏┳┳━━┓┏┳┫┊┊┣\n"
        "╨━━┗┛┗┛━━┗┛┗┛━━┻\n"
    )


@bot.on(wiki_cmd(outgoing=True, pattern=r"bernyanyi(?: |$)(.*)"))
async def _(typew):
    await typew.edit("**Ganteng Doang Gak Bernyanyi (ง˙o˙)ว**")
    sleep(2)
    await typew.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")
    sleep(1)
    await typew.edit("**♪┏(・o･)┛♪┗ ( ･o･) ┓**")
    sleep(1)
    await typew.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")
    sleep(1)
    await typew.edit("**♪┏(・o･)┛♪┗ ( ･o･) ┓**")
    sleep(1)
    await typew.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")
    sleep(1)
    await typew.edit("**♪┏(・o･)┛♪┗ ( ･o･) ┓**")
    sleep(1)
    await typew.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")
    sleep(1)
    await typew.edit("**♪┏(・o･)┛♪┗ ( ･o･) ┓**")
    sleep(1)
    await typew.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")
    sleep(1)
    await typew.edit("**♪┏(・o･)┛♪┗ ( ･o･) ┓**")
    sleep(1)
    await typew.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")
    sleep(1)
    await typew.edit("**♪┏(・o･)┛♪┗ ( ･o･) ┓**")
    sleep(1)
    await typew.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")
    sleep(1)
    await typew.edit("**♪┏(・o･)┛♪┗ ( ･o･) ┓**")
    sleep(1)
    await typew.edit("**♪┗ ( ･o･) ┓♪┏ (・o･) ┛♪**")


@bot.on(wiki_cmd(outgoing=True, pattern=r"hua$"))
async def _(e):
    await e.edit("أ‿أ")
    await e.edit("╥﹏╥")
    await e.edit("(;﹏;)")
    await e.edit("(ToT)")
    await e.edit("(┳Д┳)")
    await e.edit("(ಥ﹏ಥ)")
    await e.edit("（；へ：）")
    await e.edit("(T＿T)")
    await e.edit("（πーπ）")
    await e.edit("(Ｔ▽Ｔ)")
    await e.edit("(⋟﹏⋞)")
    await e.edit("（ｉДｉ）")
    await e.edit("(´Д⊂ヽ")
    await e.edit("(;Д;)")
    await e.edit("（>﹏<）")
    await e.edit("(TдT)")
    await e.edit("(つ﹏⊂)")
    await e.edit("༼☯﹏☯༽")
    await e.edit("(ノ﹏ヽ)")
    await e.edit("(ノAヽ)")
    await e.edit("(╥_╥)")
    await e.edit("(T⌓T)")
    await e.edit("(༎ຶ⌑༎ຶ)")
    await e.edit("(☍﹏⁰)｡")
    await e.edit("(ಥ_ʖಥ)")
    await e.edit("(つд⊂)")
    await e.edit("(≖͞_≖̥)")
    await e.edit("(இ﹏இ`｡)")
    await e.edit("༼ಢ_ಢ༽")
    await e.edit("༼ ༎ຶ ෴ ༎ຶ༽")


@bot.on(wiki_cmd(outgoing=True, pattern=r"huh(?: |$)(.*)"))
async def _(typew):
    await typew.edit("`\n(\\_/)`" "`\n(●_●)`" "`\n />❤️ *Ini Buat Kamu`")
    sleep(3)
    await typew.edit("`\n(\\_/)`" "`\n(●_●)`" "`\n/>💔  *Aku Ambil Lagi`")
    sleep(2)
    await typew.edit("`\n(\\_/)`" "`\n(●_●)`" "`\n💔<\\  *Terimakasih`")


@bot.on(wiki_cmd(pattern=r"(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    input_str = event.pattern_match.group(1)

    if input_str == "ceritacinta":

        await event.edit(input_str)

        animation_chars = [
            "`Cerita ❤️ Cinta` ",
            "  😐             😕 \n/👕\\         <👗\\ \n 👖               /|",
            "  😉          😳 \n/👕\\       /👗\\ \n  👖            /|",
            "  😚            😒 \n/👕\\         <👗> \n  👖             /|",
            "  😍         ☺️ \n/👕\\      /👗\\ \n  👖          /|",
            "  😍          😍 \n/👕\\       /👗\\ \n  👖           /|",
            "  😘   😊 \n /👕\\/👗\\ \n   👖   /|",
            " 😳  😁 \n /|\\ /👙\\ \n /     / |",
            "😈    /😰\\ \n<|\\      👙 \n /🍆    / |",
            "😅 \n/(),✊😮 \n /\\         _/\\/|",
            "😎 \n/\\_,__😫 \n  //    //       \\",
            "😖 \n/\\_,💦_😋  \n  //         //        \\",
            "  😭      ☺️ \n  /|\\   /(👶)\\ \n  /!\\   / \\ ",
            "`TAMAT 😅`",
        ]

        animation_interval = 3

        animation_ttl = range(103)

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 103])


@bot.on(wiki_cmd(pattern=r"(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    input_str = event.pattern_match.group(1)

    if input_str == "canda":

        await event.edit(input_str)

        animation_chars = [
            "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀   ⢳⡀⠀⡏⠀⠀⠀   ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀  ⠀   ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Kamu    ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀⠀__⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
            "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀  ⠀⢳⡀⠀⡏⠀⠀⠀   ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀      ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Pasti   ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀|__|⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
            "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀     ⠀⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Belum   ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀         ⡇\n  ⠙⢿⣯⠄⠀⠀(x)⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
            "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀     ⠀⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀   ⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Mandi  ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀   ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀⠀__ ⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
            "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀   ⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀ ⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Bwhaha  ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀|__| ⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
            "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀  ⠀⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀  ⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Canda   ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀   ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀****⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
        ]

        animation_interval = 1

        animation_ttl = range(11)

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])


@bot.on(wiki_cmd(outgoing=True, pattern=r"santet(?: |$)(.*)"))
async def _(typew):
    await typew.edit("`Mengaktifkan Perintah Santet Online....`")
    sleep(2)
    await typew.edit("`Mencari Nama Orang Ini...`")
    sleep(1)
    await typew.edit("`Santet Online Segera Dilakukan`")
    sleep(1)
    await typew.edit("0%")
    number = 1
    await typew.edit(str(number) + "%   ▎")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ▍")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ▌")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ▊")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ▉")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █▎")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █▍")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █▌")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █▊")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █▉")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██▎")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██▍")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██▌")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██▊")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██▉")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███▎")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███▍")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███▌")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███▊")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███▉")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████▎")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████▍")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████▌")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████▊")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████▉")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████▎")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████▍")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████▌")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████▊")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████▉")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████▎")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████▍")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████▌")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████▊")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████▉")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████▎")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████▍")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████▌")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████▊")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████▉")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████▎")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████▍")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████▌")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████▊")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████▉")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████████")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████████▎")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████████▍")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████████▌")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████████▊")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████████▉")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████████")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████████▎")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████████▍")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████████▌")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████████▊")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████████▉")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████████")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████████▎")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████████▍")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████████▌")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████████▊")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████████▉")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████████")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████████▎")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████████▍")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████████▌")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████████▊")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████████▉")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████████████")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████████████▎")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████████████▍")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████████████▌")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████████████▊")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   █████████████▉")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████████████")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████████████▎")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████████████▍")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████████████▌")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████████████▊")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ██████████████▉")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████████████")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████████████▎")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████████████▍")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████████████▌")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████████████▊")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ███████████████▉")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████████████")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████████████▎")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████████████▍")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████████████▌")
    number += 1
    sleep(0.03)
    await typew.edit(str(number) + "%   ████████████████▌")
    sleep(1)
    await typew.edit("`Target Berhasil Tersantet Online 🥴`")


@bot.on(wiki_cmd(outgoing=True, pattern=".nah(?: |$)(.*)"))
async def _(typew):
    await typew.edit("`\n(\\_/)`" "`\n(●_●)`" "`\n />💖 *Ini Buat Kamu`")
    sleep(2)
    await typew.edit("`\n(\\_/)`" "`\n(●_●)`" "`\n💖<\\  *Tapi Bo'ong`")





@bot.on(wiki_cmd(pattern=r"(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    input_str = event.pattern_match.group(1)

    if input_str == "owner":

        await event.edit(input_str)

        animation_chars = [
            "⬛⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬜⬜⬜⬛\n⬛⬜⬛⬜⬛⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬜⬜⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬛⬜⬜⬛⬛\n⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬜⬜⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬜⬜⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬛⬛⬛⬛⬛",
        ]

        animation_interval = 0.5

        animation_ttl = range(6)

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 6])
            


@bot.on(wiki_cmd(pattern=f"wikii$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(11)
    await edit_or_reply(event, "Wiki")
    animation_chars = [
        f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{ALIVE_NAME}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
        f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{ALIVE_NAME}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
        f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{ALIVE_NAME}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
        f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{ALIVE_NAME}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
        f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{ALIVE_NAME}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
        f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{ALIVE_NAME}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
        f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{ALIVE_NAME}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n", 
        f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{ALIVE_NAME}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
        f"⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️..**{ALIVE_NAME}**..⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n",
        f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{ALIVE_NAME}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n", 
        f"⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️..**{ALIVE_NAME}**..⚪️⚫️⚪️\n⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️\n⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️⚫️⚪️\n",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval) 
        await event.edit(animation_chars[i%192])
     

@bot.on(wiki_cmd(pattern=r"city", outgoing=True))
async def test(event):
    if event.fwd_from:
        return
    await edit_or_reply(event, 
        """☁☁🌞      ☁           ☁
       ☁  ✈         ☁    🚁    ☁    ☁        ☁          ☁     ☁   ☁
🏬🏨🏫🏢🏤🏥🏦🏪🏫
              🌲/     l🚍\🌳👭
           🌳/  🚘 l  🏃 \🌴 👬                       👬  🌴/            l  🚔    \🌲
      🌲/   🚖     l               \
   🌳/🚶           |   🚍         \ 🌴🚴🚴
🌴/                    |                     \🌲"""
    )        


CMD_HELP.update(
    {
        "animasi": f"`{cmd}gabut` ; `{cmd}dino`\
    \nUsage: ntahlah gabut doang.\
    \n\n`{cmd}gombal`\
    \nUsage: buat bercanda\
    \n\n`{cmd}cinta`\
    \nUsage: mengirim cintamu ke seseorang.\
    \n\n`{cmd}sayang`\
    \nUsage: untuk jadi buaya.\
    \n\n`{cmd}terkadang`\
    \nUsage: Auk dah iseng doang.\
    \n\n`{cmd}helikopter` ; `{cmd}tank` ; `{cmd}tembak`\n`{cmd}bundir`\
    \nUsage: liat sendiri\
    \n\n`{cmd}y`\
    \nUsage: jempol\
    \n\n`{cmd}bulan` ; `{cmd}hati` ; `{cmd}bernyanyi`\
    \nUsage: liat aja.\
    \n\n`{cmd}awk`\
    \nUsage: ketawa lari.\
    \n\n`{cmd}lar` ; `{cmd}abi` ; `{cmd}ajg`\
    \nUsage: liat sendiri.\
    \n\n`{cmd}nah` ; `{cmd}huh` ; `{cmd}owner`\
    \nUsage: cobain.\
    \n\n`{cmd}bunga` ; `{cmd}buah`\
    \nUsage: animasi.\
    \n\n`{cmd}waktu`\
    \nUsage: animasi.\
    \n\n`{cmd}hua`\
    \nUsage: nangis.\
    \n\n`{cmd}ceritacinta` ; `{cmd}canda`\
    \nUsage: liat sendiri\
    \n\n`{cmd}santet`\
    \nUsage: Santet Online Buat Bercanda.\
    \n\n`{cmd}wikii`\
    \nUsage: Wiki Userbot.\
    \n\n`{cmd}city`\
    \nUsage: Pemandangan Kota."
    }
)
