import discord
from discord.ext import commands
import TenGiphPy

tokens = {'bot': 'bottoken',
          'tenor': 'tenortokenhere',
          }
#u can add a prefix as u wish
bot = commands.Bot(command_prefix='')
bot.remove_command('help')
t = TenGiphPy.Tenor(token=tokens['tenor'])


#all this functions will return u a gif depending on the keywork set in t.random
@bot.command(pass_context=True)
async def random(ctx, message):
    """This command will return a tenor gif if you type "random cat" as example."""
    getgifurl = t.random(message)
    print(message)
    await ctx.send(f'{getgifurl}')

@bot.command(pass_context=True)
async def happy(ctx):
    getgifurl = t.random("happy")
    await ctx.send(f'{getgifurl}')

@bot.command(pass_context=True)
async def model(ctx):
    getgifurl = t.random("bikini hot girl")
    print(getgifurl)
    await ctx.send(f'{getgifurl}')

@bot.command(pass_context=True)
async def sparta(ctx):
    getgifurl = t.random("This is sparta")
    await ctx.send(f'{getgifurl}')

@bot.command(pass_context=True)
async def silver(ctx):
    getgifurl = t.random("sylvester stallone")
    await ctx.send(f'{getgifurl}')

@bot.command(pass_context=True)
async def Arnold(ctx):
    """This command will return a tenor gif if you type "!tenor cat" as example."""
    getgifurl = t.random("arnold schweinzeneger")
    await ctx.send(f'{getgifurl}')

@bot.command(pass_context=True)
async def yoda(ctx):
    getgifurl = t.random("Yoda")
    await ctx.send(f'{getgifurl}')

@bot.command(pass_context=True)
async def boobs(ctx):
    getgifurl = t.random("bouncing boobs")
    await ctx.send(f'{getgifurl}')

@bot.command(pass_context=True)
async def memes(ctx):
    getgifurl = t.random("memes")
    await ctx.send(f'{getgifurl}')

@bot.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(title="It's me koksal, how to use me well <3", description="Commands help, this bot provides u latest gif from tenor, all need is enter a command below", color=0x00ff00)
    embed.add_field(name="help", value= "Show u available commands", inline=False)
    embed.add_field(name="koksal", value="Show random gif of koksal", inline=True)
    embed.add_field(name="Arnold", value= "Show u random gif of arnold schweinzeneger", inline=False)
    embed.add_field(name="silver", value= "Show u random gif of sylvester stallone", inline=False)
    embed.add_field(name="happy", value= "Show u random gif of happy reaction", inline=False)
    embed.add_field(name="model", value= "Show u random gif of Model woman", inline=False)
    embed.add_field(name="sparta", value= "Show u random gif of This is Sparta", inline=False)
    embed.add_field(name="yoda", value= "Show u random gif of yoda", inline=False)
    embed.add_field(name="memes", value= "Show u random gif of memes", inline=False)
    embed.add_field(name="boobs", value= "Show u random gif of bouncing boobs", inline=False)
    await ctx.send(embed=embed)

@random.error
async def tenor_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Giftag cant be None. Please give a valid giftag to search.')
    else:
      raise error      
bot.run(tokens['bot'])
