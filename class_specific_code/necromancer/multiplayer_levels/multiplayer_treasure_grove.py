from ..spells import *
from search_code.most_valuable_item import getMostValuable
from ..necro_combat_fns import *

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        if enemy.health < (hero.maxhealth * .1):
            pet.chase(enemy)

    killThem()
    getMostValuable()
