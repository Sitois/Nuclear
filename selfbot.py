import subprocess
try:
    import sys
    import config_selfbot
    import random
    import asyncio
    from colorama import Fore, Style, Back
    import selfcord
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", '-r' , 'requirements.txt'])
    import sys
    import config_selfbot
    import random
    import asyncio
    from colorama import Fore, Style, Back
    import selfcord

print(Fore.LIGHTCYAN_EX + """$$\   $$\                     $$\                               
$$$\  $$ |                    $$ |                              
$$$$\ $$ |$$\   $$\  $$$$$$$\ $$ | $$$$$$\   $$$$$$\   $$$$$$\  
$$ $$\$$ |$$ |  $$ |$$  _____|$$ |$$  __$$\  \____$$\ $$  __$$\ 
$$ \$$$$ |$$ |  $$ |$$ /      $$ |$$$$$$$$ | $$$$$$$ |$$ |  \__|
$$ |\$$$ |$$ |  $$ |$$ |      $$ |$$   ____|$$  __$$ |$$ |      
$$ | \$$ |\$$$$$$  |\$$$$$$$\ $$ |\$$$$$$$\ \$$$$$$$ |$$ |      
\__|  \__| \______/  \_______|\__| \_______| \_______|\__|  v0.2    """, Style.RESET_ALL)


print(Fore.LIGHTYELLOW_EX, "[#]", Fore.YELLOW, "Démarrage du selfbot en cours...", Style.RESET_ALL)



#######################
#  selfbot            #
#         config ^^   #
#######################

token = config_selfbot.token

nitro_sniper = config_selfbot.nitro_sniper

deltime = config_selfbot.deltime


activity_name = config_selfbot.activity_name
activity_details = config_selfbot.activity_details
activity_state = config_selfbot.activity_state
status_activity = config_selfbot.status_activity
afk = config_selfbot.afk

streaming_url = config_selfbot.streaming_url
activity_button_one = config_selfbot.activity_button_one
activity_button_one_answer = config_selfbot.activity_button_one_answer
activity_button_two = config_selfbot.activity_button_two
activity_button_two_answer = config_selfbot.activity_button_two_answer
image_key = config_selfbot.image_key
application_id = config_selfbot.application_id
#################


poetry = [
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
    ]




bot = selfcord.Bot(prefixes=[config_selfbot.prefix], inbuilt_help=False)

@bot.on("ready")
async def ready(time):
    print(Fore.RED, "[+]", Fore.LIGHTRED_EX, f"Connecté en tant que @{bot.user.name} ({bot.user.id}), démarré en {time:0.2f} secondes.", Style.RESET_ALL)
    print(Fore.MAGENTA + " ------------------", Style.RESET_ALL)
    await bot.change_presence(status=config_selfbot.status_activity, afk=config_selfbot.afk, activity=selfcord.Activity.Stream(name=activity_name, details=activity_details, state=activity_state, url=streaming_url, buttons={activity_button_one: activity_button_one_answer, activity_button_two: activity_button_two_answer}, key=image_key, application_id=application_id))

@bot.cmd(description="set nitro sniper")
async def nitrosniper(ctx):
    global nitro_sniper
    if nitro_sniper == False:
        nitro_sniper = True
        msg = await ctx.message.edit("🟢 Nitro Sniper activé.")
        await asyncio.sleep(deltime)
        await msg.delete()
    elif nitro_sniper == True:
        nitro_sniper = False
        msg = await ctx.message.edit("🔴 Nitro Sniper désactivé.")
        await asyncio.sleep(deltime)
        await msg.delete()



@bot.on("message")
async def nitro_detect(ctx):
    if nitro_sniper == True:
      if not ctx.author.id == bot.user.id:
          if "discord.gift/" in ctx.content:
            reste = ctx.content.split("discord.gift/")[1]
            await bot.redeem_nitro(f"discord.gift/{reste}")
            print(Fore.LIGHTYELLOW_EX, "[~]", Fore.YELLOW, f"Nitro Sniper: discord.gift/{reste}", Style.RESET_ALL)

    

