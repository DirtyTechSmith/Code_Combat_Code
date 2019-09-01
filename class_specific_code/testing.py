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


while True:
    killThem()

