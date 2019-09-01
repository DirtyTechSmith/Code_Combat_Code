# Attack both ogres and grab the gem.
def lightingBolt(enemy=None, farthest=True):
    splash_damage = 2
    range = 50
    if not hero.isReady("lightning-bolt"):
        return False

    if enemy is None:
        enemies = hero.findEnemies()  # type: list
        if not enemies:
            return

        # enemies = sorted(enemies,key=lambda x: (hero.distanceTo(x)), reverse=farthest)
        for target in enemies:
            distance = hero.distanceTo(target)
            if distance > range:
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
            closest_dist = dist

    if closest_dist > 20:
        return

    hero.cast("raise-dead")


def killThem():
    enemies = hero.findEnemies()
    while enemies:
        lightingBolt()
        raiseTheDead()
        enemy = hero.findNearestEnemy()
        if enemy:
            hero.attack(enemy)

        enemies = hero.findEnemies()


moves = [hero.moveRight, hero.moveRight, hero.moveUp, hero.moveLeft, hero.moveLeft]
for move in moves:
    hero.say('poop')
    killThem()
    move()