@bot.cmd()
async def temp(ctx):
    message_split = ctx.message.content.split()
    message_content = ctx.message.content.replace(f"{message_split[0]} ", "")
    msg = await ctx.message.edit(message_content)
    await asyncio.sleep(0.7)
    await msg.delete()




@bot.cmd(description="change bio")
async def bio(ctx):
    message_split = ctx.message.content.split()
    new_bio = ctx.message.content.replace(f"{message_split[0]} ", "")
    await bot.edit_profile(bio=new_bio)
    msg = await ctx.message.edit(f"📖 Bio changée en \"{new_bio}\"")
    await asyncio.sleep(deltime)
    await msg.delete()

@bot.cmd(description="Help command !!", aliases=["aide"])
async def help(ctx):
    msg = await ctx.message.edit(f"""☄ __**{config_selfbot.selfbot_name} :**__ ☄
  ☄ "{random.choice(poetry)}" ☄

  🏮| __**General:**__ `{config_selfbot.prefix}general`
  🎤| __**Voice:**__ `{config_selfbot.prefix}voice`
  🕹️| __**Riche Presence:**__ `{config_selfbot.prefix}presence`""")
    await asyncio.sleep(deltime)
    await msg.delete()
    

@bot.cmd(description="help general lol")
async def general(ctx):
    msg = await ctx.message.edit(f"""☄ __**{config_selfbot.selfbot_name} :**__ ☄

🏮| __**GENERAL:**__
 `{config_selfbot.prefix}snipe`: Snipe (all servers).
 `{config_selfbot.prefix}hype / {config_selfbot.prefix}squad`: Set your HypeSquad (bravery, brilliance, balance).
 `{config_selfbot.prefix}ping / {config_selfbot.prefix}latency`: Display the Selfbot's ping.
 `{config_selfbot.prefix}nitrosniper`: Toggle NitroSniper.
 `{config_selfbot.prefix}flood`: Flood.
 `{config_selfbot.prefix}bio`: Change account's bio.
 `{config_selfbot.prefix}temp`: Delete message after 1 second.
 `{config_selfbot.prefix}spam`: Spam. (DON'T SPAM TOO MUCH or your account will get banned.) ({config_selfbot.prefix}spam 15 hiii guys)""")
    await asyncio.sleep(deltime)
    await msg.delete()





@bot.cmd(description="help voice lul")
async def voice(ctx):
    msg = await ctx.message.edit(f"""☄ __**{config_selfbot.selfbot_name} :**__ ☄
                           
🎤| __**Voice:**__
 `{config_selfbot.prefix}joinvc`: Join the voice channel (joinvc <voice_channel_id>).
 `{config_selfbot.prefix}joincam`: Join the voice channel with a fake camera (joincam <voice_channel_id>).
 `{config_selfbot.prefix}joinstream`: Join the voice channel with a fake stream (joinstream <voice_channel_id>).
 `{config_selfbot.prefix}leavevc`: Leave the voice channnel (leavevc <channel_id>.""")
    await asyncio.sleep(deltime)
    await msg.delete()


@bot.cmd(description="Leave the voice")
async def leavevc(ctx):
    voice_channel = bot.get_channel(ctx.message.content.split()[1])
    try:
        await selfcord.VoiceChannel.leave_call(voice_channel)
        msg = await ctx.message.edit(f"💼 Déconnection du salon {voice_channel.name} réussi.")
        await asyncio.sleep(deltime)
        await msg.delete()
    except Exception as e:
        msg = await ctx.message.edit(f"❌ Erreur lors de la déconnexion au salon vocal : {e}")
        await asyncio.sleep(deltime)
        await msg.delete()
    
@bot.cmd(description="Leave the voice")
async def bypass(ctx):
    content = ctx.message.content.split()[1]
    msg = await ctx.message.edit(f"# discord.gg/{content} ON TOP")
    await asyncio.sleep(120)
    await msg.delete()

@bot.cmd(description="Snipe (all servers).")
async def snipe(ctx):
    msg = await ctx.message.edit(f"{bot.user.deleted_messages[-1].author}: {bot.user.deleted_messages[-1]}")
    await asyncio.sleep(deltime)
    await msg.delete()

