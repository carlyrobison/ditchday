import random
import time
import actions_reactions

PLAYER_HP = 15
WOLVERINE_HP = 5

ROLES_TO_ABILITIES = {845024826702692383: actions_reactions.ELECTROKINESIS,
					  845024941086867496: actions_reactions.THERMAL_MANIPULATION}

class Wolverine:
	def __init__(self):
		self.hp = WOLVERINE_HP
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
		self.hp = PLAYER_HP
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
				return result[0].format(self.user.name), result[1], result[2]
		for r in self.user.roles:
			if r.id in ROLES_TO_ABILITIES:
				ability = ROLES_TO_ABILITIES[r.id]
				if ability["command"] in attack:
					result = ability[responding_to]
					return result[0].format(self. user.name), result[1], result[2]

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

		if user != self.last_attacked_player:
			response.append("Sorry, you can only counter when attacked.")
			# counts as a missed attack, which doesn't do damage to wolverine
			missed_result, _, player_hp_change = self.players[self.last_attacked_player].attempt_attack("(missed cue)", self.last_attack_type)
			self.player_counters_history.append((self.last_attacked_player, "(missed cue)"))
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
				self.player_counters_history.append((user, "(missed cue)"))
			else:
				self.player_counters_history.append((user, counterattack))
			response.append(result)

			self.wolverine.take_damage(damage_dealt)
			if not self.wolverine.is_alive():
				response.append("Wolverine is dead!!!! blah blah code to next thing")
				gameWon = True

			dmg = self.deal_damage_and_check_player_aliveness(self.players[user], player_hp_change)
			if dmg:  # only returns on player death
				self.players.pop(user)
				response.append(dmg)

		if len(self.players.keys()) == 0:
			response.append("No players remaining. Wolverine has won the fight. Re-enter (--enter) the Danger Room and --startfight to retry.")
			gameLost = True

		return gameLost, gameWon, "\n".join(response)

	def history_player_attacks(self):
		print(self.player_counters_history)
		return ",".join(self.player_counters_history)











