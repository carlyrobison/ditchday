from discord.ext.commands import Bot 
import discord
import asyncio
import datamodels

client = discord.Client()

bot = Bot(command_prefix='--')

dangerRooms = {}

ADMIN_CHANNEL = 845128047353921536

@bot.command(name='enter')
async def enter_room(context):
	if context.channel.id not in dangerRooms:
		dangerRooms[context.channel.id] = datamodels.FightPart1()
	dangerRooms[context.channel.id].add_player(context.message.author)
	await context.send("{0} entered the Danger Room".format(context.message.author.name))

@bot.command(name='resetroom')
async def reset_room(context):
	dangerRooms.pop(context.channel.id, None)
	dangerRooms[context.channel.id] = datamodels.FightPart1()
	await context.send("Reset the Danger Room".format(context.message.author.name))

@bot.command(name='startfight')
async def intro_message(context):
	try:
		fight_room = get_fight_room(context)
		if len(fight_room.players.keys()) == 0: # no players are entered
			await context.send("Please --enter the Danger Room")
		else:
			await context.send("blah blah intro stuff")
			await context.send(fight_room.wolverine_attack())
	except KeyError:
		await context.send("Please --enter the Danger Room")
	
@bot.command(name='counter')
async def counterattack(context, *args):
	fight_room = get_fight_room(context)
	gameLost, gameWon, msg = fight_room.handle_counterattack(context.message.author, context.message.content)

	await context.send(msg)
	if gameLost:
		await reset_room(context)
	elif gameWon:
		print(fight_room)
		print(fight_room.history_player_attack())
		dangerRooms.pop(context.channel.id, None)
	else:
		await context.send(get_fight_room(context).wolverine_attack())

@bot.command(name='fightstatus')
async def fight_status(context, *args):
	try:
		await context.send(get_fight_room(context))
	except KeyError:
		dangerRooms[context.channel.id] = datamodels.FightPart1()
		await context.send(get_fight_room(context))


def get_fight_room(context):
	return dangerRooms[context.channel.id]


bot.run('')
