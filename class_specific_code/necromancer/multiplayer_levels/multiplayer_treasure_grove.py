# The ogre looks big and slow. Movement will help you avoid his deadly attacks.
# Attack both ogres and grab the gem.
def lightingBolt(enemy=None, farthest=True):
    splash_damage = 2
    lighting_bold_range = 50
    if not hero.isReady("lightning-bolt"):
        return False

    if enemy is None:
        enemies = hero.findEnemies()  # type: list
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
        if distance < closest_dist:
            closest_dist = distance
            nearest_enemy = enemy

    return nearest_enemy


def drainLife():
    if hero.health == hero.maxhealth:
        return

    enemy = findNearestEnemy()
    if not enemy:
        return

    hero.cast("drain-life", enemy)


def killThem():
    enemy = findNearestEnemy()
    if not enemy:
        return

    while enemy:
        drainLife()
        lightingBolt()
        raiseTheDead()

        if enemy:
            hero.attack(enemy)

        enemy = hero.findNearestEnemy()


def getMostValuable(close_distance=10):
    items = hero.findItems()
    item_values = [item.value for item in items]
    best_item = max(item_values)
    # hero.say(best_item)
    nearest_item = hero.findNearestItem()
    if nearest_item.value == best_item:
        distance = hero.distanceTo(nearest_item)
        if distance <= close_distance:
            hero.moveXY(nearest_item.pos.x, nearest_item.pos.y)
        else:
            hero.move(nearest_item.pos)

        return

    nearest_distance = hero.distanceTo(nearest_item)
    value_distance = nearest_item.value / nearest_distance

    items_by_value = sorted(items, key=lambda x: x.value, reverse=False)
    items_by_value.remove(nearest_item)
    for item in items_by_value:
        if not item:
            continue

        current_value_distance = item.value / (hero.distanceTo(item))
        if current_value_distance > value_distance:
            nearest_item = item
            value_distance = current_value_distance

    if not nearest_item:
        return

    # hero.say(value_distance)
    hero.move(nearest_item.pos)


while True:
    killThem()
    getMostValuable()
