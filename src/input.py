import pygame as pg

pos = pg.Vector2(0, 0)

def get_input():
    keys = pg.key.get_pressed()
    if keys[pg.K_UP]:
        pos.y -= 3
    if keys[pg.K_DOWN]:
        pos.y += 3
    if keys[pg.K_LEFT]:
        pos.x -= 3
    if keys[pg.K_RIGHT]:
        pos.x += 3
        