import subprocess
try:
    import sys
    import os
    import random
    import asyncio
    import json
    import platform
    import ctypes
    import time
    import config_selfbot
    import fr_en
    import rpc
    from colorama import Fore, Style, Back
    import requests
    import selfcord
    from hugchat import hugchat
    from hugchat.login import Login
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", '-r' , 'requirements.txt'])
    import sys
    import os
    import random
    import asyncio
    import json
    import platform
    import ctypes
    import time
    import config_selfbot
    import fr_en
    import rpc
    from colorama import Fore, Style, Back
    import requests
    import selfcord
    from hugchat import hugchat
    from hugchat.login import Login

os.system('cls' if os.name == 'nt' else 'clear')

nuclear_version = "v0.8.1"

print(Fore.LIGHTCYAN_EX + f"""$$\   $$\                     $$\                               
$$$\  $$ |                    $$ |                              
$$$$\ $$ |$$\   $$\  $$$$$$$\ $$ | $$$$$$\   $$$$$$\   $$$$$$\  
$$ $$\$$ |$$ |  $$ |$$  _____|$$ |$$  __$$\  \____$$\ $$  __$$\ 
$$ \$$$$ |$$ |  $$ |$$ /      $$ |$$$$$$$$ | $$$$$$$ |$$ |  \__|
$$ |\$$$ |$$ |  $$ |$$ |      $$ |$$   ____|$$  __$$ |$$ |      
$$ | \$$ |\$$$$$$  |\$$$$$$$\ $$ |\$$$$$$$\ \$$$$$$$ |$$ |      
\__|  \__| \______/  \_______|\__| \_______| \_______|\__|  {nuclear_version}   """, Style.RESET_ALL)



def set_terminal_title(title):
    system = platform.system()
    if system == 'Windows':
        ctypes.windll.kernel32.SetConsoleTitleW(title)
    elif system == 'Darwin':
        subprocess.run(['osascript', '-e', f'tell application "Terminal" to set custom title of front window to "{title}"'])
    elif system == 'Linux':
        sys.stdout.write(f"\x1b]2;{title}\x07")
        sys.stdout.flush()

try:
   set_terminal_title("| Nuclear SelfBot |")
except Exception as e:
   print(f"Error while trying to change the terminal name: {e}")


if config_selfbot.token == "":
   config_selfbot.token = input(f"Token: ")

if config_selfbot.lang == "":
   print("""Language Choice / Choix de la langue:
fr: Français
en: English""")
   config_selfbot.lang = input("fr / en: ")

if config_selfbot.prefix == "":
   config_selfbot.prefix = input(f"Prefix: ")

if config_selfbot.selfbot_name == "":
   config_selfbot.selfbot_name = input(f"SelfBot name: ")


def check_latest_version(repo_owner, repo_name):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest"
    response = requests.get(url)
    
    if response.status_code == 200:
        release_info = response.json()
        latest_version = release_info['tag_name']
        return latest_version
    else:
        return None

def call_check_repo():
    global nuclear_version
    repo_owner = "Sitois"
    repo_name = "Nuclear"
    current_version = nuclear_version
    
    latest_version = check_latest_version(repo_owner, repo_name)
    if latest_version:
        if not latest_version == current_version:
            print(Fore.BLUE, "[INFO]", f"{fr_en.error_check_version_one[config_selfbot.lang]} ({latest_version}) {fr_en.error_check_version_two[config_selfbot.lang]} https://github.com/Sitois/Nuclear/releases/tag/{latest_version}")
            print(f" {fr_en.error_check_version_three[config_selfbot.lang]} {current_version}", Style.RESET_ALL)

try:
    call_check_repo()
except Exception as e:
    print(f"Error while trying to check the last Nuclear version: {e}")

print(Fore.LIGHTYELLOW_EX, "[#]", Fore.YELLOW, fr_en.start_text[config_selfbot.lang], Style.RESET_ALL)



#######################
#  selfbot            #
#         config ^^   #
#######################

token = config_selfbot.token

nitro_sniper = config_selfbot.nitro_sniper

deltime = config_selfbot.deltime

deltime_ai = config_selfbot.deltime_ai



afk = config_selfbot.afk
#################



is_spamming = False

good_person = False


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

chiffres = [1, 2, 3, 4, 5 ,6, 7, 8, 9]


poetry = {
    "fr": [
     "Jour meilleur n'existe qu'avec douleur.",
     "La seule personne que vous êtes destiné à devenir est la personne que vous décidez d'être.",
     "L'avenir appartient à ceux qui croient en la beauté de leurs rêves.",
     "L'échec est le fondement de la réussite.",
     "Ne rêvez pas votre vie, vivez vos rêves.",
     "Crois en toi, et les autres suivront.",
     "Sois le changement que tu veux voir dans le monde.",
     "Poursuis tes rêves, ils connaissent le chemin.",
     "La vie récompense l'action.",
     "Tu es plus fort que tu ne le crois.",
     "Le succès commence par l'action.",
     "La persévérance bat le talent.",
     "Ne remettez pas à demain.",
     "Chaque effort compte.",
     "Les montagnes les plus hautes ont les pentes les plus raides.",
     "Les éclats de lumière percent l'obscurité la plus profonde."
    ],
    "en": [
     "Your attitude determines your direction.",
     "Progress, not perfection.",
     "Embrace the challenges, for they are the stepping stones to success.",
     "Embrace failure as a stepping stone, not a stumbling block.",
     "The only limits that exist are the ones you place on yourself.",
     "Courage is not the absence of fear but the triumph over it.",
     "Dreams don't work unless you do",
     "Opportunities don't happen. You create them.",
     "Don't wait for the perfect moment; take the moment and make it perfect.",
     "The only way to do great work is to love what you do.",
     "Believe you can, and you're halfway there.",
     "Don't watch the clock; do what it does. Keep going"
    ],
}








####################
#  start           #
#   setup     !!!  #
####################





bot = selfcord.Bot(prefixes=[config_selfbot.prefix], inbuilt_help=False)

@bot.on("ready")
async def ready(time):
    print(Fore.RED, "[+]", Fore.LIGHTRED_EX, f"{fr_en.ready_text[config_selfbot.lang]} @{bot.user.name} ({bot.user.id}), {fr_en.ready_text_two[config_selfbot.lang]} {time:0.2f} seconds.", Style.RESET_ALL)
    print(Fore.MAGENTA + " ------------------", Style.RESET_ALL)
    await bot.change_presence(status=config_selfbot.status_activity, afk=config_selfbot.afk, activity=selfcord.Activity.Game(name=config_selfbot.activity_name, details=config_selfbot.activity_details, state=config_selfbot.activity_state, buttons={config_selfbot.activity_button_one: config_selfbot.activity_button_one_answer, config_selfbot.activity_button_two: config_selfbot.activity_button_two_answer}, key=config_selfbot.image_key, application_id=config_selfbot.application_id))


#############
#############




####################
#  help            #
#   command   !!!  #
####################