@bot.cmd(description="Change HypeSquad badge.", aliases=["squad"])
async def hype(ctx):
     await bot.change_hypesquad(house=ctx.content.split()[1])
     msg = await ctx.message.edit(f"🪄 HypeSquad modifié en '{ctx.message.content.split()[1]}'")
     await asyncio.sleep(deltime)
     await msg.delete()

@bot.cmd(description="Join a voice channel.")
async def joinvc(ctx):
        voice_channel = bot.get_channel(ctx.message.content.split()[1])

        try:
            await selfcord.VoiceChannel.call(voice_channel)
            msg = await ctx.message.edit(f"📲 Connecté au salon vocal {voice_channel.name}.")
            await asyncio.sleep(deltime)
            await msg.delete()
        except Exception as e:
            msg = await ctx.message.edit(f"❌ Erreur lors de la connexion au salon vocal : {e}")
            await asyncio.sleep(deltime)
            await msg.delete()

@bot.cmd(description="Join a voice channel with camera.")
async def joincam(ctx):
        voice_channel = bot.get_channel(ctx.message.content.split()[1])
        try:
            await selfcord.VoiceChannel.video_call(voice_channel)
            msg = await ctx.message.edit(f"🎥 Connecté au salon vocal {voice_channel.name} avec la caméra activée.")
            await asyncio.sleep(deltime)
            await msg.delete()
        except Exception as e:
            msg = await ctx.message.edit(f"❌ Erreur lors de la connexion au salon vocal : {e}")
            await asyncio.sleep(deltime)
            await msg.delete()

@bot.cmd(description="Join a voice channel with a stream.")
async def joinstream(ctx):
        voice_channel = bot.get_channel(ctx.message.content.split()[1])

        try:
            await selfcord.VoiceChannel.stream_call(voice_channel)
            msg = await ctx.message.edit(f"🖥️ Connecté au salon vocal {voice_channel.name} avec le stream activé.")
            await asyncio.sleep(deltime)
            await msg.delete()
        except Exception as e:
            msg = await ctx.message.edit(f"❌ Erreur lors de la connexion au salon vocal : {e}")
            await asyncio.sleep(deltime)
            await msg.delete()

@bot.cmd(description="Give the Ping.", aliases=["latency"])
async def ping(ctx):
    msg = await ctx.message.edit(f"🏓 Pong ! (Ping: **{bot.latency * 1000}**)")
    await asyncio.sleep(deltime)
    await msg.delete()

@bot.cmd(description="chiant")
async def spam(ctx):
    message_split = ctx.message.content.split()
    content = ctx.message.content.replace(f"{message_split[0]} {message_split[1]} ", "")

    await ctx.message.edit(content)

    for i in range(int(message_split[1]) - 1):
      await ctx.channel.send(content)
      await asyncio.sleep(0.5)




#################
#    rpc        #
#      commands #
#################



@bot.cmd(description='rpc help lul')
async def presence(ctx):
    msg = await ctx.message.edit(f'''☄ __**{config_selfbot.selfbot_name} :**__ ☄

🕹️| __**Rich Presence Settings:**__
 `{config_selfbot.prefix}rpc_status`: Set RPC's status.                         
 `{config_selfbot.prefix}rpc_name`: Set RPC's name.
 `{config_selfbot.prefix}rpc_details`: Set RPC's details.
 `{config_selfbot.prefix}rpc_state`: Set RPC's state.
 `{config_selfbot.prefix}rpc_url`: Set RPC's streaming URL.
 `{config_selfbot.prefix}rpc_application_id`: Set RPC's Application ID.
 `{config_selfbot.prefix}rpc_image`: Set RPC's image. (see `{config_selfbot.prefix}tuto` !!!!)
 `{config_selfbot.prefix}rpc_button_text_one`: Set RPC's first button text.
 `{config_selfbot.prefix}rpc_button_link_one`: Set RPC's first button link.
 `{config_selfbot.prefix}rpc_button_text_two`: Set RPC's second button text.
 `{config_selfbot.prefix}rpc_button_link_two`: Set RPC's second button link.
📖| __**Templates:**__
 `{config_selfbot.prefix}use`: "reset" / "hi" / "webdeck" / "omori" / "youtube" / "car" / "self" / "dark" / "python" / "js"''')
    await asyncio.sleep(deltime)
    await msg.delete()

