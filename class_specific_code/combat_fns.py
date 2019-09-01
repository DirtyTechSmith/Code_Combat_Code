def findNearestEnemy(banned_enemy_types=['door']):
    enemies = findEnemies(banned_enemy_types=banned_enemy_types)
    nearest_enemy = None
    closest_dist = float('inf')
    for enemy in enemies:
        distance = hero.distanceTo(enemy)
        if distance < closest_dist:
            closest_dist = distance
            nearest_enemy = enemy

    return nearest_enemy

def findEnemies(banned_enemy_types=['door']):
    enemies = hero.findEnemies()
    bad_guys = []
    for enemy in enemies:
        if not enemy:
            continue
        if enemy.type in banned_enemy_types:
            continue
        bad_guys.append(enemy)

    return bad_guys