@bot.cmd(description="Help command !!", aliases=["aide"])
async def help(ctx):
    msg = await ctx.message.edit(f"""☄ __**{config_selfbot.selfbot_name} :**__ ☄
  ☄ "{random.choice(poetry[config_selfbot.lang])}" ☄

  🏮| __**General:**__ `{config_selfbot.prefix}general`
  🎤| __**{fr_en.help_voice[config_selfbot.lang]}:**__ `{config_selfbot.prefix}voice`
  🕹️| __**Rich Presence:**__ `{config_selfbot.prefix}presence`
  🎲| __**Fun:**__ `{config_selfbot.prefix}fun`
  ⚙️| __**Config:**__ `{config_selfbot.prefix}config`""")
    await asyncio.sleep(deltime)
    await msg.delete()

#############

@bot.cmd()
async def fun(ctx):
    msg = await ctx.message.edit(f"""☄ __**{config_selfbot.selfbot_name} :**__ ☄

🎲| __**Fun:**__
 `{config_selfbot.prefix}cat`: {fr_en.help_fun_cat[config_selfbot.lang]}.
 `{config_selfbot.prefix}good`: {fr_en.help_fun_good[config_selfbot.lang]}.
 `{config_selfbot.prefix}call`: {fr_en.help_fun_call[config_selfbot.lang]}.
 `{config_selfbot.prefix}gift`: {fr_en.help_fun_gift[config_selfbot.lang]}.""")
    await asyncio.sleep(deltime)
    await msg.delete()

#############

@bot.cmd()
async def config(ctx):
    msg = await ctx.message.edit(f"""☄ __**{config_selfbot.selfbot_name} :**__ ☄

⚙️| __**Config:**__
 `{config_selfbot.prefix}nitrosniper`: {fr_en.help_general_sniper[config_selfbot.lang]}.
 `{config_selfbot.prefix}restart`: {fr_en.help_config_restart[config_selfbot.lang]}.
 `{config_selfbot.prefix}stop`: {fr_en.help_config_stop[config_selfbot.lang]}.""")
    await asyncio.sleep(deltime)
    await msg.delete()

#############

@bot.cmd()
async def general(ctx):
    msg = await ctx.message.edit(f"""☄ __**{config_selfbot.selfbot_name} :**__ ☄

🏮| __**GENERAL:**__
 `{config_selfbot.prefix}snipe`: Snipe.
 `{config_selfbot.prefix}hype / {config_selfbot.prefix}squad`: {fr_en.help_general_hype[config_selfbot.lang]} (bravery, brilliance, balance).
 `{config_selfbot.prefix}ping / {config_selfbot.prefix}latency`: {fr_en.help_general_ping[config_selfbot.lang]}.
 `{config_selfbot.prefix}flood`: Flood.
 `{config_selfbot.prefix}bio`: {fr_en.help_general_bio[config_selfbot.lang]}.
 `{config_selfbot.prefix}spam`: Spam. (`{config_selfbot.prefix}spam` 2 hello)
 `{config_selfbot.prefix}ai`: {fr_en.ai_help[config_selfbot.lang]}. (`{config_selfbot.prefix}ai` how are you today ?)
 `{config_selfbot.prefix}lang`""")
    await asyncio.sleep(deltime)
    await msg.delete()

#############

@bot.cmd()
async def voice(ctx):
    msg = await ctx.message.edit(f"""☄ __**{config_selfbot.selfbot_name} :**__ ☄
                           
🎤| __**Voice:**__
 `{config_selfbot.prefix}joinvc`: {fr_en.help_voice_vc[config_selfbot.lang]} (joinvc <voice_channel_id>).
 `{config_selfbot.prefix}joincam`: {fr_en.help_voice_cam[config_selfbot.lang]} (joincam <voice_channel_id>).
 `{config_selfbot.prefix}joinstream`: {fr_en.help_voice_stream[config_selfbot.lang]} (joinstream <voice_channel_id>).
 `{config_selfbot.prefix}leavevc`: {fr_en.help_voice_leave[config_selfbot.lang]} (leavevc <voice_channel_id>.""")
    await asyncio.sleep(deltime)
    await msg.delete()





####################
#  general         #
#   command   !!!  #
####################

sniped_messages = {}

@bot.on("message_delete")
async def message_logger(message):
    global sniped_messages
    sniped_messages[message.channel.id] = {
        'author': message.author,
        'content': message.content,
        'image': message.attachments[0].url if message.attachments else fr_en.empty[config_selfbot.lang]
    }

@bot.cmd()
async def snipe(ctx):
    global sniped_messages
    sniped_message = sniped_messages.get(ctx.channel.id)
    if sniped_message:
        msg = await ctx.message.edit(f"""__**🔫 Sniper:**__

🗣️ {fr_en.author[config_selfbot.lang]}: {sniped_message['author']}
📩 Message: {sniped_message['content']}
🖼️ Image: {sniped_message['image']}""")
        await asyncio.sleep(deltime)
        await msg.delete()
    else:
        msg = await ctx.message.edit(fr_en.error_no_message_snipe[config_selfbot.lang])
        await asyncio.sleep(deltime)
        await msg.delete()

#############

@bot.cmd(description="Change HypeSquad badge.", aliases=["squad"])
async def hype(ctx):
     await bot.change_hypesquad(house=ctx.content.split()[1])
     msg = await ctx.message.edit(f"🪄 HypeSquad {fr_en.hype_command[config_selfbot.lang]} '{ctx.message.content.split()[1]}'")
     await asyncio.sleep(deltime)
     await msg.delete()

#############
     
def fix_ai_character(texte, encodage_source="utf-8", encodage_destination="utf-8"):
    try:

        if any(ord(char) > 127 for char in texte):
            texte_correct = texte.encode(encodage_source, errors="ignore").decode(encodage_destination)
            return texte_correct
        else:
            return texte
    except Exception as e:
        print(f"Error while trying to correct the AI text: {e}")
        return None


@bot.cmd()
async def ai(ctx):
    message_split = ctx.message.content.split()
    content = ctx.message.content.replace(f"{message_split[0]} ", "")
    if not config_selfbot.hug_chat_password == "" and not config_selfbot.hug_chat_email == "":
      sign = Login(config_selfbot.hug_chat_email, config_selfbot.hug_chat_password)
      cookies = sign.login()
      chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
      ai_ask = content
      await ctx.message.edit(f"⌚ {fr_en.ai_wait[config_selfbot.lang]}...")
      query_result = chatbot.query(f"Question: {ai_ask}. You MUST answer entirely in {config_selfbot.language_ai} with a maximum of 1800 characters. You MUST anwser normally to the question (without specifying the characters limit.)")
      fixed_answer = fix_ai_character(str(query_result), encodage_source="iso-8859-1")
      msg = await ctx.message.edit( f"""❓| Question: {ai_ask}
✅| {fr_en.ai_response[config_selfbot.lang]}: {fixed_answer}""")
      await asyncio.sleep(deltime_ai)
      await msg.delete()
    else:
       msg = await ctx.message.edit(fr_en.ai_error[config_selfbot.lang])
       await asyncio.sleep(deltime)
       await msg.delete()

