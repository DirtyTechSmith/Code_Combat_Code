from hero_base import hero


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

    if not hero.canCast('raise-dead', closest_corpse):
        return

    if not move_to_corpses:
        if closest_dist > 20:
            return
    else:
        hero.move(closest_corpse.pos)

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


def sacrifice(target_1=None, target_2=hero, health_threshold=.5):
    health_percent = hero.health / hero.maxHealth
    if health_percent > health_threshold:
        return

    spell_string = 'sacrifice'
    spell_range = 20
    if target_1 is None:
        friends = hero.findFriends()
        for friend in friends:
            if not friend:
                continue
            if hero.distanceTo(friend) > spell_range:
                continue

            target_1 = friend

    if not target_1:
        return

    if hero.distanceTo(target_1) > spell_range:
        return

    if not target_2:
        return

    if hero.canCast(spell_string, target_1):
        return

    hero.cast(spell_string, target_1, target_2)


def soulLink(target_1=None, target_2=hero):
    spell_string = 'soul-link'
    spell_range = 25
    if target_1 is None:
        friends = hero.findFriends()
        for friend in friends:
            if not friend:
                continue
            if hero.distanceTo(friend) > spell_range:
                continue

            target_1 = friend

    if not target_1:
        return

    if hero.distanceTo(target_1) > spell_range:
        return

    if not target_2:
        return

    if hero.canCast(spell_string, target_1):
        return

    hero.cast(spell_string, target_1, target_2)


def summonUndead(soul_link=True, sacrifice_on_low_health=True):
    spell_string = 'summon-undead'
    if not hero.canCast(spell_string):
        return

    hero.cast(spell_string)

    if not soul

    skeletons = hero.findByType('skeleton', hero.findFriends())
    if not skeletons:
        return

    for skeleton in skeletons:
        if not skeleton:
            continue

        if sacrifice_on_low_health:
            if hero.health < (hero.maxHealth * 0.5):
                sacrifice(target_1=skeleton)

        if soul_link:
            soulLink(target_1=skeleton)
