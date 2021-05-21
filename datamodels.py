import random
import time
import actions_reactions
import constants
import json
from io import StringIO

class Wolverine:
	def __init__(self):
		self.hp = constants.WOLVERINE_HP
		self.actions = {"claws": "Wolverine goes for {0} with his claws!",
						"slap": "Wolverine winds up to slap {0} across the face",
						"fastball": "Somehow, Wolverine has thrown __himself__ in a fastball special at {0}!"}

	def __repr__(self):
		return "Wolverine with HP {0}".format(self.hp)

	def attack(self, other_players):
		# choose other player to attack
		target = random.choice(other_players)
		attackName = random.choice(list(self.actions.keys()))
		# say the attack
		return attackName, target, self.actions[attackName].format(target.name)

	# returns True if Wolverine dies
	def take_damage(self, hpchange):
		self.hp += hpchange

	def is_alive(self):
		return self.hp > 0

class Player:
	def __init__(self, user):
		self.hp = constants.PLAYER_HP
		self.abilities = actions_reactions.EVERYONE
		self.user = user

	def __repr__(self):
		return "{0} with hp {1}".format(self.user.name, self.hp)

	# returns the string to send, and the hpchange to deal to Wolverine, and the damage to the player
	def attempt_attack(self, attack, responding_to):
		for a in self.abilities:
			if a in attack:
				# also deal the associated damage
				result = self.abilities[a][responding_to]
				return self.abilities[a]["description"].format(self.user.name) + " " + result[0].format(self.user.name), result[1], result[2]
		for r in self.user.roles:
			if r.id in constants.ROLES_TO_ABILITIES:
				ability = constants.ROLES_TO_ABILITIES[r.id]
				if ability["command"] in attack:
					result = ability[responding_to]
					return ability["description"].format(self.user.name) + " " + result[0].format(self. user.name), result[1], result[2]

		return "invalid attack", 0, 0

	# returns True if player dies
	def take_damage(self, hpchange):
		self.hp += hpchange

	def is_alive(self):
		return self.hp > 0

class FightPart1:
	def __init__(self):
		self.wolverine = Wolverine()
		self.players = {}
		self.last_attack_time = 0
		self.last_attack_type = None
		self.last_attacked_player = None
		self.player_counters_history = []

	def __repr__(self):
		return "Fight with Wolverine: {0}, Players: {1}, last attack: {2} against {3}".format(self.wolverine, [p for p in self.players.values()], self.last_attack_type, (self.last_attacked_player.name if self.last_attacked_player else None) )

	def deal_damage_and_check_player_aliveness(self, player, hp_change):
		player.take_damage(hp_change)
		if not player.is_alive():
			return "{0} has taken too much damage and has been neutralized!".format(player.user.name)

	def add_player(self, user):
		if user not in self.players:
			self.players[user] = Player(user)

	# Returns the message to send to the chat
	def wolverine_attack(self):
		self.last_attack_type, self.last_attacked_player, attackMessage = self.wolverine.attack(list(self.players.keys()))
		self.last_attack_time = time.time()
		return attackMessage

	def handle_counterattack(self, user, counterattack):
		response = []
		gameLost = False
		gameWon = False

		print(time.time() - self.last_attack_time)

		if (time.time() - self.last_attack_time) > constants.SECONDS_TO_RESPOND:
			# you were too slow!
			missed_result, _, player_hp_change = self.players[self.last_attacked_player].attempt_attack("(missed cue)", self.last_attack_type)
			self.player_counters_history.append((self.last_attacked_player.name, "(missed cue)"))
			response.append(missed_result)
			# deal damage to the player
			dmg = self.deal_damage_and_check_player_aliveness(self.players[self.last_attacked_player], player_hp_change)
			if dmg:  # only returns on player death
				self.players.pop(self.last_attacked_player)
				response.append(dmg)

		elif user != self.last_attacked_player:
			response.append("Sorry, you can only counter when attacked.")
			# counts as a missed attack, which doesn't do damage to wolverine
			missed_result, _, player_hp_change = self.players[self.last_attacked_player].attempt_attack("(missed cue)", self.last_attack_type)
			self.player_counters_history.append((self.last_attacked_player.name, "(missed cue)"))
			response.append(missed_result)
			# deal damage to the player
			dmg = self.deal_damage_and_check_player_aliveness(self.players[self.last_attacked_player], player_hp_change)
			if dmg:  # only returns on player death
				self.players.pop(self.last_attacked_player)
				response.append(dmg)
		
		else:  # else it was the correct player responding
			result, damage_dealt, player_hp_change = self.players[user].attempt_attack(counterattack, self.last_attack_type)
			if result == "invalid attack":
				response.append("Invalid attack.")
				result, _, player_hp_change = self.players[user].attempt_attack("(missed cue)", self.last_attack_type)
				self.player_counters_history.append((user.name, "(missed cue)"))
			else:
				self.player_counters_history.append((user.name, counterattack))
			response.append(result)

			self.wolverine.take_damage(damage_dealt)
			if not self.wolverine.is_alive():
				response.append("Wolverine is dead!!!! Continue with the code 'victory'.")
				gameWon = True

			dmg = self.deal_damage_and_check_player_aliveness(self.players[user], player_hp_change)
			if dmg:  # only returns on player death
				self.players.pop(user)
				response.append(dmg)

		if len(self.players.keys()) == 0:
			response.append("No players remaining. Wolverine has won the fight. Re-enter (--enter) the Danger Room and --startfight to retry.")
			gameLost = True

		return gameLost, gameWon, "\n".join(response)

	def history_player_attack(self):
		print(self.player_counters_history)
		return json.dumps(self.player_counters_history)


