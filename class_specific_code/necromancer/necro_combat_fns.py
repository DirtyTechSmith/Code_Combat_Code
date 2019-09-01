from ..combat_fns import *
def killThem(banned_enemy_types=['door']):
    enemy = findNearestEnemy(banned_enemy_types=banned_enemy_types)
    if not enemy:
        return

    while enemy:
        distance = hero.distanceTo(enemy)
        if hero.canCast("fear", enemy) and distance < 10:
            hero.cast("fear", enemy)

        # drainLife()
        lightingBolt()
        raiseTheDead()

        if enemy:
            hero.attack(enemy)

        enemy = findNearestEnemy(banned_enemy_types=banned_enemy_types)