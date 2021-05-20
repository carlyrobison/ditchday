import random
import actions_reactions

PLAYER_HP = 15
WOLVERINE_HP = 50

ROLES_TO_ABILITIES = {"845024826702692383": actions_reactions.ELECTROKINESIS}

class Wolverine:
	def __init__(self):
		self.hp = WOLVERINE_HP
		self.actions = {"claws": "Wolverine goes for {0} with his claws!",
						"slap": "Wolverine winds up to slap {0} across the face",
						"fastball": "Somehow, Wolverine has thrown __himself__ in a fastball special at {0}!"}

	def attack(self, other_players):
		# choose other player to attack
		target = random.choice(other_players)
		attack = random.choice(list(self.actions.values()))
		# say the attack
		return attack.format(target)


	def take_damage(self, dmg):
		self.hp -= dmg
		if self.hp <= 0:
			# do something to say you've died
			return ""

class Player:
	def __init__(self):
		self.hp = hp
		self.abilities = actions_reactions.EVERYONE
		self.special_abilities = ROLES_TO_ABILITIES

	def attempt_attack(self, user, attack):
		print("checking attack {0} for validity in {1}".format(attack, self.abilities))
		for a in self.abilities:
			if a in attack:
				# also deal the associated damage
				return self.abilities[a].format(user.name)
		for r in user.roles:
			if r.id in ROLES_TO_ABILITIES:
				if 

		return "invalid attack"

class Fight:
	def __init__(self):
		self.wolverine = Wolverine()
		self.players = {}
		self.last_attack_time = 0
		self.last_attack_type = None

	def add_player(user):
		self.players[user.id] = Player()