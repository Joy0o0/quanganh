import asyncio
from typing import Text
from aiohttp.helpers import TOKEN
import os
import discord
import datetime
import random
from random import randint
import time
from discord import message
from discord import guild
from discord import channel
from discord import client
from discord import colour
from discord.ext import commands
from discord.ext.commands.core import command
from discord.ext.commands import Bot, guild_only
from discord.ext.commands.errors import NoEntryPointError


intents = discord.Intents.default()
intents.members = True

lucy = commands.Bot(command_prefix = 'n', intents=intents)
TOKEN = 'OTI4MTI3OTA2NDE1MjY3OTAy.YdUQeA.xfAWFZYiPBQDrGqtrU-g1OjbyyU'
time = datetime.datetime.now()
lucy.sniped_messages = {}



quanganh = commands.Bot(command_prefix = '')
    
print("Logged in as quanganh#5877")

@quanganh.command()
async def hello(ctx):
    await ctx.reply('Hello!')

@quanganh.command()
async def hi(ctx):
    await ctx.reply('chào bạn nhé')

@quanganh.command()
async def Hi(ctx):
    await ctx.reply('Chào bạn nhé!')

@quanganh.command()
async def Chào(ctx):
    await ctx.reply('hellooo ')

@quanganh.command()
async def chào(ctx):
    await ctx.reply('hellooo ')


#@quanganh.command()
#async def Phương(ctx):
#    await ctx.send('Phương yêu <@587207999882395648>  ')

#@quanganh.command()
#async def Hoàng(ctx):
#    await ctx.send('Hoàng yêu <@772118765705756712> ')

#@quanganh.command()
#async def Linh(ctx):
#    await ctx.send('Linh iu Đức ')

@quanganh.command()
async def phiphai(ctx):
    await ctx.send('sống dai thành huyền thoại')

@quanganh.command()
async def freefire(ctx):
    await ctx.send('sống dai thành huyền thoại')

@quanganh.command()
async def raid(ctx):
    await ctx.send('raid mẹ server đi dí cái lon đu má')

#@quanganh.command()
#async def Tinz(ctx):
#    await ctx.send('yêu Thảo Linh')

@quanganh.command()
async def Nhựt(ctx):
    await ctx.send('yêu 𝐖𝐢𝐥𝐥 ')


@quanganh.command()
async def Hello(ctx):
    await ctx.reply('Hello! <a:ST_godau:920249241597788170>')

@quanganh.command()
async def ngu(ctx):
    await ctx.reply('? ngu cc ')

@quanganh.command()
async def nRaid(ctx):
     await ctx.send('raid\nraid\nraid\nraid\nraid\nraid\nraid\nraid\nraid\nraid\nraid\nraid\nraid\nraid\nraid\nraid\nraid\nraid\nraid\nraid\nraid\nraid\nraid\nraid\nraid\nraid\nraid\nraid\nraid\nraid\nraid\nraid\nraid\nraid\nraid\nraid\n ')

@quanganh.command()
async def Owner(ctx):
    await ctx.send('<@455335800834359296> tệ vcl ')

@quanganh.command()
async def owner(ctx):
    await ctx.send('<@455335800834359296> tệ vcl  ')

@quanganh.command()
async def prefix(ctx):
    await ctx.reply('my prefix is n')

@quanganh.command()
async def tệ(ctx):
    await ctx.send('sống thế đéo nào người ta bảo tệ kìa ?')

@quanganh.command()
async def nrandom(ctx, range: int):
    await ctx.send(f'Số của bạn là: {randint(1, range)}')

@quanganh.command()
async def fbi(ctx):
    embed = discord.Embed(title = "FBI đây thằng lồn", color = discord.Colour.red())
    embed.set_image(url='https://i.pinimg.com/originals/e6/83/15/e683152889dc703c77ce5bada1e89705.gif')
    await ctx.send(embed = embed)

@quanganh.command()
async def nbc(ctx):
    baucua = [
        'Bầu', 'Cua','Tôm','Cá','Nai','Gà'
    ]
    a = random.choice(baucua)
    b = random.choice(baucua)
    c = random.choice(baucua)
    d =a +  ' ' + b + ' ' + c
    embed = discord.Embed(color = discord.Color.blue())
    embed.add_field(name = 'Bầu cua', value=d ,inline=False)
    await ctx.channel.send(embed=embed)

