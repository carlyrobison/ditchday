import random
import time
import actions_reactions

PLAYER_HP = 15
WOLVERINE_HP = 50

ROLES_TO_ABILITIES = {845024826702692383: actions_reactions.ELECTROKINESIS,
					  845024941086867496: actions_reactions.THERMAL_MANIPULATION}

class Wolverine:
	def __init__(self):
		self.hp = WOLVERINE_HP
		self.actions = {"claws": "Wolverine goes for {0} with his claws!",
						"slap": "Wolverine winds up to slap {0} across the face",
						"fastball": "Somehow, Wolverine has thrown __himself__ in a fastball special at {0}!"}

	def attack(self, other_players):
		# choose other player to attack
		target = random.choice(other_players)
		attackName = random.choice(list(self.actions.keys()))
		# say the attack
		return attackName, target, self.actions[attackName].format(target.name)

	# returns True if Wolverine dies
	def take_damage(self, hpchange):
		self.hp += hpchange
		if self.hp <= 0:
			return True
		return False

class Player:
	def __init__(self, user):
		self.hp = PLAYER_HP
		self.abilities = actions_reactions.EVERYONE
		self.special_abilities = ROLES_TO_ABILITIES
		self.user = user

	# returns the string to send, and the hpchange to deal to Wolverine
	# TODO: should also check that player hp >= 0 (player is alive)
	def attempt_attack(self, attack, responding_to):
		for a in self.abilities:
			if a in attack:
				# also deal the associated damage
				result = self.abilities[a][responding_to]
				self.take_damage(result[2])
				return result[0].format(self.user.name), result[1]
		for r in self.user.roles:
			if r.id in ROLES_TO_ABILITIES:
				ability = ROLES_TO_ABILITIES[r.id]
				if ability["command"] in attack:
					result = ability[responding_to]
					self.take_damage(result[2])
					return result[0].format(self. user.name), result[1]

		return "invalid attack", 0

	# returns True if player dies
	def take_damage(self, hpchange):
		self.hp += hpchange
		if self.hp <= 0:
			# do something to say you've died
			return "Player dies :("

class Fight:
	def __init__(self):
		self.wolverine = Wolverine()
		self.players = {}
		self.last_attack_time = 0
		self.last_attack_type = None
		self.last_attacked_player = None

	def add_player(self, user):
		if user not in self.players:
			self.players[user] = Player(user)

	# Returns the message to send to the chat
	def wolverine_attack(self):
		self.last_attack_type, self.last_attacked_player, attackMessage = self.wolverine.attack(list(self.players.keys()))
		self.last_attack_time = time.time()
		return attackMessage

	def handle_counterattack(self, user, counterattack):
		if user != self.last_attacked_player:
			# counts as a missed attack, which doesn't do damage to wolverine
			missed_result, _ = self.players[self.last_attacked_player].attempt_attack("(missed cue)", self.last_attack_type)
			return "Sorry, you can only counter when attacked.\n" + missed_message
		
		# else it was the correct player responding
		result, damage_dealt = self.players[user].attempt_attack(counterattack, self.last_attack_type)
		if self.wolverine.take_damage(damage_dealt):
			return result + "Wolverine is dead!!!! blah blah"
		if result == "invalid attack":
			result, _ = self.players[user].attempt_attack("(missed cue)", self.last_attack_type)
			return "Invalid attack. " + result
		return result











