import random

class Player:
	def __init__(self, hp, abilities):
		self.hp = hp
		self.abilities = abilities

	def attempt_attack(self, user, attack):
		print("checking attack {0} for validity in {1}".format(attack, self.abilities))
		for a in self.abilities:
			if a in attack:
				# also deal the associated damage
				return self.abilities[a].format(user.name)
		return "invalid attack"



class Wolverine:
	def __init__(self, hp):
		self.hp = hp
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