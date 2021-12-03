import discord
import discord.utils
from discord import Member
from discord.ext import commands
from discord.ext import tasks
from discord.ext.commands import Bot
import random
import asyncio

keshi = commands.Bot(command_prefix='k!', help_command=None)

@keshi.event
async def on_ready():
    await keshi.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching, name='Server Mommy || DM Moderator untuk Report'))
    print('KeshiBot online')


# (activity=discord.Streaming(name='Sea of Thieves', url='https://www.twitch.tv/your_channel_here')) LIVE
# (activity=discord.Activity(type=discord.ActivityType.watching, name='Server Mommy || DM Moderator untuk report ya!')) NORMAL

@keshi.event
async def on_message(message):
    if keshi.user.mentioned_in(message):
        variable = [
            'https://media1.tenor.com/images/f6fe8d1d0463f4e51b6367bbecf56a3e/tenor.gif?itemid=6198981',
        ]
        embed = discord.Embed(title='Meow', description=f'Nyahaloo~ {message.author.mention}!, untuk report, jangan lupa DM aku aja nyaaaa~')
        embed.set_image(url=random.choice(variable))
        if (message.author.bot): return;
        await message.channel.send(embed=embed )


    if 'pagi keshi' in message.content:
        if (message.author.bot): return;
        await message.channel.send(f'Pagi Nyaa {message.author.mention}')

    if 'Pagi Keshi' in message.content:
        if (message.author.bot): return;
        await message.channel.send(f'Pagi Nyaa {message.author.mention}')

    if 'Pagi keshi' in message.content:
        if (message.author.bot): return;
        await message.channel.send(f'Pagi Nyaa {message.author.mention}')

    if 'PAGI KESHI' in message.content:
        if (message.author.bot): return;
        await message.channel.send(f'Pagi Nyaa {message.author.mention}')

    if 'siang keshi' in message.content:
        if (message.author.bot): return;
        await message.channel.send(f'Siang Nyaa {message.author.mention}')

    if 'Siang keshi' in message.content:
        if (message.author.bot): return;
        await message.channel.send(f'Siang Nyaa {message.author.mention}')

    if 'Siang Keshi' in message.content:
        if (message.author.bot): return;
        await message.channel.send(f'Siang Nyaa {message.author.mention}')

    if 'SIANG KESHI' in message.content:
        if (message.author.bot): return;
        await message.channel.send(f'Siang Nyaa {message.author.mention}')

    if 'sore keshi' in message.content:
        if (message.author.bot): return;
        await message.channel.send(f'Sore Nyaa {message.author.mention}')

    if 'Sore keshi' in message.content:
        if (message.author.bot): return;
        await message.channel.send(f'Sore Nyaa {message.author.mention}')

    if 'Sore Keshi' in message.content:
        if (message.author.bot): return;
        await message.channel.send(f'Sore Nyaa {message.author.mention}')

    if 'SORE KESHI' in message.content:
        if (message.author.bot): return;
        await message.channel.send(f'Sore Nyaa {message.author.mention}')

    if 'Malam Keshi' in message.content:
        if (message.author.bot): return;
        await message.channel.send(f'Malam Nyaa {message.author.mention}')

    if 'malam keshi' in message.content:
        if (message.author.bot): return;
        await message.channel.send(f'Malam Nyaa {message.author.mention}')

    if 'MALAM KESHI' in message.content:
        if (message.author.bot): return;
        await message.channel.send(f'Malam Nyaa {message.author.mention}')

    if 'Malam keshi' in message.content:
        if (message.author.bot): return;
        await message.channel.send(f'Malam Nyaa {message.author.mention}')

    if ' Iri ' in message.content:
        variable = [
            'https://media1.tenor.com/images/986ac46406928712ebc36435948dc6b4/tenor.gif',
        ]
        embed = discord.Embed(title='Meow',description=f'HEM {message.author.mention}')
        embed.set_image(url=random.choice(variable))
        if (message.author.bot): return;
        await message.channel.send(embed=embed)

    if ' iri ' in message.content:
        variable = [
            'https://media1.tenor.com/images/986ac46406928712ebc36435948dc6b4/tenor.gif',
        ]
        embed = discord.Embed(title='Meow',description=f'HEM {message.author.mention}')
        embed.set_image(url=random.choice(variable))
        if (message.author.bot): return;
        await message.channel.send(embed=embed)

    await keshi.process_commands(message)

