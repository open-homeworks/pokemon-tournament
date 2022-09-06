import random
from dataclasses import dataclass
from typing import Dict, List, Tuple

from lib.pokemon import Pokemon

@dataclass
class BattleRound:
    attacker: str
    defendant: str
    damage: float
    ability: str

@dataclass
class BattleSummary:
    winner: Pokemon
    defeated: Pokemon
    rounds: List[BattleRound]


def simulate_battle(p1: Pokemon, p2: Pokemon, random_seed: int = 0) -> BattleSummary:
    """This function simulates a single battle between two Pokémons.

    A battle consists of several rounds, at each round there is only one Pokémon
    doing the attack, while the other is defending. The role at each turn
    is defined randomly and each participant has a random chance of being
    selected as the attacker, weigthed by the amount abilities of the
    participant over the total number of abilities of both participants. For
    example, if `p1` has 2 abilities, while `p2` has only one, then `p1` is
    expected to be selected as the attacker 66.66% of the time.

    Since a battle is a random process, we will repeat each battle a thousand
    times and pick the winner as the most common winner in all battles, as well
    as picking the least number of rounds in which the winner won.

    Each battle comes to an end whenever the health points of any of the
    Pokémons reaches 0 or there are 100 rounds. At each turn of the battle,
    the health points of the attacker remain the same, while the ones for the
    defendant are computed as:

        damage = attacker.attack * random.betavariate(1, 5)
        HP_t+1 = HP_t - damage (Health points of the defendant at time t)


    This function is provided a random_seed value, so that the battle always
    yields the same results.
    """
    raise NotImplementedError
