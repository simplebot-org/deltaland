"""Constants"""

from enum import IntEnum

DATABASE_VERSION = 3
WORLD_ID = 0
MAX_HP = 300
MAX_STAMINA = 5
STARTING_LEVEL = 1
STARTING_ATTACK = 1
STARTING_DEFENSE = 1
STARTING_GOLD = 0
DICE_FEE = 10
MIN_CAULDRON_GIFT = 20
MAX_CAULDRON_GIFT = 100

LIFEREGEN_COOLDOWN = 30
STAMINA_COOLDOWN = 60 * 60
DICE_COOLDOWN = 60 * 5


class StateEnum(IntEnum):
    # Player state
    REST = 0
    PLAYING_DICE = -1
    HEALING = -2

    # World state
    DAY = -100
    MONTH = -101
    YEAR = -102
    BATTLE = -103


class CombatTactic(IntEnum):
    NONE = 0
    HIT = 1
    FEINT = 2
    PARRY = 3