@bot.cmd(description='rpc tuto lul')
async def tuto(ctx):
    msg = await ctx.message.edit(f"""☄ __**{config_selfbot.selfbot_name} :**__ ☄

🎮| __**Rich Presence Image Tutorial:**__
 To get a custom rpc image, you should:
  1. Upload an image (gif, png...) into Discord. (in any channel)
  2. Right Click and "Copy Image Link".
  3. Do `{config_selfbot.prefix}rpc_image mp:attachements/67484738743874387438/657438923487543/example.png`.
  4. Done !""")
    await asyncio.sleep(deltime)
    await msg.delete()




@bot.cmd()
async def use(ctx):
    choice = ctx.message.content.split()[1]
    if choice.lower() == "hi":
     await bot.change_presence(status=config_selfbot.status_activity, 
                              afk=config_selfbot.afk, 
                              activity=selfcord.Activity.Game(name="Hi !", 
                                                                details="hi !!!!!!", 
                                                                state=None,
                                                                buttons={activity_button_one: activity_button_one_answer, activity_button_two: activity_button_two_answer}, 
                                                                key="mp:attachments/1135264530188992562/1194342119989575832/MGflOC7.jpg?ex=65b93b47&is=65a6c647&hm=af5387b219eb9f9bf4cf7137758c4fad9da45a174305655ccb84c977a38dcd9f&=&format=webp&width=744&height=419",
                                                                application_id=application_id
                                                                )
                                                                )
     msg = await ctx.message.edit(f"👋 Template \"hi !\" séléctionnée.")
     await asyncio.sleep(deltime)
     await msg.delete()
    elif choice.lower() == "omori":
     await bot.change_presence(status=config_selfbot.status_activity, 
                              afk=config_selfbot.afk, 
                              activity=selfcord.Activity.Game(name="Omori", 
                                                                details="In Game", 
                                                                state="Fighting a boss.",
                                                                buttons={activity_button_one: activity_button_one_answer, activity_button_two: activity_button_two_answer}, 
                                                                key="mp:attachments/1135264530188992562/1177984303456604253/i9ja3eA.gif?ex=65b517df&is=65a2a2df&hm=ba4d90afb6d6f47adceb1dbdc8ae28435c20a0fc46dd52cd3b492b427d356987&=&width=559&height=419",
                                                                application_id=application_id
                                                                )
                                                                )
     msg = await ctx.message.edit(f"💡 Template \"Omori\" séléctionnée.")
     await asyncio.sleep(deltime)
     await msg.delete()
    elif choice.lower() == "youtube":
     await bot.change_presence(status=config_selfbot.status_activity, 
                              afk=config_selfbot.afk, 
                              activity=selfcord.Activity.Watch(name="Youtube", 
                                                                details="Watching Videos", 
                                                                state=None,
                                                                buttons={activity_button_one: activity_button_one_answer, activity_button_two: activity_button_two_answer}, 
                                                                key="mp:attachments/1135264530188992562/1197991793111863417/ILAO8CE.png?ex=65bd47cd&is=65aad2cd&hm=585fcd20ef938d1a7637732d5d251cba50c82024c980c5b1e785bb486e4c5f4a&=&format=webp&quality=lossless&width=419&height=419",
                                                                application_id=application_id
                                                                )
                                                                )
     msg = await ctx.message.edit(f"🎦 Template \"YouTube\" séléctionnée.")
     await asyncio.sleep(deltime)
     await msg.delete()
    elif choice.lower() == "car":
     await bot.change_presence(status=config_selfbot.status_activity, 
                              afk=config_selfbot.afk, 
                              activity=selfcord.Activity.Watch(name="Drift Car", 
                                                                details="Watching DriftCar", 
                                                                state=None,
                                                                buttons={activity_button_one: activity_button_one_answer, activity_button_two: activity_button_two_answer}, 
                                                                key="mp:attachments/1135264530188992562/1198216462536552468/Wy5D92g.gif?ex=65be190a&is=65aba40a&hm=ee3adfbaccfb4a72ef71196d5b675aaef7df29a6f92f6841e4b161ed989aa783&=",
                                                                application_id=application_id
                                                                )
                                                                )
     msg = await ctx.message.edit(f"🏎️ Template \"Car\" séléctionnée.")
     await asyncio.sleep(deltime)
     await msg.delete()
    elif choice.lower() == "python":
     await bot.change_presence(status=config_selfbot.status_activity, 
                              afk=config_selfbot.afk, 
                              activity=selfcord.Activity.Game(name="Visual Studio Code", 
                                                                details=f"Editing {bot.user.name}.py", 
                                                                state="Workspace: Nuclear",
                                                                buttons={activity_button_one: activity_button_one_answer, activity_button_two: activity_button_two_answer}, 
                                                                key="mp:attachments/1135264530188992562/1198617576553599057/3jMZG0a.png?ex=65bf8e9b&is=65ad199b&hm=d61ea94e9db57f790e49dab09a9390bd61e5362a14cd44738a9a2e8aa70092d0&=&format=webp&quality=lossless",
                                                                application_id=application_id
                                                                )
                                                                )
     msg = await ctx.message.edit(f"👨‍💻 Template \"Python\" séléctionnée.")
     await asyncio.sleep(deltime)
     await msg.delete()
    elif choice.lower() == "js":
     await bot.change_presence(status=config_selfbot.status_activity, 
                              afk=config_selfbot.afk, 
                              activity=selfcord.Activity.Game(name="Visual Studio Code", 
                                                                details=f"Editing {bot.user.name}.js (273 lines)", 
                                                                state="Workspace: Nuclear",
                                                                buttons={activity_button_one: activity_button_one_answer, activity_button_two: activity_button_two_answer}, 
                                                                key="mp:attachments/1135264530188992562/1198623222678179960/FYcrOR1.png?ex=65bf93dd&is=65ad1edd&hm=196ea799818a84abed3db5089be49eb2f470fe31e9ed5d984bfb6b898c868a4a&=&format=webp&quality=lossless",
                                                                application_id=application_id
                                                                )
                                                                )
     msg = await ctx.message.edit(f"👨‍💻 Template \"JavaScript\" séléctionnée.")
     await asyncio.sleep(deltime)
     await msg.delete()
    elif choice.lower() == "dark":
     await bot.change_presence(status=config_selfbot.status_activity, 
                              afk=config_selfbot.afk, 
                              activity=selfcord.Activity.Game(name="to a game.", 
                                                                details="Life.", 
                                                                state=None,
                                                                buttons={activity_button_one: activity_button_one_answer, activity_button_two: activity_button_two_answer},
                                                                key="mp:attachments/1135264530188992562/1198250065970606210/0RoaYys.gif?ex=65be3856&is=65abc356&hm=39b3c558a1adb1b03ffa16c2ad8ff5b7ae7afedb3539db772fc0ee26c504fc8f&=",
                                                                application_id=application_id,
                                                                )
                                                                )
     msg = await ctx.message.edit(f"🖤 Template \"Dark\" séléctionnée.")
     await asyncio.sleep(deltime)
     await msg.delete()
    elif choice.lower() == "webdeck":
     await bot.change_presence(status=config_selfbot.status_activity, 
                              afk=config_selfbot.afk, 
                              activity=selfcord.Activity.Game(name="WebDeck", 
                                                                details="Watching stars on GitHub...", 
                                                                state="Playing with Free StreamDeck.",
                                                                buttons={"Webdeck's GitHub (star it)": "https://github.com/LeLenoch/WebDeck", "WebDeck's Discord server": "https://discord.com/invite/CK2mu4P"},
                                                                key="mp:attachments/1135264530188992562/1197999417853218927/jj0PYp2.png?ex=65bd4ee6&is=65aad9e6&hm=ef2a47c5023678209436c74e3067469cf5c28143e5c12a3f714746fd03f1321e&=&format=webp&quality=lossless",
                                                                application_id=application_id
                                                                )
                                                                )
     msg = await ctx.message.edit(f"📱 Template \"WebDeck\" séléctionnée.")
     await asyncio.sleep(deltime)
     await msg.delete()
    elif choice.lower() == "self":
     await bot.change_presence(status=config_selfbot.status_activity, 
                              afk=config_selfbot.afk, 
                              activity=selfcord.Activity.Stream(name="click mee", 
                                                                details="Nuclear $B", 
                                                                state="Free $B",
                                                                buttons={"Nuclear $B": "https://github.com/Sitois/Nuclear", "Star it !": "https://github.com/Sitois/Nuclear"},
                                                                key="mp:attachments/1135264530188992562/1198281648437993553/CIjvBOJ.png?ex=65be55bf&is=65abe0bf&hm=40a3c63ca07dfac28726eadae220a07412551a69deea021b73c24ae00933782e&=&format=webp&quality=lossless",
                                                                application_id=application_id,
                                                                url=streaming_url
                                                                )
                                                                )
     msg = await ctx.message.edit(f"🌌 Template \"Nuclear\" séléctionnée.")
     await asyncio.sleep(deltime)
     await msg.delete()
    elif choice.lower() == "reset":
     await bot.change_presence(status=config_selfbot.status_activity, 
                              afk=config_selfbot.afk, 
                              activity=selfcord.Activity.Stream(name=activity_name, 
                                                                details=activity_details, 
                                                                state=activity_state, 
                                                                url=streaming_url, 
                                                                buttons={activity_button_one: activity_button_one_answer, activity_button_two: activity_button_two_answer}, 
                                                                key=image_key, 
                                                                application_id=application_id
                                                                )
                                                                )
     msg = await ctx.message.edit(f"🔄️ Le RPC a bien été reset.")
     await asyncio.sleep(deltime)
     await msg.delete()
    else:
        msg = await ctx.message.edit("❌ Choix incorrect !")
        await asyncio.sleep(deltime)
        await msg.delete()







