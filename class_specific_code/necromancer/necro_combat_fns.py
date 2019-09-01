def killThem():
    enemies = hero.findEnemies()
    for enemy in enemies:
        if not enemy:
            raiseTheDead()
            continue

        lightingBolt()
        raiseTheDead()
        enemy = hero.findNearestEnemy()
        if enemy:
            hero.attack(enemy)


def findNearestEnemy():
    enemies = hero.findEnemies()
    nearest_enemy = None
    closest_dist = float('inf')
    for enemy in enemies:
        if not enemy:
            continue

        if enemy.type == 'door':
            continue

        distance = hero.distanceTo(enemy)
        if distance < closet_dist:
            cloest_dist = distance
            nearest_enemy = enemy
    return nearest_enemy