snipe_message_content = None
snipe_message_author = None
snipe_message_id = None
@quanganh.event
async def on_message_delete(message):
    global snipe_message_content
    global snipe_message_author
    global snipe_message_id

    snipe_message_content = message.content
    snipe_message_author = message.author
    snipe_message_id = message.id
    await asyncio.sleep(60)

    if message.id == snipe_message_id:
        snipe_message_author = None
        snipe_message_content = None
        snipe_message_id = None

@quanganh.command()
async def nsnipe(message):
    if snipe_message_content==None:
        await message.channel.send("Không tìm thấy tin nhắn!")
    else:
        embed = discord.Embed(description=f"{snipe_message_content}", color = discord.Color.blue())
        embed.set_footer(text=f"ID tin nhắn: {snipe_message_id}")
        embed.set_author(name=f"{snipe_message_author.name}#{snipe_message_author.discriminator}", icon_url=snipe_message_author.avatar_url)
        await message.channel.send(embed=embed)
        return

@quanganh.command()
async def npunch(ctx, member:discord.Member=None):
    if member != None:
        punch = [
            'https://i.pinimg.com/originals/8d/50/60/8d50607e59db86b5afcc21304194ba57.gif',
            'https://i.pinimg.com/originals/3b/b2/02/3bb2023cc65482bc6660120cfa7623e8.gif',
            'https://i.pinimg.com/originals/bf/a3/b6/bfa3b6b9cf23145f0b13b879f568433c.gif',
            'https://i.pinimg.com/originals/2b/a0/03/2ba0035666157ac1181d9be7d7dbf635.gif',
            'https://i.pinimg.com/originals/b7/11/1b/b7111bef6f73d827ff3d8e19d2b392f4.gif',
            'https://i.pinimg.com/originals/e4/16/32/e41632c40770852bd304f8e19bcb3108.gif',
            'https://i.pinimg.com/originals/40/b3/69/40b369c95c91914fcbb339090e58df4a.gif',
            'https://i.pinimg.com/originals/8d/e9/92/8de99269d67653248d65d83eb27cfc8b.gif',
            'https://gifimage.net/wp-content/uploads/2017/09/anime-punch-in-the-face-gif-3.gif',
            'https://pa1.narvii.com/5668/d845ea44f1ce209351976f2a22b4c728873fac21_hq.gif',
            'https://i1.wp.com/myotakuworld.com/wp-content/uploads/2020/06/Kamui-Punch%E2%80%99s-Nobunobu-1.gif?resize=540%2C304&ssl=1',
            'https://i0.wp.com/myotakuworld.com/wp-content/uploads/2020/06/Apachai-Hopachai-1.gif?resize=500%2C224&ssl=1',
            'https://i.pinimg.com/originals/53/31/bf/5331bfe64d40dee341a7b9c67f73d383.gif',
            'https://i.pinimg.com/originals/58/52/5c/58525c46daf52a150b705caa3387e035.gif',
            'https://i.pinimg.com/originals/79/9e/f9/799ef9d0043d2bfb6eee7ae698e1f204.gif'
        ]
        if member.id == ctx.author.id:
            await ctx.send('Aw, sao lại đấm chính mình thế ÓwÒ')
        else:
            embed = discord.Embed(title = f'{ctx.author.name} vừa đấm {member.name}',color = discord.Colour.blue())
            embed.set_footer(icon_url = ctx.author.avatar_url, text = time.strftime("%H:%M") +f" - Requested by {ctx.author.name}")
            embed.set_image(url = random.choice(punch))
            await ctx.send(embed=embed) 
    else:
        await ctx.channel.send('Cần ping thành viên để dùng lệnh')   