@bot.cmd(description='set rpc')
async def rpc_details(ctx):
    message_split = ctx.message.content.split()
    activity_details = ctx.message.content.replace(f"{message_split[0]} ", "")
    await bot.change_presence(status=config_selfbot.status_activity, 
                              afk=config_selfbot.afk, 
                              activity=selfcord.Activity.Stream(name=activity_name, 
                                                                details=activity_details, 
                                                                state=activity_state, 
                                                                url=streaming_url, 
                                                                buttons={activity_button_one: activity_button_one_answer, activity_button_two: activity_button_two_answer}, 
                                                                key=image_key, 
                                                                application_id=application_id
                                                                )
                                                                )
    msg = await ctx.message.edit(f"🕹️| Details changé en `{activity_details}`")
    await asyncio.sleep(deltime)
    await msg.delete()

@bot.cmd(description='set rpc title')
async def rpc_name(ctx):
    message_split = ctx.message.content.split()
    activity_name = ctx.message.content.replace(f"{message_split[0]} ", "")
    await bot.change_presence(status=config_selfbot.status_activity, 
                              afk=config_selfbot.afk, 
                              activity=selfcord.Activity.Stream(name=activity_name, 
                                                                details=activity_details, 
                                                                state=activity_state, 
                                                                url=streaming_url, 
                                                                buttons={activity_button_one: activity_button_one_answer, activity_button_two: activity_button_two_answer}, 
                                                                key=image_key, 
                                                                application_id=application_id
                                                                )
                                                                )
    msg = await ctx.message.edit(f"🕹️| Name changé en `{activity_name}`")
    await asyncio.sleep(deltime)
    await msg.delete()