class WolverinePart2:
	def __init__(self):
		self.hp = constants.WOLVERINE_HP
		self.actions = {"claws": "Wolverine goes for {0} with his claws!",
						"slap": "Wolverine winds up to slap {0} across the face",
						"fastball": "Somehow, Wolverine has thrown __himself__ in a fastball special at {0}!"}

	def __repr__(self):
		return "BackInTimeWolverine with HP {0}".format(self.hp)

	def is_valid_attack(self, attack, target):
		for attackName in self.actions.keys():
			if attackName in attack:
				return True, attackName, self.actions[attackName].format(target)
		return False, "", ""

	# returns True if Wolverine dies
	def take_damage(self, hpchange):
		self.hp += hpchange

	def is_alive(self):
		return self.hp > 0

class PlayerPart2:
	def __init__(self, name):
		self.hp = constants.PLAYER_HP
		self.abilities = actions_reactions.EVERYONE
		self.name = name

	def __repr__(self):
		return "{0} with hp {1}".format(self.name, self.hp)

	# returns the string to send, and the hpchange to deal to Wolverine, and the damage to the player
	def attempt_counter(self, attack, responding_to):
		for a in self.abilities:
			if a in attack:
				# also deal the associated damage
				result = self.abilities[a][responding_to]
				return self.abilities[a]["description"].format(self.name) + " " + result[0].format(self.name), result[1], result[2]
		for ability in constants.ROLES_TO_ABILITIES.values():
			if ability["command"] in attack:
				result = ability[responding_to]
				return ability["description"].format(self.name) + " " + result[0].format(self.name), result[1], result[2]

		return "invalid attack", 0, 0

	# returns True if player dies
	def take_damage(self, hpchange):
		self.hp += hpchange

	def is_alive(self):
		return self.hp > 0

class FightPart2:
	def __init__(self, players_history):
		self.wolverine = WolverinePart2()
		self.roundNum = 0
		self.player_counters_history = json.loads(players_history) # process the history
		self.players = {}
		self.load_targets()

	def __repr__(self):
		return "Fight with Wolverine: {0}, players {3}, on attack {1}, attack history {2}".format(self.wolverine, self.roundNum, self.player_counters_history, self.players)

	def load_targets(self):
		for t in list(set([p[0] for p in self.player_counters_history])):
			self.players[t] = PlayerPart2(t)

	# Returns False if the target is dead
	def get_target(self):
		target = self.player_counters_history[self.roundNum][0]
		if target not in self.players:
			return False, target
		return True, target

	# Returns the message to send to the chat
	def manage_attack(self, attack):
		response = []

		targetPlayerAlive, target = self.get_target()

		if targetPlayerAlive:
			targetPlayer = self.players[target]
			isValid, attackName, attackDesc = self.wolverine.is_valid_attack(attack, target)
			if isValid:
				response.append(attackDesc)
				result, wolverine_hp_change, player_hp_change = targetPlayer.attempt_counter(self.player_counters_history[self.roundNum][1], attackName)
				response.append(result)

				# deal player damage
				targetPlayer.take_damage(player_hp_change)
				if not targetPlayer.is_alive():
					self.players.pop(target)
					response.append("{0} has taken too much damage and has been neutralized!".format(target))

				# deal wolverine damage
				self.wolverine.take_damage(wolverine_hp_change)
				if not self.wolverine.is_alive():
					response.append("Players have taken down Wolverine! --resetreplay")
				self.roundNum += 1
			else:
				response.append("Attack was invalid. Try again!")
		else:
			if len(self.players) == 0:
				response.append("Wolverine has survived the fight! Continue with HUBRIS")
			else:
				self.roundNum += 1
				response.append("Target is already incapactitated. No damage dealt or taken.")

		
		if self.roundNum >= len(self.player_counters_history):
			response.append("Wolverine has survived the fight! Continue with HUBRIS")

		return "\n".join(response)
	
	def history_player_attack(self):
		print(self.player_counters_history)
		return json.dumps(self.player_counters_history)