@quanganh.command()
async def hug(ctx, member:discord.Member=None):
    hug = [
        'https://i.pinimg.com/originals/52/6f/9e/526f9edaf5414c5406434ea29c776b9d.gif',
        'https://i.pinimg.com/originals/be/8d/41/be8d41333e616efab00959dde69ae8f0.gif',
        'https://i.pinimg.com/originals/ef/b6/e3/efb6e37a8a31e47b1ea969833555b4b6.gif',
        'https://i.pinimg.com/originals/c8/67/f6/c867f6e32eb7bc81760015dfc08f4d05.gif',
        'https://i.pinimg.com/originals/96/9f/0f/969f0f462e4b7350da543f0231ba94cb.gif',
        'https://i.pinimg.com/originals/0a/d6/93/0ad693eaef0cde71f7001a3ecbded6c9.gif',
        'https://i.pinimg.com/originals/83/b7/32/83b732c53bfdd1409aec0553f9bfacfd.gif',
        'https://i.pinimg.com/originals/88/a6/7c/88a67cbf4dfdf4b93834d467eed01979.gif',
        'https://i.pinimg.com/originals/42/92/2e/42922e87b3ec288b11f59ba7f3cc6393.gif',
        'https://i.pinimg.com/originals/5d/93/f4/5d93f4ca1115d4f9e01a67ba9250f14f.gif',
        'https://i.pinimg.com/originals/8d/8f/08/8d8f08ebd8ef64d4422e7becfaa0e448.gif',
        'https://i.pinimg.com/originals/94/98/9f/94989f6312726739893d41231942bb1b.gif',
        'https://i.pinimg.com/originals/06/dd/8f/06dd8f976b7353d69aec173b44927ef4.gif',
        'https://i.pinimg.com/originals/3d/06/31/3d0631e61cb528e3263506a4f08b3675.gif',
        'https://i.pinimg.com/originals/a8/f2/f6/a8f2f612ab90fec87a14e4266d04b812.gif'
    ]
    if member.id == ctx.author.id:
        await ctx.send('Sao ôm chính mình thế em, tự luyến ak em :> ?')
    else:
        embed = discord.Embed(title = f'{ctx.author.name} vừa ôm {member.name}',color = discord.Colour.blue())
        embed.set_footer(icon_url = ctx.author.avatar_url, text = time.strftime("%H:%M") +f" - Requested by {ctx.author.name}")
        embed.set_image(url = random.choice(hug))
        await ctx.send(embed=embed)

@quanganh.command()
async def nhug(ctx, member:discord.Member=None):
    hug = [
        'https://i.pinimg.com/originals/52/6f/9e/526f9edaf5414c5406434ea29c776b9d.gif',
        'https://i.pinimg.com/originals/be/8d/41/be8d41333e616efab00959dde69ae8f0.gif',
        'https://i.pinimg.com/originals/ef/b6/e3/efb6e37a8a31e47b1ea969833555b4b6.gif',
        'https://i.pinimg.com/originals/c8/67/f6/c867f6e32eb7bc81760015dfc08f4d05.gif',
        'https://i.pinimg.com/originals/96/9f/0f/969f0f462e4b7350da543f0231ba94cb.gif',
        'https://i.pinimg.com/originals/0a/d6/93/0ad693eaef0cde71f7001a3ecbded6c9.gif',
        'https://i.pinimg.com/originals/83/b7/32/83b732c53bfdd1409aec0553f9bfacfd.gif',
        'https://i.pinimg.com/originals/88/a6/7c/88a67cbf4dfdf4b93834d467eed01979.gif',
        'https://i.pinimg.com/originals/42/92/2e/42922e87b3ec288b11f59ba7f3cc6393.gif',
        'https://i.pinimg.com/originals/5d/93/f4/5d93f4ca1115d4f9e01a67ba9250f14f.gif',
        'https://i.pinimg.com/originals/8d/8f/08/8d8f08ebd8ef64d4422e7becfaa0e448.gif',
        'https://i.pinimg.com/originals/94/98/9f/94989f6312726739893d41231942bb1b.gif',
        'https://i.pinimg.com/originals/06/dd/8f/06dd8f976b7353d69aec173b44927ef4.gif',
        'https://i.pinimg.com/originals/3d/06/31/3d0631e61cb528e3263506a4f08b3675.gif',
        'https://i.pinimg.com/originals/a8/f2/f6/a8f2f612ab90fec87a14e4266d04b812.gif'
    ]
    if member.id == ctx.author.id:
        await ctx.send('Sao ôm chính mình thế em, tự luyến ak em :> ?')
    else:
        embed = discord.Embed(title = f'{ctx.author.name} vừa ôm {member.name}',color = discord.Colour.blue())
        embed.set_footer(icon_url = ctx.author.avatar_url, text = time.strftime("%H:%M") +f" - Requested by {ctx.author.name}")
        embed.set_image(url = random.choice(hug))
        await ctx.send(embed=embed)