#############

@bot.cmd(description="Give the Ping.", aliases=["latency"])
async def ping(ctx):
    msg = await ctx.message.edit(f"🏓 Pong ! (Ping: **{round(bot.latency * 1000)}ms**)")
    await asyncio.sleep(deltime)
    await msg.delete()

#############

@bot.cmd()
async def spam(ctx):
    global is_spamming
    message_split = ctx.message.content.split()

    content = ctx.message.content.replace(f"{message_split[0]} {message_split[1]} ", "")

    try:
        count = int(message_split[1]) - 1
    except Exception:
        msg = await ctx.message.edit(f"{fr_en.spam_invalid[config_selfbot.lang]}!")
        await asyncio.sleep(deltime)
        await msg.delete()
        return
    if is_spamming == False:
      is_spamming = True

      await ctx.message.edit(content)

      for i in range(count):
        await ctx.channel.send(content)
        await asyncio.sleep(0.5)
      is_spamming = False
    else:
       msg = await ctx.message.edit(fr_en.spam_cooldown[config_selfbot.lang])
       await asyncio.sleep(deltime)
       await msg.delete()

#############

@bot.cmd()
async def bio(ctx):
    message_split = ctx.message.content.split()
    new_bio = ctx.message.content.replace(f"{message_split[0]} ", "")
    await bot.edit_profile(bio=new_bio)
    msg = await ctx.message.edit(f"📖 Bio {fr_en.bio_command[config_selfbot.lang]} \"`{new_bio}`\"")
    await asyncio.sleep(deltime)
    await msg.delete()

#############

@bot.cmd()
async def lang(ctx):
    if config_selfbot.lang == "fr":
        config_selfbot.lang = "en"
        msg = await ctx.message.edit("🟢 Language set to **English**.")
        await asyncio.sleep(deltime)
        await msg.delete()
    elif config_selfbot.lang == "en":
        config_selfbot.lang = "fr"
        msg = await ctx.message.edit("🟢 Langue changé en **Français**.")
        await asyncio.sleep(deltime)
        await msg.delete()

#############

@bot.on("message")
async def nitro_detect(ctx):
    if nitro_sniper == True:
      if not ctx.author.id == bot.user.id:
          if "discord.gift/" in ctx.content:
            reste = ctx.content.split("discord.gift/")[1]
            await bot.redeem_nitro(f"{reste}")
            print(Fore.LIGHTYELLOW_EX, "[~]", Fore.YELLOW, f"Nitro Sniper: discord.gift/{reste}", Style.RESET_ALL)





####################
# voice            #
#   command   !!!  #
####################

@bot.cmd(description="Join a voice channel.")
async def joinvc(ctx):
    voice_channel = bot.get_channel(ctx.message.content.split()[1])

    try:
        await selfcord.VoiceChannel.call(voice_channel)
        msg = await ctx.message.edit(f"📲 {fr_en.voice_join[config_selfbot.lang]} {voice_channel.name}.")
        await asyncio.sleep(deltime)
        await msg.delete()
    except Exception as e:
        msg = await ctx.message.edit(f"❌ {fr_en.voice_join_error[config_selfbot.lang]} : {e}")
        await asyncio.sleep(deltime)
        await msg.delete()

#############

@bot.cmd(description="Join a voice channel with camera.")
async def joincam(ctx):
    voice_channel = bot.get_channel(ctx.message.content.split()[1])
    try:
        await selfcord.VoiceChannel.video_call(voice_channel)
        msg = await ctx.message.edit(f"🎥 {fr_en.voice_join_cam[config_selfbot.lang]} {voice_channel.name} {fr_en.voice_join_cam_two[config_selfbot.lang]}.")
        await asyncio.sleep(deltime)
        await msg.delete()
    except Exception as e:
        msg = await ctx.message.edit(f"❌ {fr_en.voice_join_error[config_selfbot.lang]} : {e}")
        await asyncio.sleep(deltime)
        await msg.delete()

#############

@bot.cmd(description="Join a voice channel with a stream.")
async def joinstream(ctx):
    voice_channel = bot.get_channel(ctx.message.content.split()[1])

    try:
        await selfcord.VoiceChannel.stream_call(voice_channel)
        msg = await ctx.message.edit(f"🖥️ {fr_en.voice_join[config_selfbot.lang]} {voice_channel.name} {fr_en.voice_stream_join[config_selfbot.lang]}.")
        await asyncio.sleep(deltime)
        await msg.delete()
    except Exception as e:
        msg = await ctx.message.edit(f"❌ {fr_en.voice_join_error[config_selfbot.lang]} : {e}")
        await asyncio.sleep(deltime)
        await msg.delete()

#############

@bot.cmd(description="Leave the voice")
async def leavevc(ctx):
    voice_channel = bot.get_channel(ctx.message.content.split()[1])
    try:
        await selfcord.VoiceChannel.leave_call(voice_channel)
        msg = await ctx.message.edit(f"💼 {fr_en.leave_voice[config_selfbot.lang]} {voice_channel.name}.")
        await asyncio.sleep(deltime)
        await msg.delete()
    except Exception as e:
        msg = await ctx.message.edit(f"❌ {fr_en.leave_voice_error[config_selfbot.lang]} : {e}")
        await asyncio.sleep(deltime)
        await msg.delete()






####################
# fun              #
#   command   !!!  #
####################

@bot.cmd()
async def call(ctx):
   voice_channel = bot.get_channel(ctx.channel.id)
   await ctx.message.delete()
   for i in range(5):
    try:
        await selfcord.VoiceChannel.call(voice_channel)
        await asyncio.sleep(0.5)
        await selfcord.VoiceChannel.leave_call(voice_channel)
        await asyncio.sleep(0.6)
    except Exception as e:
       print(f"{fr_en.voice_join_error[config_selfbot.lang]}: {e}")

#############

good_person_list =[
   "GeForce RTX 4000",
   "🍗",
   "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu.",
   "AMD Ryzen™ 9 7900",
   "Intel Core ",
   "🐈",
   "🍟",
   "yipeeeeeeeee",
   "😍",
   "🌠",
   "u r beautiful",
   "you are all very intelligent",
   "excuse me"
]


@bot.cmd()
async def good(ctx):
    global good_person
    if good_person == False:
        good_person = True
        msg = await ctx.message.edit(f"🌈 Good Person {fr_en.enable[config_selfbot.lang]}")
        await asyncio.sleep(deltime)
        await msg.delete()
    elif good_person == True:
        good_person = False
        msg = await ctx.message.edit(f"🔥 Good Person {fr_en.disable[config_selfbot.lang]}")
        await asyncio.sleep(deltime)
        await msg.delete()

#############

