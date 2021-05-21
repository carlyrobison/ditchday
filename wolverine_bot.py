from discord.ext.commands import Bot 
import discord
import asyncio
import datamodels
import constants

client = discord.Client()

bot = Bot(command_prefix='--')

dangerRooms = {}

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
		await bot.get_channel(constants.ADMIN_CHANNEL).send(fight_room.history_player_attack())
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

@bot.command(name='dangerroominstructions')
async def list_instructions(context, *args):
	await context.send(constants.INSTRUCTIONS)

def get_fight_room(context):
	return dangerRooms[context.channel.id]


dangerRoomsPart2 = {}

@bot.command(name='replayinstructions')
async def list_replay_instructions(context, *args):
	await context.send(constants.INSTRUCTIONS_PART_2)

@bot.command(name='loadpart2history')
async def load_history(context, *, arg):
	dangerRoomsPart2[context.channel.id] = datamodels.FightPart2(arg)
	await context.send("Loaded fight history: {0}. Please delete this message for maximum challenge.".format(dangerRoomsPart2[context.channel.id]))

@bot.command(name='resetreplay')
async def reset_replay(context, *arg):
	try:
		dr = dangerRoomsPart2[context.channel.id]
		dangerRoomsPart2[context.channel.id] = datamodels.FightPart2(dr.history_player_attack())
		await context.send("Fight replay reset.")
	except KeyError:
		await context.send("Missing fight history. Ask an alum/senior to load it.")

@bot.command(name='attack')
async def attack(context, *args):
	try:
		dr = dangerRoomsPart2[context.channel.id]
		await context.send(dr.manage_attack(context.message.content))
	except KeyError:
		await context.send("Missing fight history. Ask an alum/senior to load it.")

bot.run('')
