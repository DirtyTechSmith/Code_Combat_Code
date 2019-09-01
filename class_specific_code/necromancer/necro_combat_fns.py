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