@bot.on("message")
async def insult_detect(ctx):
    global good_person
    if good_person == True:
      if ctx.author.id == bot.user.id:
        if "fuck" in ctx.content:
           await ctx.edit(random.choice(good_person_list))
        elif "shit" in ctx.content:
           await ctx.edit(random.choice(good_person_list))
        elif "pute" in ctx.content:
           await ctx.edit(random.choice(good_person_list))
        elif "connard" in ctx.content:
           await ctx.edit(random.choice(good_person_list))
        elif "connasse" in ctx.content:
           await ctx.edit(random.choice(good_person_list))
        elif "conasse" in ctx.content:
           await ctx.edit(random.choice(good_person_list))
        elif "nigg" in ctx.content:
           await ctx.edit(random.choice(good_person_list))
        elif "bitch" in ctx.content:
           await ctx.edit(random.choice(good_person_list))
        elif "kys" in ctx.content:
           await ctx.edit(random.choice(good_person_list))
        elif "fdp" in ctx.content:
           await ctx.edit(random.choice(good_person_list))
        elif "ntm" in ctx.content:
           await ctx.edit(random.choice(good_person_list))

#############

@bot.cmd()
async def cat(ctx):
    requests.get('https://api.thecatapi.com/v1/images/search')

    if requests.get('https://api.thecatapi.com/v1/images/search').status_code == 200:
        data = json.loads(requests.get('https://api.thecatapi.com/v1/images/search').text)
        cat_image_url = data[0]['url']
        await ctx.message.edit(cat_image_url)
    else:
        await ctx.message.edit(f"failed for the cute cat: {requests.get('https://api.thecatapi.com/v1/images/search').text}")
        return

#############

@bot.cmd()
async def gift(ctx):
    await ctx.message.edit(f"discord.gift/{random.choice(chiffres)}{random.choice(alphabet).upper()}{random.choice(alphabet).upper()}{random.choice(alphabet).upper()}{random.choice(alphabet)}{random.choice(alphabet)}{random.choice(alphabet)}{random.choice(chiffres)}{random.choice(alphabet).upper()}{random.choice(alphabet)}{random.choice(chiffres)}{random.choice(alphabet)}{random.choice(alphabet).upper()}{random.choice(alphabet).upper()}{random.choice(alphabet)}{random.choice(alphabet)}{random.choice(chiffres)}")


####################
#  setings         #
#   command   !!!  #
####################



def restart_selfbot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

@bot.cmd()
async def restart(ctx):
    msg = await ctx.message.edit(fr_en.restart_command[config_selfbot.lang])
    time.sleep(2)
    await msg.delete()
    restart_selfbot()

#############

@bot.cmd()
async def nitrosniper(ctx):
    global nitro_sniper
    if nitro_sniper == False:
        nitro_sniper = True
        msg = await ctx.message.edit("🟢 Nitro Sniper **On**.")
        await asyncio.sleep(deltime)
        await msg.delete()
    elif nitro_sniper == True:
        nitro_sniper = False
        msg = await ctx.message.edit("🔴 Nitro Sniper **Off**.")
        await asyncio.sleep(deltime)
        await msg.delete()

#############
    
@bot.cmd()
async def stop(ctx):
    msg = await ctx.message.edit(fr_en.stop_command[config_selfbot.lang])
    time.sleep(2)
    await msg.delete()
    exit()



#################
#    rpc        #
#      commands #
#################



@bot.cmd()
async def presence(ctx):
    msg = await ctx.message.edit(f'''☄ __**{config_selfbot.selfbot_name} :**__ ☄

🕹️| __**Rich Presence Settings:**__
 `{config_selfbot.prefix}rpc_status`: {fr_en.rpc_status_translate[config_selfbot.lang]}. (Online, Dnd, Invisible)                   
 `{config_selfbot.prefix}rpc_name`: {fr_en.rpc_name_translate[config_selfbot.lang]}.
 `{config_selfbot.prefix}rpc_details`: {fr_en.rpc_details_translate[config_selfbot.lang]}.
 `{config_selfbot.prefix}rpc_state`: {fr_en.rpc_state_translate[config_selfbot.lang]}.
 `{config_selfbot.prefix}rpc_url`: {fr_en.rpc_url_translate[config_selfbot.lang]}.
 `{config_selfbot.prefix}rpc_application_id`: {fr_en.rpc_id_translate[config_selfbot.lang]}.
 `{config_selfbot.prefix}rpc_image`: {fr_en.rpc_image_translate[config_selfbot.lang]}. (`{config_selfbot.prefix}tuto` !!!)
 `{config_selfbot.prefix}rpc_button_text_one`: {fr_en.rpc_button_text_one_translate[config_selfbot.lang]}.
 `{config_selfbot.prefix}rpc_button_link_one`: {fr_en.rpc_button_link_one_translate[config_selfbot.lang]}.
 `{config_selfbot.prefix}rpc_button_text_two`: {fr_en.rpc_button_text_two_translate[config_selfbot.lang]}.
 `{config_selfbot.prefix}rpc_button_link_two`: {fr_en.rpc_button_link_two_translate[config_selfbot.lang]}.
📖| __**Templates:**__
 `{config_selfbot.prefix}template`''')
    await asyncio.sleep(deltime)
    await msg.delete()

#############

@bot.cmd()
async def template(ctx):
    msg = await ctx.message.edit(f'''☄ __**{config_selfbot.selfbot_name} :**__ ☄

📖| __**Templates:**__
 `{config_selfbot.prefix}use`:
 "reset": {fr_en.template_help_reset[config_selfbot.lang]}
 "default": {fr_en.template_help_default[config_selfbot.lang]}
 "hi": {fr_en.template_help_hi[config_selfbot.lang]}
 "webdeck": {fr_en.template_help_webdeck[config_selfbot.lang]}
 "omori": {fr_en.template_help_omori[config_selfbot.lang]}
 "youtube": {fr_en.template_help_youtube[config_selfbot.lang]}
 "car": {fr_en.template_help_car[config_selfbot.lang]}
 "self": {fr_en.template_help_self[config_selfbot.lang]}
 "dark": {fr_en.template_help_dark[config_selfbot.lang]}
 "python": {fr_en.template_help_python[config_selfbot.lang]}
 "js": {fr_en.template_help_js[config_selfbot.lang]}
 "cod": {fr_en.template_help_cod[config_selfbot.lang]}
 "gta": {fr_en.template_help_gta[config_selfbot.lang]}''')
    await asyncio.sleep(deltime)
    await msg.delete()

#############

@bot.cmd()
async def tuto(ctx):
    msg = await ctx.message.edit(f"""☄ __**{config_selfbot.selfbot_name} :**__ ☄

🎮| __**Rich Presence Image Tutorial:**__
{fr_en.tutorial_rpc[config_selfbot.lang]}""")
    await asyncio.sleep(deltime)
    await msg.delete()

#############

