def getMostValuable(close_distance=10):
    items = hero.findItems()
    item_values = [item.value for item in items]
    best_item = max(item_values)
    # hero.say(best_item)
    nearest_item = hero.findNearestItem()
    if not nearest_item:
        return

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