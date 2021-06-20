import discord
from discord import user 
from discord.ext import commands
from discord.ext.commands.core import Command 

client = commands.Bot(command_prefix = 'hks ')

@client.event
async def on_ready():
    print('bot has started!')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! `{round(client.latency * 1000)}ms`')

@client.command()
async def ghostping(ctx, *, arg):
    await ctx.send(arg)

@client.command()
@commands.has_role("STAFF")
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send (f'Kicked {member.mention}')

@client.command()
@commands.has_role("STAFF")
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send (f'Banned {member.mention}')

@client.command()
@commands.has_role("STAFF")
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user


        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'unbanned {user.mention}')
            return

@client.command(pass_context=True)
async def purge(ctx, amount=30):
    channel = ctx.message.channel
    messages = []
    async for message in channel.history(limit=amount + 1):
              messages.append(message)

    await channel.delete_messages(messages)
    await ctx.send(f'{amount} messages have been purged by {ctx.message.author.mention}')

@client.command()
async def say(ctx, *, arg):
    allowed_mentions = discord.AllowedMentions(users=False, roles=False, everyone=False)
    await ctx.send(arg, allowed_mentions=allowed_mentions)

client.run('ODU2MTg2MjI1MzY5OTM5OTg5.YM9Xjw.N0p35i9J9W4TcDoMU9FLMF5Nd2A')

