from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = 'NzU1MjcyNTM4ODk1OTQxNjcy.X2A4XQ.6uEv0LSKlZtnmPstmvv1dM96G3I'


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run(token)