@bot.cmd()
async def use(ctx):
    choice = ctx.message.content.split()[1]
    if choice.lower() == "hi":
     await bot.change_presence(status=rpc.read_variable_json("status_activity"),
                              afk=afk, 
                              activity=selfcord.Activity.Game(name="Hi !", 
                                                                details="hi !!!!!!", 
                                                                state=None,
                                                                buttons={rpc.read_variable_json("activity_button_one"): rpc.read_variable_json("activity_button_one_answer"), rpc.read_variable_json("activity_button_two"): rpc.read_variable_json("activity_button_two_answer")},
                                                                key="mp:attachments/1135264530188992562/1194342119989575832/MGflOC7.jpg?ex=65b93b47&is=65a6c647&hm=af5387b219eb9f9bf4cf7137758c4fad9da45a174305655ccb84c977a38dcd9f&=&format=webp&width=744&height=419",
                                                                application_id=config_selfbot.application_id if rpc.read_variable_json("application_id") == "VOID" else rpc.read_variable_json("application_id")
                                                                )
                                                                )
     msg = await ctx.message.edit(f"👋 Template \"hi !\".")
     await asyncio.sleep(deltime)
     await msg.delete()
    elif choice.lower() == "omori":
     await bot.change_presence(status=rpc.read_variable_json("status_activity"),
                              afk=afk, 
                              activity=selfcord.Activity.Game(name="Omori", 
                                                                details="In Game", 
                                                                state="Fighting a boss.",
                                                                buttons={rpc.read_variable_json("activity_button_one"): rpc.read_variable_json("activity_button_one_answer"), rpc.read_variable_json("activity_button_two"): rpc.read_variable_json("activity_button_two_answer")},
                                                                key="mp:attachments/1135264530188992562/1177984303456604253/i9ja3eA.gif?ex=65b517df&is=65a2a2df&hm=ba4d90afb6d6f47adceb1dbdc8ae28435c20a0fc46dd52cd3b492b427d356987&=&width=559&height=419",
                                                                application_id=config_selfbot.application_id if rpc.read_variable_json("application_id") == "VOID" else rpc.read_variable_json("application_id")
                                                                )
                                                                )
     msg = await ctx.message.edit(f"💡 Template \"Omori\".")
     await asyncio.sleep(deltime)
     await msg.delete()
    elif choice.lower() == "cod":
     await bot.change_presence(status=rpc.read_variable_json("status_activity"),
                              afk=afk,
                              activity=selfcord.Activity.Game(name="Call Of Duty: MWIII", 
                                                                details=f"{fr_en.rpc_cod_details[config_selfbot.lang]}", 
                                                                state=f"{fr_en.rpc_cod_state[config_selfbot.lang]}",
                                                                buttons={rpc.read_variable_json("activity_button_one"): rpc.read_variable_json("activity_button_one_answer"), rpc.read_variable_json("activity_button_two"): rpc.read_variable_json("activity_button_two_answer")},
                                                                key="mp:attachments/1135264530188992562/1199007140782813284/5rr7SXS.png?ex=65c0f96a&is=65ae846a&hm=f92e8757ce026cb26fc3d6e44e2e9e02ccb2577e9f047e62f9891c0f5925c725&=&format=webp&quality=lossless",
                                                                application_id=config_selfbot.application_id if rpc.read_variable_json("application_id") == "VOID" else rpc.read_variable_json("application_id")
                                                                )
                                                                )
     msg = await ctx.message.edit(f"🔫 Template \"Call Of Duty\".")
     await asyncio.sleep(deltime)
     await msg.delete()
    elif choice.lower() == "youtube":
     await bot.change_presence(status=rpc.read_variable_json("status_activity"),
                              afk=afk,
                              activity=selfcord.Activity.Watch(name="Youtube", 
                                                                details="Watching Videos", 
                                                                state=None,
                                                                buttons={rpc.read_variable_json("activity_button_one"): rpc.read_variable_json("activity_button_one_answer"), rpc.read_variable_json("activity_button_two"): rpc.read_variable_json("activity_button_two_answer")},
                                                                key="mp:attachments/1135264530188992562/1197991793111863417/ILAO8CE.png?ex=65bd47cd&is=65aad2cd&hm=585fcd20ef938d1a7637732d5d251cba50c82024c980c5b1e785bb486e4c5f4a&=&format=webp&quality=lossless&width=419&height=419",
                                                                application_id=config_selfbot.application_id if rpc.read_variable_json("application_id") == "VOID" else rpc.read_variable_json("application_id")
                                                                )
                                                                )
     msg = await ctx.message.edit(f"🎦 Template \"YouTube\".")
     await asyncio.sleep(deltime)
     await msg.delete()
    elif choice.lower() == "car":
     await bot.change_presence(status=rpc.read_variable_json("status_activity"), 
                              afk=afk, 
                              activity=selfcord.Activity.Watch(name="Drift Car", 
                                                                details="Watching DriftCar", 
                                                                state=None,
                                                                buttons={rpc.read_variable_json("activity_button_one"): rpc.read_variable_json("activity_button_one_answer"), rpc.read_variable_json("activity_button_two"): rpc.read_variable_json("activity_button_two_answer")},
                                                                key="mp:attachments/1135264530188992562/1198216462536552468/Wy5D92g.gif?ex=65be190a&is=65aba40a&hm=ee3adfbaccfb4a72ef71196d5b675aaef7df29a6f92f6841e4b161ed989aa783&=",
                                                                application_id=config_selfbot.application_id if rpc.read_variable_json("application_id") == "VOID" else rpc.read_variable_json("application_id")
                                                                )
                                                                )
     msg = await ctx.message.edit(f"🏎️ Template \"Car\".")
     await asyncio.sleep(deltime)
     await msg.delete()
    elif choice.lower() == "js":
     await bot.change_presence(status=rpc.read_variable_json("status_activity"),
                              afk=afk, 
                              activity=selfcord.Activity.Game(name="Visual Studio Code", 
                                                                details=f"Editing {bot.user.name}.js (273 lines)", 
                                                                state="Workspace: Nuclear",
                                                                buttons={rpc.read_variable_json("activity_button_one"): rpc.read_variable_json("activity_button_one_answer"), rpc.read_variable_json("activity_button_two"): rpc.read_variable_json("activity_button_two_answer")},
                                                                key="mp:attachments/1135264530188992562/1198623222678179960/FYcrOR1.png?ex=65bf93dd&is=65ad1edd&hm=196ea799818a84abed3db5089be49eb2f470fe31e9ed5d984bfb6b898c868a4a&=&format=webp&quality=lossless",
                                                                application_id=config_selfbot.application_id if rpc.read_variable_json("application_id") == "VOID" else rpc.read_variable_json("application_id")
                                                                )
                                                                )
     msg = await ctx.message.edit(f"👨‍💻 Template \"JavaScript\".")
     await asyncio.sleep(deltime)
     await msg.delete()
    elif choice.lower() == "python":
     await bot.change_presence(status=rpc.read_variable_json("status_activity"),
                              afk=afk, 
                              activity=selfcord.Activity.Game(name="Visual Studio Code", 
                                                                details=f"Editing {bot.user.name}.py", 
                                                                state="Workspace: Nuclear",
                                                                buttons={rpc.read_variable_json("activity_button_one"): rpc.read_variable_json("activity_button_one_answer"), rpc.read_variable_json("activity_button_two"): rpc.read_variable_json("activity_button_two_answer")},
                                                                key="mp:attachments/1135264530188992562/1198617576553599057/3jMZG0a.png?ex=65bf8e9b&is=65ad199b&hm=d61ea94e9db57f790e49dab09a9390bd61e5362a14cd44738a9a2e8aa70092d0&=&format=webp&quality=lossless",
                                                                application_id=config_selfbot.application_id if rpc.read_variable_json("application_id") == "VOID" else rpc.read_variable_json("application_id")
                                                                )
                                                                )
     msg = await ctx.message.edit(f"👨‍💻 Template \"Python\".")
     await asyncio.sleep(deltime)
     await msg.delete()
    elif choice.lower() == "webdeck":
     await bot.change_presence(status=rpc.read_variable_json("status_activity"),
                              afk=afk,
                              activity=selfcord.Activity.Game(name="WebDeck", 
                                                                details="Watching stars on GitHub...", 
                                                                state="Playing with Free StreamDeck.",
                                                                buttons={"Webdeck's GitHub (star it)": "https://github.com/Lenochxd/WebDeck", "WebDeck's Discord server": "https://discord.com/invite/CK2mu4P"},
                                                                key="mp:attachments/1135264530188992562/1197999417853218927/jj0PYp2.png?ex=65bd4ee6&is=65aad9e6&hm=ef2a47c5023678209436c74e3067469cf5c28143e5c12a3f714746fd03f1321e&=&format=webp&quality=lossless",
                                                                application_id=config_selfbot.application_id if rpc.read_variable_json("application_id") == "VOID" else rpc.read_variable_json("application_id")
                                                                )
                                                                )
     msg = await ctx.message.edit(f"📱 Template \"WebDeck\".")
     await asyncio.sleep(deltime)
     await msg.delete()
    elif choice.lower() == "self":
     await bot.change_presence(status=rpc.read_variable_json("status_activity"),
                              afk=afk, 
                              activity=selfcord.Activity.Stream(name="click mee", 
                                                                details="Nuclear $B", 
                                                                state="Free $B",
                                                                buttons={"Nuclear $B": "https://github.com/Sitois/Nuclear", "star it !": "https://github.com/Sitois/Nuclear"},
                                                                key="mp:attachments/1135264530188992562/1198281648437993553/CIjvBOJ.png?ex=65be55bf&is=65abe0bf&hm=40a3c63ca07dfac28726eadae220a07412551a69deea021b73c24ae00933782e&=&format=webp&quality=lossless",
                                                                application_id=config_selfbot.application_id if rpc.read_variable_json("application_id") == "VOID" else rpc.read_variable_json("application_id"),
                                                                url=rpc.read_variable_json("streaming_url")
                                                                )
                                                                )
     msg = await ctx.message.edit(f"🌌 Template \"Nuclear\".")
     await asyncio.sleep(deltime)
     await msg.delete()
    elif choice.lower() == "dark":
     await bot.change_presence(status=rpc.read_variable_json("status_activity"),
                              afk=afk, 
                              activity=selfcord.Activity.Game(name="☄", 
                                                                details=None, 
                                                                state=None,
                                                                buttons={rpc.read_variable_json("activity_button_one"): rpc.read_variable_json("activity_button_one_answer"), rpc.read_variable_json("activity_button_two"): rpc.read_variable_json("activity_button_two_answer")},
                                                                key="mp:attachments/1135264530188992562/1205872002238382111/PNjYcIL.png?ex=65d9f2d1&is=65c77dd1&hm=37a71d4fc6c032214d71c8d94d7d6f6c99f8f9773c467cf8f7cc4d56a618da73&=&format=webp&quality=lossless",
                                                                application_id=config_selfbot.application_id if rpc.read_variable_json("application_id") == "VOID" else rpc.read_variable_json("application_id")
                                                                )
                                                                )
     msg = await ctx.message.edit(f"🖤 Template \"Dark\".")
     await asyncio.sleep(deltime)
     await msg.delete()
    elif choice.lower() == "gta":
     await bot.change_presence(status=rpc.read_variable_json("status_activity"),
                              afk=afk, 
                              activity=selfcord.Activity.Game(name="Grand Theft Auto VI", 
                                                                details="Welcome to Vice City !", 
                                                                state="Playing SinglePlayer",
                                                                buttons={rpc.read_variable_json("activity_button_one"): rpc.read_variable_json("activity_button_one_answer"), rpc.read_variable_json("activity_button_two"): rpc.read_variable_json("activity_button_two_answer")},
                                                                key="mp:attachments/1135264530188992562/1200905385230475424/rhqvEdX.png?ex=65c7e14b&is=65b56c4b&hm=b375f98036eb15cedb369aff743ab040585f4777cc3756530e936fd5bbbb98d4&=&format=webp&quality=lossless&width=417&height=419",
                                                                application_id=config_selfbot.application_id if rpc.read_variable_json("application_id") == "VOID" else rpc.read_variable_json("application_id")
                                                                )
                                                                )
     msg = await ctx.message.edit(f"🔫 Template \"Grand Theft Auto VI\".")
     await asyncio.sleep(deltime)
     await msg.delete()
    elif choice.lower() == "reset":
     await bot.change_presence(status=rpc.read_variable_json("status_activity"),
                              afk=afk, 
                              activity=selfcord.Activity.Game(name=rpc.read_variable_json("activity_name"), 
                                                                details=rpc.read_variable_json("activity_details"), 
                                                                state=rpc.read_variable_json("activity_state"),  
                                                                buttons={rpc.read_variable_json("activity_button_one"): rpc.read_variable_json("activity_button_one_answer"), rpc.read_variable_json("activity_button_two"): rpc.read_variable_json("activity_button_two_answer")}, 
                                                                key=rpc.read_variable_json("image_key"), 
                                                                application_id=config_selfbot.application_id if rpc.read_variable_json("application_id") == "VOID" else rpc.read_variable_json("application_id")
                                                                )
                                                                )
     msg = await ctx.message.edit(f"🔄️ RPC Reset.")
     await asyncio.sleep(deltime)
     await msg.delete()
    elif choice.lower() == "default":
     await bot.change_presence(status=config_selfbot.status_activity,
                              afk=afk,
                              activity=selfcord.Activity.Game(name=config_selfbot.activity_name, 
                                                                details=config_selfbot.activity_details,
                                                                state=config_selfbot.activity_state,
                                                                buttons={config_selfbot.activity_button_one: config_selfbot.activity_button_one_answer, config_selfbot.activity_button_two: config_selfbot.activity_button_two_answer},
                                                                key=config_selfbot.image_key,
                                                                application_id=config_selfbot.application_id
                                                                )
                                                                )
     msg = await ctx.message.edit(f"🔄️ RPC \"Default\".")
     await asyncio.sleep(deltime)
     await msg.delete()
    else:
        msg = await ctx.message.edit("❌ Incorrect !")
        await asyncio.sleep(deltime)
        await msg.delete()