@bot.cmd(description='set rpc title')
async def rpc_state(ctx):
    message_split = ctx.message.content.split()
    activity_state = ctx.message.content.replace(f"{message_split[0]} ", "")
    await bot.change_presence(status=config_selfbot.status_activity, 
                              afk=config_selfbot.afk, 
                              activity=selfcord.Activity.Stream(name=activity_name, 
                                                                details=activity_details, 
                                                                state=activity_state, 
                                                                url=streaming_url, 
                                                                buttons={activity_button_one: activity_button_one_answer, activity_button_two: activity_button_two_answer}, 
                                                                key=image_key, 
                                                                application_id=application_id
                                                                )
                                                                )
    msg = await ctx.message.edit(f"🕹️| State changé en `{activity_state}`")
    await asyncio.sleep(deltime)
    await msg.delete()

@bot.cmd(description='set rpc title')
async def rpc_url(ctx):
    message_split = ctx.message.content.split()
    streaming_url = ctx.message.content.replace(f"{message_split[0]} ", "")
    await bot.change_presence(status=config_selfbot.status_activity, 
                              afk=config_selfbot.afk, 
                              activity=selfcord.Activity.Stream(name=activity_name, 
                                                                details=activity_details, 
                                                                state=activity_state, 
                                                                url=streaming_url, 
                                                                buttons={activity_button_one: activity_button_one_answer, activity_button_two: activity_button_two_answer}, 
                                                                key=image_key, 
                                                                application_id=application_id
                                                                )
                                                                )
    msg = await ctx.message.edit(f"🕹️| Stream URL changé en `{streaming_url}`")
    await asyncio.sleep(deltime)
    await msg.delete()