@quanganh.command()
async def nkiss(ctx, member:discord.Member=None):
    kiss = [
        'https://i.pinimg.com/originals/d5/1b/f7/d51bf72501ce723a579ea45396ef4bc6.gif',
        'https://i.pinimg.com/originals/36/86/02/368602e5a4262aa4052bfe1a0addeb12.gif',
        'https://i.pinimg.com/originals/ec/89/36/ec8936fc307d2cd3c71c6100a99dfc0d.gif',
        'https://i.pinimg.com/originals/92/2e/da/922eda2bcaacce3a80d1944177c61933.gif',
        'https://i.pinimg.com/originals/fc/b2/09/fcb2094674122f0b829016352f511f92.gif',
        'https://i.pinimg.com/originals/b2/0f/e0/b20fe027ba2f488d72d890ddc2b927ab.gif',
        'https://i.pinimg.com/originals/ed/52/90/ed52908adf694ba04a73b8f43c117796.gif',
        'https://i.pinimg.com/originals/c0/9d/0d/c09d0d5a6dd73402d37f81b465af62de.gif'
    ]
    if member.id == ctx.author.id:
        await ctx.send('Tự luyến có mức độ thôi em, đừng quá')
    else:
        embed = discord.Embed(title = f'{ctx.author.name} vừa hôn {member.name}',color = discord.Colour.blue())
        embed.set_footer(icon_url = ctx.author.avatar_url, text = time.strftime("%H:%M") +f" - Requested by {ctx.author.name}")
        embed.set_image(url = random.choice(kiss))
        await ctx.send(embed=embed)

@quanganh.command()
async def nslap(ctx, member:discord.Member=None):
    slap = [
        'https://i.pinimg.com/originals/c7/2f/e9/c72fe91601066cc6ec83580b3310b45c.gif',
        'https://i.pinimg.com/originals/d1/49/69/d14969a21a96ec46f61770c50fccf24f.gif',
        'https://i.pinimg.com/originals/65/6c/0a/656c0ae24dc099999bc5574e33f2ecf4.gif',
        'https://i.pinimg.com/originals/40/ef/24/40ef24388a01ba9be6da6dea69d30fda.gif',
        'https://i.pinimg.com/originals/b7/a8/44/b7a844cc66ca1c6a4f06c266646d070f.gif',
        'https://i.pinimg.com/originals/65/57/f6/6557f684d6ffcd3cd4558f695c6d8956.gif',
        'https://i.pinimg.com/originals/8c/a5/fc/8ca5fc2e6657e04b6a4236cf3dcc3f6b.gif',
        'https://i.pinimg.com/originals/48/30/a3/4830a35f081b6fd856165ddcf0624b3d.gif',
        'https://i.pinimg.com/originals/df/c9/bd/dfc9bdbabda5045d55ba7f0a1a9f5135.gif',
        'https://i.pinimg.com/originals/ee/9b/65/ee9b656ec7062a00494f7f56e043b0d4.gif',
        'https://i.pinimg.com/originals/66/6e/ee/666eeeb7c73ca062dc3491622306bf36.gif',
        'https://i.pinimg.com/originals/01/5e/18/015e18721c72e62184409cedb7e57888.gif',
        'https://i.pinimg.com/originals/0f/1c/10/0f1c10c4298b7c3143cd9b251fcba791.gif',
        'https://i.pinimg.com/originals/6f/3b/ed/6f3bed83654dbd1c5d9fd9f4ea746e8a.gif',
        'https://i.pinimg.com/originals/1f/36/7f/1f367ff51cee54ae921142d41daaa20f.gif'
    ]
    if member.id == ctx.author.id:
        await ctx.send('Aw, sao lại tát chính mình thế, phải tát mạnh hơn chứ :)))')
    else:
        embed = discord.Embed(title = f'{ctx.author.name} vừa tát {member.name}',color = discord.Colour.blue())
        embed.set_footer(icon_url = ctx.author.avatar_url, text = time.strftime("%H:%M") +f" - Requested by {ctx.author.name}")
        embed.set_image(url = random.choice(slap))
        await ctx.send(embed=embed)

