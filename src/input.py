import pygame as pg

pos = pg.Vector2(0, 0)

def get_input():
    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
        pos.y -= 3
    if keys[pg.K_s]:
        pos.y += 3
    if keys[pg.K_a]:
        pos.x -= 3
    if keys[pg.K_d]:
        pos.x += 3
        