import pygame as pg
import game
import character

pos = pg.Vector2(0, 0)

def get_input():
    keys = pg.key.get_pressed()
    if keys[pg.K_UP]:
        game.char.direction = character.Direction.UP
        game.char.moving = True
        pos.y -= 3
    elif keys[pg.K_DOWN]:
        game.char.direction = character.Direction.DOWN
        game.char.moving = True
        pos.y += 3
    elif keys[pg.K_LEFT]:
        game.char.direction = character.Direction.LEFT
        game.char.moving = True
        pos.x -= 3
    elif keys[pg.K_RIGHT]:
        game.char.direction = character.Direction.RIGHT
        game.char.moving = True
        pos.x += 3
    else:
        game.char.moving = False

        