@quanganh.command()
async def nsmile(ctx):
    smile = [
        'https://i.pinimg.com/originals/c4/9d/c9/c49dc9422aac61eebbf8ae9d42bb26b7.gif',
        'https://i.pinimg.com/originals/ca/8b/df/ca8bdf23f33469f5eb0d2ba44aef6593.gif',
        'https://i.pinimg.com/originals/bc/11/80/bc11809c97271e15b7495b7ccd880ab7.gif',
        'https://i.pinimg.com/originals/37/19/a5/3719a55afa6d78768d68a1b26fd3dc49.gif',
        'https://i.pinimg.com/originals/10/02/67/100267c958fe4e56aecfbc969d42f3ce.gif',
        'https://i.pinimg.com/originals/01/49/4d/01494db608809aa11df515fadbc545ef.gif',
        'https://i.pinimg.com/originals/50/1c/6b/501c6b26d450c96c12bc9c7eee593336.gif',
        'https://i.pinimg.com/originals/c8/56/4a/c8564a53ab234f0ff5a4f6f5f92f9650.gif'
    ]
    embed = discord.Embed(title = f'{ctx.author.name} cười kìa, đụ má, hề vãi.',color = discord.Colour.blue())
    embed.set_footer(icon_url = ctx.author.avatar_url, text = time.strftime("%H:%M") +f" - Requested by {ctx.author.name}")
    embed.set_image(url = random.choice(smile))
    await ctx.send(embed=embed) 


@quanganh.command()
async def nhelp(ctx):
    embed = discord.Embed(
        title = 'Command',
        description = '',
        color = discord.Colour.blue()
    )
    embed.add_field(name="Actions", value="punch, slap, cry, hug, kiss, snipe", inline=False)
    embed.add_field(name="Emotes", value="cry", inline=False)
    embed.add_field(name="Moderation", value="ban, unban, kick", inline=False)
    await ctx.send(embed=embed)

@quanganh.command()
async def ncry(ctx):
    cry = [
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        ''
    ]
    embed = discord.Embed(title = f'{ctx.author.name} khóc rồi, ai dỗ đi >:(',color = discord.Colour.red())
    embed.set_image(url = random.choice(cry))
    await ctx.send(embed=embed)    



@quanganh.command()
async def ninvite(ctx):
    await ctx.reply('https://discord.com/api/oauth2/authorize?client_id=928127906415267902&permissions=8&scope=bot')

@quanganh.command()
async def npat(ctx, member:discord.Member=None):
    pat= [
        'https://i.pinimg.com/originals/a4/ff/aa/a4ffaa47407de70db28c57a25a557efb.gif',
        'https://i.pinimg.com/originals/71/e7/42/71e74263a48a6e9a2c53f3bc1439c3ac.gif',
        'https://i.pinimg.com/originals/d7/c3/26/d7c326bd43776f1e0df6f63956230eb4.gif',
        'https://i.pinimg.com/originals/5a/69/2d/5a692dc246f2468ca0e37446b4964054.gif',
        'https://i.pinimg.com/originals/c7/18/d7/c718d7517aec454697998c68ab0cd2fb.gif',
        'https://i.pinimg.com/originals/61/51/c4/6151c42c94df654b1c7de2fdebaa6bd1.gif',
        'https://i.pinimg.com/originals/70/96/0e/70960e87fb9454df6a1d15c96c9ad955.gif'
    ]
    if member.id == ctx.author.id:
        await ctx.send('Aw, hãy để tôi xoa đầu bạn')
    else:
        embed = discord.Embed(title = f'{ctx.author.name} vừa xoa đầu {member.name}',color = discord.Colour.blue())
        embed.set_image(url = random.choice(pat))
        await ctx.send(embed=embed) 