#############



@bot.cmd()
async def rpc_details(ctx):
    message_split = ctx.message.content.split()
    message_content = ctx.message.content.replace(f"{message_split[0]} ", "")
    rpc.edit_variable_json("activity_details", message_content)
    await bot.change_presence(status=rpc.read_variable_json("status_activity"),
                              afk=afk, 
                              activity=selfcord.Activity.Game(name=rpc.read_variable_json("activity_name"), 
                                                                details=rpc.read_variable_json("activity_details"), 
                                                                state=rpc.read_variable_json("activity_state"),  
                                                                buttons={rpc.read_variable_json("activity_button_one"): rpc.read_variable_json("activity_button_one_answer"), rpc.read_variable_json("activity_button_two"): rpc.read_variable_json("activity_button_two_answer")}, 
                                                                key=rpc.read_variable_json("image_key"), 
                                                                application_id=config_selfbot.application_id if rpc.read_variable_json("application_id") == "VOID" else rpc.read_variable_json("application_id")
                                                                )
                                                                )
    msg = await ctx.message.edit(f"🕹️| Details: `{message_content}`")
    await asyncio.sleep(deltime)
    await msg.delete()

#############

@bot.cmd()
async def rpc_name(ctx):
    message_split = ctx.message.content.split()
    message_content = ctx.message.content.replace(f"{message_split[0]} ", "")
    rpc.edit_variable_json("activity_name", message_content)
    await bot.change_presence(status=rpc.read_variable_json("status_activity"),
                              afk=afk, 
                              activity=selfcord.Activity.Game(name=rpc.read_variable_json("activity_name"), 
                                                                details=rpc.read_variable_json("activity_details"), 
                                                                state=rpc.read_variable_json("activity_state"),  
                                                                buttons={rpc.read_variable_json("activity_button_one"): rpc.read_variable_json("activity_button_one_answer"), rpc.read_variable_json("activity_button_two"): rpc.read_variable_json("activity_button_two_answer")}, 
                                                                key=rpc.read_variable_json("image_key"), 
                                                                application_id=config_selfbot.application_id if rpc.read_variable_json("application_id") == "VOID" else rpc.read_variable_json("application_id")
                                                                )
                                                                )
    msg = await ctx.message.edit(f"🕹️| Name: `{message_content}`")
    await asyncio.sleep(deltime)
    await msg.delete()

