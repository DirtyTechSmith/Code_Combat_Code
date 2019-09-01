# Use "fire-trap"s to defeat the ogres.
buildit = "fire-trap"
center = Vector(40, 34)
while True:
    enemy = hero.findNearestEnemy()
    # if hero.canCast("summon-undead"):
    #     hero.cast("summon-undead")

    hero.move(center)

    if enemy:
        if enemy.pos.x < hero.pos.x:
            hero.buildXY(buildit, 40, 49)
            hero.moveXY(center.x, center.y)
        elif enemy.pos.x > hero.pos.x:
            hero.buildXY(buildit, 55, 33)
            hero.moveXY(center.x, center.y)
        elif enemy.pos.y < hero.pos.y:
            hero.buildXY(buildit, 40, 19)
            hero.moveXY(center.x, center.y)
        elif enemy.pos.y > hero.pos.y:
            hero.buildXY(buildit, 25, 34)
            hero.moveXY(center.x, center.y)