@bot.cmd(description='set rpc title')
async def rpc_image(ctx):
    message_split = ctx.message.content.split()
    image_key = ctx.message.content.replace(f"{message_split[0]} ", "")
    await bot.change_presence(status=config_selfbot.status_activity, 
                              afk=config_selfbot.afk, 
                              activity=selfcord.Activity.Stream(name=activity_name, 
                                                                details=activity_details, 
                                                                state=activity_state, 
                                                                url=streaming_url, 
                                                                buttons={activity_button_one: activity_button_one_answer, activity_button_two: activity_button_two_answer}, 
                                                                key=image_key, 
                                                                application_id=application_id
                                                                )
                                                                )
    msg = await ctx.message.edit(f"🕹️| Image changé en `{image_key}`")
    await asyncio.sleep(deltime)
    await msg.delete()


@bot.cmd(description='set rpc title')
async def rpc_application_id(ctx):
    message_split = ctx.message.content.split()
    application_id = ctx.message.content.replace(f"{message_split[0]} ", "")
    await bot.change_presence(status=config_selfbot.status_activity, 
                              afk=config_selfbot.afk, 
                              activity=selfcord.Activity.Stream(name=activity_name, 
                                                                details=activity_details, 
                                                                state=activity_state, 
                                                                url=streaming_url, 
                                                                buttons={activity_button_one: activity_button_one_answer, activity_button_two: activity_button_two_answer}, 
                                                                key=image_key, 
                                                                application_id=application_id
                                                                )
                                                                )
    msg = await ctx.message.edit(f"🕹️| Application ID changé en `{application_id}`")
    await asyncio.sleep(deltime)
    await msg.delete()

@bot.cmd(description='set rpc title')
async def rpc_button_text_one(ctx):
    message_split = ctx.message.content.split()
    activity_button_one = ctx.message.content.replace(f"{message_split[0]} ", "")
    await bot.change_presence(status=config_selfbot.status_activity, 
                              afk=config_selfbot.afk, 
                              activity=selfcord.Activity.Stream(name=activity_name, 
                                                                details=activity_details, 
                                                                state=activity_state, 
                                                                url=streaming_url, 
                                                                buttons={activity_button_one: activity_button_one_answer, activity_button_two: activity_button_two_answer}, 
                                                                key=image_key, 
                                                                application_id=application_id
                                                                )
                                                                )
    msg = await ctx.message.edit(f"🕹️| Button One Text changé en `{activity_button_one}`")
    await asyncio.sleep(deltime)
    await msg.delete()