#############

@bot.cmd()
async def rpc_state(ctx):
    message_split = ctx.message.content.split()
    message_content = ctx.message.content.replace(f"{message_split[0]} ", "")
    rpc.edit_variable_json("activity_state", message_content)
    await bot.change_presence(status=rpc.read_variable_json("status_activity"),
                              afk=afk, 
                              activity=selfcord.Activity.Game(name=rpc.read_variable_json("activity_name"), 
                                                                details=rpc.read_variable_json("activity_details"), 
                                                                state=rpc.read_variable_json("activity_state"),  
                                                                buttons={rpc.read_variable_json("activity_button_one"): rpc.read_variable_json("activity_button_one_answer"), rpc.read_variable_json("activity_button_two"): rpc.read_variable_json("activity_button_two_answer")}, 
                                                                key=rpc.read_variable_json("image_key"), 
                                                                application_id=config_selfbot.application_id if rpc.read_variable_json("application_id") == "VOID" else rpc.read_variable_json("application_id")
                                                                )
                                                                )
    msg = await ctx.message.edit(f"🕹️| State: `{message_content}`")
    await asyncio.sleep(deltime)
    await msg.delete()

#############

@bot.cmd(description='set rpc title')
async def rpc_url(ctx):
    message_split = ctx.message.content.split()
    message_content = ctx.message.content.replace(f"{message_split[0]} ", "")
    rpc.edit_variable_json("streaming_url", message_content)
    await bot.change_presence(status=rpc.read_variable_json("status_activity"),
                              afk=afk, 
                              activity=selfcord.Activity.Game(name=rpc.read_variable_json("activity_name"), 
                                                                details=rpc.read_variable_json("activity_details"), 
                                                                state=rpc.read_variable_json("activity_state"),  
                                                                buttons={rpc.read_variable_json("activity_button_one"): rpc.read_variable_json("activity_button_one_answer"), rpc.read_variable_json("activity_button_two"): rpc.read_variable_json("activity_button_two_answer")}, 
                                                                key=rpc.read_variable_json("image_key"), 
                                                                application_id=config_selfbot.application_id if rpc.read_variable_json("application_id") == "VOID" else rpc.read_variable_json("application_id")
                                                                )
                                                                )
    msg = await ctx.message.edit(f"🕹️| Stream URL: `{message_content}`")
    await asyncio.sleep(deltime)
    await msg.delete()

#############

@bot.cmd(description='set rpc title')
async def rpc_image(ctx):
    message_split = ctx.message.content.split()
    message_content = ctx.message.content.replace(f"{message_split[0]} ", "")
    rpc.edit_variable_json("image_key", message_content)
    await bot.change_presence(status=rpc.read_variable_json("status_activity"),
                              afk=afk, 
                              activity=selfcord.Activity.Game(name=rpc.read_variable_json("activity_name"), 
                                                                details=rpc.read_variable_json("activity_details"), 
                                                                state=rpc.read_variable_json("activity_state"),  
                                                                buttons={rpc.read_variable_json("activity_button_one"): rpc.read_variable_json("activity_button_one_answer"), rpc.read_variable_json("activity_button_two"): rpc.read_variable_json("activity_button_two_answer")}, 
                                                                key=rpc.read_variable_json("image_key"), 
                                                                application_id=config_selfbot.application_id if rpc.read_variable_json("application_id") == "VOID" else rpc.read_variable_json("application_id")
                                                                )
                                                                )
    msg = await ctx.message.edit(f"🕹️| Image: `{message_content}`")
    await asyncio.sleep(deltime)
    await msg.delete()

#############

@bot.cmd(description='set rpc title')
async def rpc_application_id(ctx):
    message_split = ctx.message.content.split()
    message_content = ctx.message.content.replace(f"{message_split[0]} ", "")
    rpc.edit_variable_json("application_id", message_content)
    await bot.change_presence(status=rpc.read_variable_json("status_activity"),
                              afk=afk, 
                              activity=selfcord.Activity.Game(name=rpc.read_variable_json("activity_name"), 
                                                                details=rpc.read_variable_json("activity_details"), 
                                                                state=rpc.read_variable_json("activity_state"),  
                                                                buttons={rpc.read_variable_json("activity_button_one"): rpc.read_variable_json("activity_button_one_answer"), rpc.read_variable_json("activity_button_two"): rpc.read_variable_json("activity_button_two_answer")}, 
                                                                key=rpc.read_variable_json("image_key"), 
                                                                application_id=config_selfbot.application_id if rpc.read_variable_json("application_id") == "VOID" else rpc.read_variable_json("application_id")
                                                                )
                                                                )
    msg = await ctx.message.edit(f"🕹️| Application ID: `{message_content}`")
    await asyncio.sleep(deltime)
    await msg.delete()

#############

