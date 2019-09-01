from ..combat_fns import *


def killThem(move_to_corpses=True, banned_enemy_types=['door']):
    enemy = findNearestEnemy(banned_enemy_types=banned_enemy_types)
    if not enemy:
        return

    while enemy:
        distance = hero.distanceTo(enemy)
        if hero.canCast("fear", enemy) and distance < 10:
            hero.cast("fear", enemy)

        devour()
        drainLife()
        lightingBolt()
        raiseTheDead(move_to_corpses=move_to_corpses)

        if enemy:
            hero.attack(enemy)

        enemy = findNearestEnemy(banned_enemy_types=banned_enemy_types)