@bot.cmd(description='set rpc title')
async def rpc_button_text_two(ctx):
    message_split = ctx.message.content.split()
    activity_button_two = ctx.message.content.replace(f"{message_split[0]} ", "")
    await bot.change_presence(status=config_selfbot.status_activity, 
                              afk=config_selfbot.afk, 
                              activity=selfcord.Activity.Stream(name=activity_name, 
                                                                details=activity_details, 
                                                                state=activity_state, 
                                                                url=streaming_url, 
                                                                buttons={activity_button_one: activity_button_one_answer, activity_button_two: activity_button_two_answer}, 
                                                                key=image_key, 
                                                                application_id=application_id
                                                                )
                                                                )
    msg = await ctx.message.edit(f"🕹️|Button Text Two changé en `{activity_button_two}`")
    await asyncio.sleep(deltime)
    await msg.delete()

@bot.cmd(description='set rpc title')
async def rpc_button_link_one(ctx):
    message_split = ctx.message.content.split()
    activity_button_one_answer = ctx.message.content.replace(f"{message_split[0]} ", "")
    await bot.change_presence(status=config_selfbot.status_activity, 
                              afk=config_selfbot.afk, 
                              activity=selfcord.Activity.Stream(name=activity_name, 
                                                                details=activity_details, 
                                                                state=activity_state, 
                                                                url=streaming_url, 
                                                                buttons={activity_button_one: activity_button_one_answer, activity_button_two: activity_button_two_answer}, 
                                                                key=image_key, 
                                                                application_id=application_id
                                                                )
                                                                )
    msg = await ctx.message.edit(f"🕹️| Button One Link changé en `{activity_button_one_answer}`")
    await asyncio.sleep(deltime)
    await msg.delete()


@bot.cmd(description='set rpc title')
async def rpc_button_link_two(ctx):
    message_split = ctx.message.content.split()
    activity_button_two_answer = ctx.message.content.replace(f"{message_split[0]} ", "")
    await bot.change_presence(status=config_selfbot.status_activity, 
                              afk=config_selfbot.afk, 
                              activity=selfcord.Activity.Stream(name=activity_name, 
                                                                details=activity_details, 
                                                                state=activity_state, 
                                                                url=streaming_url, 
                                                                buttons={activity_button_one: activity_button_one_answer, activity_button_two: activity_button_two_answer}, 
                                                                key=image_key, 
                                                                application_id=application_id
                                                                )
                                                                )
    msg = await ctx.message.edit(f"🕹️| Button Link Two changé en `{activity_button_two_answer}`")
    await asyncio.sleep(deltime)
    await msg.delete()


@bot.cmd(description='set rpc title')
async def rpc_status(ctx):
    message_split = ctx.message.content.split()
    status_activity = ctx.message.content.replace(f"{message_split[0]} ", "")
    await bot.change_presence(status=config_selfbot.status_activity, 
                              afk=config_selfbot.afk, 
                              activity=selfcord.Activity.Stream(name=activity_name, 
                                                                details=activity_details, 
                                                                state=activity_state, 
                                                                url=streaming_url, 
                                                                buttons={activity_button_one: activity_button_one_answer, activity_button_two: activity_button_two_answer}, 
                                                                key=image_key, 
                                                                application_id=application_id
                                                                )
                                                                )
    msg = await ctx.message.edit(f"🕹️| RPC Status changé en `{status_activity}`")
    await asyncio.sleep(deltime)
    await msg.delete()



####################
# flood command    #
#      (it's very  #
#         big)     #
####################


@bot.cmd(description="flood")
async def flood(ctx):
    await ctx.message.edit("""_ _
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
_ _""")
    await asyncio.sleep(0.4)
    await ctx.channel.send("""_ _
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
_ _""") 
    await asyncio.sleep(0.4)
    await ctx.channel.send("""_ _
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
_ _""")
    await asyncio.sleep(0.4)
    await ctx.channel.send("""_ _
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
_ _""")

try:
    bot.run(token)
except Exception:
    print(Fore.RED, "[!!!]", Fore.LIGHTRED_EX, "Bad Token !")