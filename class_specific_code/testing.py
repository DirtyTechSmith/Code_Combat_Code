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


def lightingBolt(banned_enemy_types=['door'],enemy=None, False=True):
    splash_damage = 2
    lighting_bold_range = 50
    if not hero.isReady("lightning-bolt"):
        return False

    if enemy is None:
        enemies = hero.findEnemies()  # type: list
        if not enemies:
            return
        enemies = [enemy for enemy in enemies if enemy.type not in banned_enemy_types]
        if not enemies:
            return
        # enemies = sorted(enemies,key=lambda x: (hero.distanceTo(x)), reverse=farthest)
        for target in enemies:
            distance = hero.distanceTo(target)
            if distance > lighting_bold_range:
                continue

            if not hero.canCast("lightning-bolt", target):
                continue

            enemy = target
            break

    if enemy is None:
        return False

    hero.cast("lightning-bolt", enemy)
    return True


def raiseTheDead():
    if not hero.isReady("raise-dead"):
        return

    corpses = hero.findCorpses()
    if not corpses:
        return

    closest_corpse = corpses[0]
    if not closest_corpse:
        return

    closest_dist = hero.distanceTo(closest_corpse)
    for corpse in corpses:
        distance = hero.distanceTo(corpse)
        if distance < closest_dist:
            closest_corpse = corpse
            closest_dist = distance

    if closest_dist > 20:
        return

    hero.cast("raise-dead")


def drainLife(banned_enemy_types=['door']):
    if hero.health == hero.maxhealth:
        return

    enemy = findNearestEnemy(banned_enemy_types=banned_enemy_types)
    if not enemy:
        return

    hero.cast("drain-life", enemy)
