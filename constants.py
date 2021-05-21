
import actions_reactions

ADMIN_CHANNEL = 845128047353921536

PLAYER_HP = 15
WOLVERINE_HP = 50

SECONDS_TO_RESPOND = 10

ROLES_TO_ABILITIES = {845024826702692383: actions_reactions.ELECTROKINESIS,
					  845024941086867496: actions_reactions.THERMAL_MANIPULATION,
					  845249621621342219: actions_reactions.MAGNOKINESIS,
					  845249760712720416: actions_reactions.LUMINESCENCE,
					  845249813406154752: actions_reactions.ALCHEMY,
					  845249857493139487: actions_reactions.PHOTOKINESIS,
					  845249922348744754: actions_reactions.SHAPESHIFTING,
					  845249967274721290: actions_reactions.SONOKINESIS}

INSTRUCTIONS = """Wolverine is waiting for you in the Danger Room!
Everyone should `--enter` the room and then you can --startfight.
If you need to, you can --resetroom and re-enter.

Wolverine will choose one of you at a time to attack. When he does,
--counter with one of the following attacks based on your abilities.
Choose the one that has the highest chance of success depending on
Wolverine's attack!

Everyone: --counter protect
You cower in fear and protect your face.

Electrokinesis: --counter electrocute
You send a bolt of electricity towards Wolverine.

Thermal Manipulation: --counter burn
You send a wave of heat towards Wolverine.

Magnokinesis: --counter paralyze
You repel Wolverine's magnetic skeleton.

Luminescence: --counter flare
You send out a bright pulse of light.

Alchemy: --counter transmute
You turn your skin to steel.

Photokinesis: --counter darken
You remove all the light from the room.

Shapeshifting: --counter mimic
You morph into one of Wolverine's teammates.

Sonokinesis: --counter scream
You let out a high pitched scream.

If any of your hit points are reduced to 0, you'll be out of the fight.
If you can deal enough damage to Wolverine before he gets all of you,
then you win!
"""


INSTRUCTIONS_PART_2 = """You've gone back in time and are now controlling
Wolverine! You must choose your attacks strategically so that the players
all lose. However, to keep the fabric of spacetime intact, you'll have to
target players in the same order as you did before. Your first attack will
start the fight. If you get through the fight without dying this time,
you win!

As Wolverine, you have the following attacks:
--attack claws
You go for your tatget with your Claws!

--attack slap
You wind up to slap your target across the face.

--attack fastball
Somehow, you throw _yourself_ in a fastball special at your target!
"""