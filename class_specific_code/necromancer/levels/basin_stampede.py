# Keep moving right, but adjust up and down as you go.
def runAway(enemy, min=10):
    distance = hero.distanceTo(enemy)
    if distance >= min:
        return
    while distance <= min:
        diff = min - distance
        x_move = diff
        y_move = diff
        if enemy.pos.y > hero.pos.y:
            y_move = 0.0 - y_move

        if enemy.pos.x > hero.pos.x:
            x_move = 0.0 - x_move

        hero.moveXY(hero.pos.x + x_move, hero.pos.y + y_move)
        distance = hero.distanceTo(enemy)


while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        runAway(enemy)
        # castable = hero.canCast("lightning-bolt", enemy)
        # if castable:
        #     hero.cast("lightning-bolt", enemy)
    xPos = hero.pos.x + 5
    yPos = 17
    hero.moveXY(xPos, yPos)