@keshi.command(aliases=['Kick', 'KICK'])
async def kick (ctx, member: discord.Member=None):
    if not member:
        # We dont have anyone to mention so tell the user
        await ctx.send("Please tag the user you wish to interact with")
        return

    variable=[
        'https://media1.tenor.com/images/dddc6e263456df2af41a93e123a7622a/tenor.gif',
        'https://i.gifer.com/QVlJ.gif',
        'https://media.tenor.com/images/22bfaf74d8f0a76ea0c63a383e483fc4/tenor.gif',
        'https://i.gifer.com/ACKR.gif',
        'https://media1.tenor.com/images/d4bd24c980e46c66f67077aff59f0565/tenor.gif',
        'https://i.makeagif.com/media/12-08-2015/1WELz7.gif',
        ]
    embed = discord.Embed(description=f'{ctx.message.author.mention} menendang {member.mention}')
    embed.set_image(url=random.choice(variable))
    await ctx.send(embed=embed)

@keshi.command(aliases=['Slam', 'SLAM'])
async def slam (ctx, member: discord.Member=None):
    if not member:
        # We dont have anyone to mention so tell the user
        await ctx.send("Please tag the user you wish to interact with")
        return

    variable=[
        'https://media.tenor.com/images/9a4d2a49a651d0bbc23e4b0530861528/tenor.gif',
        'https://media1.giphy.com/media/bzsbT0mdQooKEIVyHc/giphy.gif',
        'https://media1.tenor.com/images/8bbe6be3a459ff7415dbda18d1409930/tenor.gif',
    ]
    embed = discord.Embed(description=f'{ctx.message.author.mention} membanting {member.mention}')
    embed.set_image(url=random.choice(variable))
    await ctx.send(embed=embed)

@keshi.command(aliases=['Kiss', 'KISS'])
async def kiss (ctx, member: discord.Member=None):
    if not member:
        # We dont have anyone to mention so tell the user
        await ctx.send("Please tag the user you wish to interact with")
        return

    variable=[
        'https://pa1.narvii.com/6049/7bfe768fe464171b5687cda04d52995834606980_hq.gif',
        'https://i.pinimg.com/originals/32/d4/f0/32d4f0642ebb373e3eb072b2b91e6064.gif',
        'https://i.pinimg.com/originals/39/3f/c3/393fc3ee25ab2bed1a60d87c86bad3b0.gif',
        ]
    embed = discord.Embed(description=f'{ctx.message.author.mention} mencium {member.mention}')
    embed.set_image(url=random.choice(variable))
    await ctx.send(embed=embed)

@keshi.command(aliases=['Punch', 'PUNCH'])
async def punch (ctx, member: discord.Member=None):
    if not member:
        # We dont have anyone to mention so tell the user
        await ctx.send("Please tag the user you wish to interact with")
        return

    variable=[
        'https://i.gifer.com/Aq6y.gif',
        'https://i.pinimg.com/originals/3a/a4/b8/3aa4b8cd43153e81cd03376f342efccf.gif',
        'https://i.gifer.com/9eUJ.gif',
        ]
    embed = discord.Embed(description=f'{ctx.message.author.mention} memukul {member.mention}')
    embed.set_image(url=random.choice(variable))
    await ctx.send(embed=embed)

@keshi.command(aliases=['Tanya', 'TANYA'])
async def tanya(ctx, question=None):
    outcome = ['Tentu Nyaa!',
               'Pasti Nyaa! Keshi jamin',
               'Sudah Jelas Nyaa!',
               'Kemungkinannya Besar Nyaa!',
               'Sangat Mungkin Nyaaa!',
               'Humm, Mungkin Tidak Nyaa..',
               'Kemungkinannya agak kecil sih Nyaoo..',
               'Hum harusnya tidak... Nyaoo...',
               'Tidak Nyaaoo',
               'Tidak Mungkin Nyaoo']
    if question is None:
        await ctx.send(f'Keshi kurang tau kamu mau bertanya tentang apa nyaaann {ctx.message.author.mention}')
    elif 'Alice' in question:
        await ctx.send (f'Keshi kurang tau Nyaa Keshi kan cuman Kocheng kesayangan Alice Nyaa {ctx.message.author.mention}')
    elif 'alice' in question:
        await ctx.send(f'Keshi kurang tau Nyaa Keshi kan cuman Kocheng kesayangan Alice Nyaa {ctx.message.author.mention}')
    else:
        await ctx.send(f'{random.choice(outcome)} {ctx.message.author.mention}')

@keshi.command()
async def pilih (ctx,args1,args2):
    variable = [args1, args2]
    await ctx.send(f'Keshi pilih {random.choice(variable)}')

@keshi.command()
async def roll (ctx):
    variable = ['https://media.tenor.com/images/772e46e6f8d1b342753ebb988ae7ed57/tenor.gif']
    embed = discord.Embed(title='Nyaoo')
    embed.set_image(url=random.choice(variable))
    await ctx.send(embed=embed)
        