@bot.cmd()
async def rpc_button_text_one(ctx):
    message_split = ctx.message.content.split()
    message_content = ctx.message.content.replace(f"{message_split[0]} ", "")
    rpc.edit_variable_json("activity_button_one", message_content)
    await bot.change_presence(status=rpc.read_variable_json("status_activity"),
                              afk=afk, 
                              activity=selfcord.Activity.Game(name=rpc.read_variable_json("activity_name"), 
                                                                details=rpc.read_variable_json("activity_details"), 
                                                                state=rpc.read_variable_json("activity_state"),  
                                                                buttons={rpc.read_variable_json("activity_button_one"): rpc.read_variable_json("activity_button_one_answer"), rpc.read_variable_json("activity_button_two"): rpc.read_variable_json("activity_button_two_answer")}, 
                                                                key=rpc.read_variable_json("image_key"), 
                                                                application_id=config_selfbot.application_id if rpc.read_variable_json("application_id") == "VOID" else rpc.read_variable_json("application_id")
                                                                )
                                                                )
    msg = await ctx.message.edit(f"🕹️| Button One Text: `{message_content}`")
    await asyncio.sleep(deltime)
    await msg.delete()

#############

@bot.cmd()
async def rpc_button_text_two(ctx):
    message_split = ctx.message.content.split()
    message_content = ctx.message.content.replace(f"{message_split[0]} ", "")
    rpc.edit_variable_json("activity_button_two", message_content)
    await bot.change_presence(status=rpc.read_variable_json("status_activity"),
                              afk=afk, 
                              activity=selfcord.Activity.Game(name=rpc.read_variable_json("activity_name"), 
                                                                details=rpc.read_variable_json("activity_details"), 
                                                                state=rpc.read_variable_json("activity_state"),  
                                                                buttons={rpc.read_variable_json("activity_button_one"): rpc.read_variable_json("activity_button_one_answer"), rpc.read_variable_json("activity_button_two"): rpc.read_variable_json("activity_button_two_answer")}, 
                                                                key=rpc.read_variable_json("image_key"), 
                                                                application_id=config_selfbot.application_id if rpc.read_variable_json("application_id") == "VOID" else rpc.read_variable_json("application_id")
                                                                )
                                                                )
    msg = await ctx.message.edit(f"🕹️|Button Text Two: `{message_content}`")
    await asyncio.sleep(deltime)
    await msg.delete()

#############

@bot.cmd()
async def rpc_button_link_one(ctx):
    message_split = ctx.message.content.split()
    message_content = ctx.message.content.replace(f"{message_split[0]} ", "")
    rpc.edit_variable_json("activity_button_one_answer", message_content)
    await bot.change_presence(status=rpc.read_variable_json("status_activity"),
                              afk=afk, 
                              activity=selfcord.Activity.Game(name=rpc.read_variable_json("activity_name"), 
                                                                details=rpc.read_variable_json("activity_details"), 
                                                                state=rpc.read_variable_json("activity_state"),  
                                                                buttons={rpc.read_variable_json("activity_button_one"): rpc.read_variable_json("activity_button_one_answer"), rpc.read_variable_json("activity_button_two"): rpc.read_variable_json("activity_button_two_answer")}, 
                                                                key=rpc.read_variable_json("image_key"), 
                                                                application_id=config_selfbot.application_id if rpc.read_variable_json("application_id") == "VOID" else rpc.read_variable_json("application_id")
                                                                )
                                                                )
    msg = await ctx.message.edit(f"🕹️| Button One Link: `{message_content}`")
    await asyncio.sleep(deltime)
    await msg.delete()

#############

@bot.cmd()
async def rpc_button_link_two(ctx):
    message_split = ctx.message.content.split()
    message_content = ctx.message.content.replace(f"{message_split[0]} ", "")
    rpc.edit_variable_json("activity_button_two_answer", message_content)
    await bot.change_presence(status=rpc.read_variable_json("status_activity"),
                              afk=afk, 
                              activity=selfcord.Activity.Game(name=rpc.read_variable_json("activity_name"), 
                                                                details=rpc.read_variable_json("activity_details"), 
                                                                state=rpc.read_variable_json("activity_state"),  
                                                                buttons={rpc.read_variable_json("activity_button_one"): rpc.read_variable_json("activity_button_one_answer"), rpc.read_variable_json("activity_button_two"): rpc.read_variable_json("activity_button_two_answer")}, 
                                                                key=rpc.read_variable_json("image_key"), 
                                                                application_id=config_selfbot.application_id if rpc.read_variable_json("application_id") == "VOID" else rpc.read_variable_json("application_id")
                                                                )
                                                                )
    msg = await ctx.message.edit(f"🕹️| Button Link Two: `{message_content}`")
    await asyncio.sleep(deltime)
    await msg.delete()

#############

@bot.cmd()
async def rpc_status(ctx):
    message_split = ctx.message.content.split()
    message_content = ctx.message.content.replace(f"{message_split[0]} ", "")
    rpc.edit_variable_json("status_activity", message_content)
    await bot.change_presence(status=rpc.read_variable_json("status_activity"),
                              afk=afk, 
                              activity=selfcord.Activity.Game(name=rpc.read_variable_json("activity_name"), 
                                                                details=rpc.read_variable_json("activity_details"), 
                                                                state=rpc.read_variable_json("activity_state"),  
                                                                buttons={rpc.read_variable_json("activity_button_one"): rpc.read_variable_json("activity_button_one_answer"), rpc.read_variable_json("activity_button_two"): rpc.read_variable_json("activity_button_two_answer")}, 
                                                                key=rpc.read_variable_json("image_key"), 
                                                                application_id=config_selfbot.application_id if rpc.read_variable_json("application_id") == "VOID" else rpc.read_variable_json("application_id")
                                                                )
                                                                )
    msg = await ctx.message.edit(f"🕹️| RPC Status: `{message_content}`")
    await asyncio.sleep(deltime)
    await msg.delete()



####################
# flood command    #
#      (it's very  #
#     big!!!!)     #
####################

flood_spam = """_ _
_ _
_ _
_ _
_ _
_ _
_ _
_ _
_ _
_ _
_ _
_ _
_ _
_ _
_ _
_ _
_ _
_ _
_ _
_ _
_ _
_ _
_ _
_ _
_ _
_ _
_ _
_ _
_ _
_ _
_ _
_ _
_ _
_ _
_ _
_ _
_ _
_ _
_ _
_ _
_ _
_ _
_ _
_ _
_ _
_ _
_ _
_ _
_ _
_ _
_ _
_ _
_ _
_ _
_ _
_ _
_ _"""














@bot.cmd(description="flood")
async def flood(ctx):
    await ctx.message.edit(flood_spam)
    await asyncio.sleep(0.4)
    for i in range(2):
      await ctx.channel.send(flood_spam) 
      await asyncio.sleep(0.4)






####################
# start the        #
#      selfbot !!  #
####################
    
try:
    bot.run(token)
except selfcord.api.errors.LoginFailure:
   print(f"Token Error. Please configure a valid token in config_selfbot.py\n( Error Message: {e} )")
except Exception as e:
    print(f"Maybe Config Error. Make sure all information in config_selfbot.py are correct.\n( Error Message: {e} )")