@quanganh.command()
async def nship(ctx,member1:discord.Member,member2:discord.Member):
    per = random.randint(1,100)
    if  (member1.id == 839053812803043368) or (member2.id  == 839053812803043368):
        if (member1.id == 868127101142859827) or (member2.id == 868127101142859827):
            embed = discord.Embed(title=f'Chỉ số ship của {member1.name} và {member2.name} là 100%. Cố gắng luôn giữ nó ở mức này nhé ÒwÓ.', color = discord.Colour.green())
            embed.set_image(url='https://i.pinimg.com/originals/2b/51/0f/2b510fbba385a28885942e1a98ff6d0c.gif')
            embed.set_footer(icon_url = ctx.author.avatar_url, text = time.strftime("%H:%M") +f" - Requested by {ctx.author.name}")
            await ctx.channel.send(embed=embed)
        else:
            embed = discord.Embed(title=f'Chỉ số ship của {member1.name} và {member2.name} là -1%. Rất tiếc cho bạn nhưng không sao, cố gắng để đạt 100%' + ' nhé ÓwÒ', color = discord.Colour.green())
            embed.set_image(url='https://i.pinimg.com/originals/ef/5f/11/ef5f112be2952c59c4bc5668465439b1.gif')
            embed.set_footer(icon_url = ctx.author.avatar_url, text = time.strftime("%H:%M") +f" - Requested by {ctx.author.name}")
            await ctx.channel.send(embed=embed)
    else:
        if per < 50:
            embed = discord.Embed(title=f'Chỉ số ship của {member1.name} và {member2.name} là '+ str(per) + '%. Rất tiếc cho bạn nhưng không sao, cố gắng để đạt 100%' + ' nhé ÓwÒ', color = discord.Colour.green())
            embed.set_image(url='https://i.pinimg.com/originals/ef/5f/11/ef5f112be2952c59c4bc5668465439b1.gif')
            embed.set_footer(icon_url = ctx.author.avatar_url, text = time.strftime("%H:%M") +f" - Requested by {ctx.author.name}")
            await ctx.channel.send(embed=embed)
        else:
            embed = discord.Embed(title=f'Chỉ số ship của {member1.name} và {member2.name} là '+ str(per) + '%. Cố gắng luôn giữ nó ở mức này nhé ÒwÓ.', color = discord.Colour.green())
            embed.set_image(url='https://i.pinimg.com/originals/2b/51/0f/2b510fbba385a28885942e1a98ff6d0c.gif')
            embed.set_footer(icon_url = ctx.author.avatar_url, text = time.strftime("%H:%M") +f" - Requested by {ctx.author.name}")
            await ctx.channel.send(embed=embed)


@quanganh.command()
async def navatar(ctx, member : discord.Member = None):
    embed = discord.Embed(
        title = 'Avatar',
        description = '',
        colour = discord.Color.blue()
    )
    if member == None:
        embed = discord.Embed(title = "Avatar")
        embed.set_image(url = ctx.author.avatar_url)
        embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)

    else:
        embed = discord.Embed(title = "Avatar")
        embed.set_image(url = member.avatar_url)
        embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)

@quanganh.command
async def roll(ctx):
    await ctx.send(random.randint(1, ctx))


@quanganh.command()
@commands.has_permissions(kick_members = True)
async def nkick(ctx, member:discord.Member,*,reason = 'No reason provided'):
    embed = discord.Embed(title=f'{member.name} vừa bị kick khỏi {ctx.message.guild.name} bởi {ctx.author.name}', color = discord.Colour.red())
    await member.kick(reason=reason)
    await ctx.send(embed=embed)


@quanganh.command(aliases = ['b'])
@commands.has_permissions(ban_members = True)
async def nban(ctx, member:discord.Member,*,reason = 'No reason provided',):
    if ctx.message.author.guild_permissions.administrator:
        embed = discord.Embed(title=f'{member.name} vừa bị ban khỏi {ctx.message.guild.name}', color = discord.Colour.red())
        await ctx.send(embed=embed)
        await member.ban(reason=reason)


@quanganh.command()
async def nunban(ctx, id: int):
    usern = quanganh.get_user(id)
    user = await quanganh.fetch_user(id)

    embed = discord.Embed(title = f'Unban thành công bởi {ctx.author.name}',color = discord.Colour.green())
    await ctx.guild.unban(user)
    await ctx.send(embed=embed)





quanganh.run(TOKEN)

#######################################################################################################
