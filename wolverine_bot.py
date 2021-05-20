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
		dangerRooms[context.channel.id] = datamodels.Fight()
	dangerRooms[context.channel.id].add_player(context.message.author)
	await context.send("{0} entered the Danger Room".format(context.message.author.name))

@bot.command(name='startfight')
async def intro_message(context):
	await context.send("blah blah intro stuff")
	await context.send(get_fight_room(context).wolverine_attack())


@bot.command(name='counterattack')
async def counterattack(context, *args):
	print("counterattack attempted by {0} message {1} with roles {2}".format(context.message.author.name,
		context.message.content, context.message.author.roles))

	await context.send(get_fight_room(context).handle_counterattack(context.message.author, context.message.content))
	await context.send(get_fight_room(context).wolverine_attack())


def get_fight_room(context):
	return dangerRooms[context.channel.id]


bot.run('')
