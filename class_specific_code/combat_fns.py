def findNearestEnemy(banned_enemy_types =['door']):
    enemies = hero.findEnemies()
    nearest_enemy = None
    closest_dist = float('inf')
    for enemy in enemies:
        if not enemy:
            continue

        if enemy.type in banned_enemy_types:
            continue

        distance = hero.distanceTo(enemy)
        if distance < closest_dist:
            closest_dist = distance
            nearest_enemy = enemy

    return nearest_enemy