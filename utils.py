import math

def iterateQueue(game):
    """
    iterate on the queue of bullet. This is to achieve the anime effect of bullet
    :param game: runtime environment
    :return: none
    """
    for bullet in game.bulletQueue:
        bullet.move(angleToDirection(game, bullet.angle))
        bullet.update()
        if bullet.collapse():
            if bullet in game.bulletQueue:
                game.bulletQueue.remove(bullet)

def angleToDirection(game, angle):
    """A function that turn angle to a direction vector

    :param game: runtime environment
    :param angle: angle between the vector with the x axis. x axis point to right and y axis point to top
    :return: a direction vector
    """
    return [game.tank1.speed * math.cos(math.radians(angle)), -game.tank1.speed * math.sin(math.radians(angle))]

def Add(game, event):
    """
    add a event to game.uevent
    :param game: runtime environment
    :param event: a event to be added in the game.uevent queue
    :return: none
    """
    for e in game.uevent:
        if(e == event):
            return
    game.uevent.append(event)

def checkCollapse(game):
    """
    check if two tanks are collapsed
    :param game: runtime environment
    :return: none
    """
    if(abs(game.tank1.pos[0] - game.tank2.pos[0]) < game.tank1.width / 2 and abs(game.tank2.pos[1] - game.tank1.pos[1]) < game.tank1.height / 2):
        game.restart()

def getAttackAngle(game):
    """
    used in AI mode. get the correct attack angle
    :param game: runtime environment
    :return: attack angle - in degree
    """
    x = game.tank1.pos[0] - game.tank2.pos[0]
    y = -(game.tank1.pos[1] - game.tank2.pos[1])
    return math.degrees(math.atan2(y, x))
