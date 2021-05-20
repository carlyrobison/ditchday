from discord.ext.commands import Bot 
import discord
import asyncio
import datamodels

client = discord.Client()

bot = Bot(command_prefix='--')


state = 0
wolverine = datamodels.Wolverine(50)
players = []
player = datamodels.Player(15, {"electrocute": "Uh Oh! Wolverine hits {0} and the electrcity hits them both! Wolverine and {0} each take 2 Damage."})

@bot.command(name='enterroom')
async def enter_room(context):
	players.append(context.message.author.name)
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