@keshi.command()
async def funfact (ctx):
    funfact = ['lemon mengandung banyak gula daripada stroberi',
               'Huruf yang paling sering digunakan adalah huruf E dan huruf Q adalah yang paling jarang dipakai',
               'Secara resmi setiap tanggal 6 Oktober di Jepang merayakan Tom Cruise Day.',
               'Jembatan suramadu (surabaya-madura) adalah jembatan terpanjang di Asia Tenggara (5438 m).',
               'Rafflesia Arnoldii yang tumbuh di Sumatera adalah bunga terbesar di dunia. Ketika bunganya mekar, diameternya mencapai 1 meter.',
               'Tertawa dan bahagia meningkatkan imun, terutama produksi sel-sel pembunuh alamiah yang membantu melindungi tubuh dari penyakit.',
               'Orang yang membayangkan suara baru yang belum pernah didengar, atau menggabungkan sebuah melodi matanya akan bergerak ke kiri',
               'Menara Eiffel dibangun oleh Alexandre Eiffel, dan sebagian besar biayanya ditanggung oleh dia.',
               'Rata-rata orang di dunia jatuh cinta sebanyak 7 kali dulu sebelum ditakdirkan menikah.',
               'Ken Edwards seorang pria asal Inggris memegang rekor Guinness untuk makan 36 kecoa dalam 1 menit.',
               'Energi yang dihasilkan oleh angin ribut (topan) selama 10 menit lebih besar dibandingkan energi dari bom saat perang',
               'Lagu kebangsaan Yunani mempunyai 158 bait.',
               'Bobby Tufts (4 tahun) adalah Wali Kota termuda di dunia saat ini (Wali Kota Dorset, Minnesota, AS).',
               'Kata “Poli” berarti Banyak dan “Tics” berarti Makhluk Pengisap Darah. Jadi kata Politics (politik) berarti Banyak Makhluk Pengisap Darah.',
               'Musik dapat membuat otak bahagia dan kebanyakan mendengarkan musik dapat membuat perut cepat lapar.'
               'Letusan gunung Tambora mengilhami penemuan sepeda, karena bnyk hewan transportasi menjadi mati akibat dr prubahan cuaca yg ekstrem saat itu.',
               'Tertawa sebanyak 100 kali setara dengan mendayung selama 10 menit. [Dr William Fry dari Stanford Medical School]',
               'Di Italia, dalam aturannya minuman Cappuccino hanya boleh di minum sebelum waktu siang',
               'Koin ¥ 1 (Yen Jepang) bisa mengapung di atas air.',
               'Di Cape Town, Afrika Selatan, remaja laki-laki yang memiliki gigi ompong dianggap tampan / maskulin.',
               'Kata “Mouse” (tikus) berasal dari turunan Bahasa Sansekerta “Mus” yang berarti “pencuri”. 48. Berjalan kaki atau bersepeda ke sekolah mempertajam konsentrasi siswa di kelas dan tetap bertahan sekitar 4 jam kemudian. [Medical Daily]',
               'Rata-rata orang akan merasa 100 persen sehat / fit hanya 61 hari dalam setahun. [penelitian di Inggris]',
               'Polydactyl Cat adalah jenis kucing yang memiliki jempol di kaki mereka.',
               'Ketika kita sedang jatuh cinta, otak akan memproduksi dopamin ekstra, bahan kimia yang membuat seseorang menjadi gembira berlebihan.',
               '“Mwahahaha” dan “lolz” telah ditambahkan ke Kamus Inggris Oxford.',
               'Menurut penelitian, pria cenderung menurunkan volume suaranya ketika ia berbicara dg seseorang yg ia cintai, sementara perempuan sebaliknya.',
               'Jerapah memiliki lidah sepanjang 21 inchi.',
               'Sepeda pertama dibuat pada tahun 1817 dibuat tanpa pedal.',
               'Balon mainan yang pertama kali terbuat dari karet vulkansir.',
               'Semut tidak pernah tidur.']
    await ctx.send(f'{ctx.message.author.mention}, kamu tau nggak kalau {random.choice(funfact)} Nyaa')

@keshi.command()
async def hug (ctx):
    if not member:
        # We dont have anyone to mention so tell the user
        await ctx.send("Please tag the user you wish to interact with")
        return

    variable=[
        '',
        ]
    embed = discord.Embed(description=f'{ctx.message.author.mention} memeluk {member.mention}')
    embed.set_image(url=random.choice(variable))
    await ctx.send(embed=embed)

