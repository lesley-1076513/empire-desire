import pygame as pg
import game
import character

pos = pg.Vector2(0, 0)

def get_input():
    keys = pg.key.get_pressed()
    if keys[pg.K_UP]:
        game.char.direction = character.Direction.UP
        game.char.state = character.State.MOVING
        pos.y -= 3
    elif keys[pg.K_DOWN]:
        game.char.direction = character.Direction.DOWN
        game.char.state = character.State.MOVING
        pos.y += 3
    elif keys[pg.K_LEFT]:
        game.char.direction = character.Direction.LEFT
        game.char.state = character.State.MOVING
        pos.x -= 3
    elif keys[pg.K_RIGHT]:
        game.char.direction = character.Direction.RIGHT
        game.char.state = character.State.MOVING
        pos.x += 3
    elif keys[pg.K_a]:
        game.char.state = character.State.ATTACKING
    else:
        game.char.state = character.State.IDLE

        