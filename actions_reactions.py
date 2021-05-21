

EVERYONE = {
	"(missed cue)": {
		"description": "{0} didn't react in time!",
		# first number is HP change to wolverine, second number is damage change to player
		"claws": ["Wolverine stabs {0} in the shoulder! {0} takes 5 damage.", 0, -5],
		"slap": ["Wolverine slaps {0}! {0} takes 2 damage.", 0, -2],
		"fastball": ["Wolverine careens into {0} with his claws out! {0} takes 7 Damage!", 0, -7]
	},
	"protect": {
		"description": "{0} cowers in fear and protects their face.",
		"claws": ["{0} saves their face from lacerations! {0} takes 2 damage.", 0, -2],
		"slap": ["Wolverine hits {0}'s shoulder! No Damage Taken.", 0, 0],
		"fastball": ["The full force of an angry Canadian hits {0}! {0} takes 3 Damage", 0, -3]
	}
}

ELECTROKINESIS = {
	"command": "electrocute",
	"description": "{0} sends a bolt of electricity towards Wolverine!",
	"claws": ["The electricity hits Wolverine's claws and he convulses! Wolverine takes 4 damage!", -4, 0],
	"slap": ["Uh Oh! Wolverine hits {0} and the electrcity hits them both! Wolverine and {0} each take 2 Damage.", -2, -2],
	"fastball": ["It's super effective! Wolverine is hit midair and takes 5 points of damage", -5, 0]
}

THERMAL_MANIPULATION = {
	"command": "burn",
	"description": "{0} sends a wave of heat towards Wolverine!",
	"claws": ["Wolverine's super heated claws plunge into {0}'s shoulder! {0} takes 4 damage", 0, -4],
	"slap": ["Wolverine's hand boils in midair! He takes 3 Damage.", -3, 0],
	"fastball": ["Wolverine is moving too fast for the heat pocket to hurt him! {0} takes 2 damage!", 0, -2]
}

MAGNOKINESIS = {
	"command": "paralyze",
	"description": "{0} repels Wolverine's magnetic skeleton!",
	"claws": ["Wolverine is frozen in front of {0}! No Damage Taken", 0, 0],
	"slap": ["{0} makes Wolverine hit himself in the face, but he grazes {0} on the way. They both take 1 damage!", -1, -1],
	"fastball": ["{0} slams Wolverine into the floor. Wolverine takes 3 damage!", -3, 0]
}

LUMINESCENCE = {
	"command": "flare",
	"description": "{0} sends out a bright pulse of light!",
	"claws": ["Wolverine is blinded and misses {0}'s shoulder and hits their chest instead! {0} Takes 10 damage. Wolverine takes 2 Damage", -2, -10],
	"slap": ["You don't need to see to slap! Wolverine and {0} both take 2 Damage.", -2, -2],
	"fastball": ["Wolverine misses {0} and crashes into the wall! Wolverine takes 3 Damage. ", -3, 0]
}

ALCHEMY = {
	"command": "transmute",
	"description": "{0} turns their skin to steel!",
	"claws": ["Adamantium beats steel! Wolverine's claws cut through {0} like butter, but at least now it's frozen butter. {0} takes 1 Damage", 0, -1],
	"slap": ["Wolverine bruises his hand on {0}'s face! Wolverine takes 2 damage", -2, 0],
	"fastball": ["Wolverine's momentum is stopped suddenly by {0}'s high mass! Wolverine takes 1 Damage!", -1, 0]
}

PHOTOKINESIS = {
	"command": "darken",
	"description": "{0} removes all light from the room!",
	"claws": ["Wolverine misses {0}! No Damage taken", 0, 0],
	"slap": ["You don't need to see to slap! {0} takes 2 Damage.", 0, -2],
	"fastball": ["Wolverine misses {0} and crashes into the wall! Wolverine takes 3 Damage. ", -3, 0]
}

SHAPESHIFTING = {
	"command": "mimic",
	"description": "{0} morphs into one of Wolverine's Team Mates!",
	"claws": ["{0} turns into Jean Grey. You see Wolverine shed a tear as he stabs {0} in the heart. {0} Takes 3 Damage, Wolverine takes 1 emotional damage.", -1, -3],
	"slap": ["{0} turns into Cyclops. Wolverine Slaps them extra hard. {0} takes 3 damage.", 0, -3],
	"fastball": ["{0} turns into Wolverine. Their sudden height decrease causes Wolverine to miss. No Damage taken.", 0, 0]
}

SONOKINESIS = {
	"command": "scream",
	"description": "{0} lets out a high pitched scream!",
	"claws": ["Wolverine grimaces but perserveres! {0} and Wolverine both take 2 damage", -2, -2],
	"slap": ["Wolverine winces and claps his hands to his ears instead! Wolverine takes 1 Damage", -1, 0],
	"fastball": ["The force of the scream shoves Wolverine back! No Damage taken. ", 0, 0]
}