@keshi.command()
async def slap (ctx):
    if not member:
        # We dont have anyone to mention so tell the user
        await ctx.send("Please tag the user you wish to interact with")
        return

    variable=[
        '',
        ]
    embed = discord.Embed(description=f'{ctx.message.author.mention} menampar {member.mention}')
    embed.set_image(url=random.choice(variable))
    await ctx.send(embed=embed)

@keshi.command()
async def help (ctx):
    await ctx.send('Saya sibuk gan, jadi command" lain menyusul -Frans')


@keshi.command(aliases=['updates', 'patch', 'UPDATE', 'Update', 'update'])
async def patchnotes (ctx):
    embed = discord.Embed(title='Patch Notes for KeshiBot', description=f'requested by {ctx.message.author.mention}')
    embed.set_author(name='LATEST PATCH!')
    embed.add_field(name='New Features!', value='```Added k!janken with alias k! + (janken/gbk/guntingbatukertas)```')
    embed.add_field(name='Fixes, Removal, Update Notes', value="```Removed a few lines of code that interacts with specific words.```")
    embed.add_field(name='Next Patch!', value='```Currently, KeshiBot is being rewritten for performance issues (mainly relating to the many if statements made on the previous code)```')

    await ctx.send(embed=embed)

@keshi.command(aliases=['notice','note'])
async def Notice (ctx):

    embed = discord.Embed(title=f"Developer's notes",description=f'Requested by {ctx.message.author.mention}')
    embed.set_author(name='NOTICE!')
    embed.add_field(name='Bot Status',value='KeshiBot is currently being rewritten in Python and JS, so a few features might not be stable for the time being.')
    embed.add_field(name='Contact:',value='if you have any ideas on new features, or want to contribute something, just message me on Discord! <@787968792541265982>')
    embed.add_field(name='KeshiDev',value='<@787968792541265982>')

    await ctx.send(embed=embed)

@keshi.command(aliases=['janken', 'guntingbatukertas', 'gbk'])
async def gunbaker (ctx,args1):
   answer = args1.lower()
   guntingbatukertas = ['gunting', 'batu', 'kertas']
   cc = random.choice(guntingbatukertas)
   if answer not in guntingbatukertas:
       await ctx.send ("Ndak ada pilihan itu nyaa!")
   else:
       if answer == cc:
           await ctx.send('Keshi shoots.. ')
           await ctx.send(cc)
           await ctx.send(f'{ctx.message.author.mention} Seri nyaa!')
       elif answer == 'gunting':
           if cc == 'batu':
               await ctx.send('Keshi shoots.. ')
               await ctx.send(cc)
               await ctx.send(f'{ctx.message.author.mention} kalah nyaa!')
           elif cc == 'kertas':
               await ctx.send('Keshi shoots.. ')
               await ctx.send(cc)
               await ctx.send(f'{ctx.message.author.mention} menang nyaa!')
       elif answer == 'batu':
           if cc == 'kertas':
               await ctx.send('Keshi shoots.. ')
               await ctx.send(cc)
               await ctx.send(f'{ctx.message.author.mention} kalah nyaa!')
           elif cc == 'gunting':
               await ctx.send('Keshi shoots.. ')
               await ctx.send(cc)
               await ctx.send(f'{ctx.message.author.mention} menang nyaa!')
       elif answer == 'kertas':
           if cc == 'gunting':
               await ctx.send('Keshi shoots.. ')
               await ctx.send(cc)
               await ctx.send(f'{ctx.message.author.mention} kalah nyaa!')
           elif cc == 'batu':
               await ctx.send('Keshi shoots.. ')
               await ctx.send(cc)
               await ctx.send(f'{ctx.message.author.mention} menang nyaa!')

@keshi.command(aliases=['pfp', 'PFP', 'Pfp', 'Avatar', 'PP', 'pp'])
async def avatar(ctx,member : discord.Member=None):
    if not member:
        embed = discord.Embed(title=f'Get Avatar', description=f'Requested by : {ctx.message.author.mention}')
        embed.set_author(name='Keshi v1.0rev4')
        embed.add_field(name='Profile Picture Saha?', value='Cannot Find member :( mungkin namanya salah nyaa!')
        return

    embed = discord.Embed(title=f'Get Avatar', description=f'Requested by : {ctx.message.author.mention}')
    embed.set_author(name='Keshi v1.0rev4')
    embed.add_field(name=f"Hippity Hoppity your Profile Picture is now my property!", value=f"{member.mention}'s Profile Picture")
    embed.set_image(url=member.avatar_url)

    await ctx.send(embed=embed)



keshi.run('ODAxOTc5ODIxMjAxNTU1NDY4.YAoj6Q.kFQu8YOEL01NlhgcwGFg-u4FtEc')
