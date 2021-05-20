from discord.ext.commands import Bot 
import discord
import asyncio
import datamodels

client = discord.Client()

bot = Bot(command_prefix='--')

dangerRooms = {}


@bot.command(name='enterroom')
async def enter_room(context):
	if context.channel.id not in dangerRooms:
		dangerRooms[context.channel.id] = Fight()
	dangerRooms[context.channel.id].add_player()
	await context.send("{0} entered the Danger Room".format(context.message.author.name))

@bot.command(name='startfight')
async def intro_message(context):
	await context.send("blah blah intro stuff")
	await context.send(wolverine.attack(players))


@bot.command(name='counterattack')
async def counterattack(context, *args):
	print("counterattack attempted by {0} message {1} with roles {2}".format(context.message.author.name,
		context.message.content, context.message.author.roles))

	await context.send(player.attempt_attack(context.message.author, context.message.content))


bot.run('')