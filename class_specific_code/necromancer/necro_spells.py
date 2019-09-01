def lightingBolt(banned_enemy_types=['door', 'chest'], enemy=None, farthest=True):
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
    if not hero.canCast('lightning-bolt', enemy):
        return

    hero.cast("lightning-bolt", enemy)
    return True


def raiseTheDead(move_to_corpses=True):
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

    if not move_to_corpses:
        if closest_dist > 20:
            return
    else:
        hero.move(closest_corpse.pos)

    if not hero.canCast('raise-dead', enemy):
        return

    hero.cast("raise-dead")


def drainLife(banned_enemy_types=['door', 'chest']):
    cast_range = 15
    if hero.health == hero.maxhealth:
        return

    enemy = findNearestEnemy(banned_enemy_types=banned_enemy_types)
    if not enemy:
        return

    if hero.distanceTo(enemy) > cast_range:
        return

    if not hero.canCast('drain-life', enemy):
        return

    hero.cast("drain-life", enemy)


def devour(banned_enemy_types=['door', 'chest']):
    damage = 200

    if hero.health == hero.maxhealth:
        return

    enemy = findNearestEnemy(banned_enemy_types=banned_enemy_types)
    if not enemy:
        return

    if enemy.health > damage * .5:
        return

    if not hero.canCast('devour', enemy):
        return

    hero.cast("devour", enemy)
