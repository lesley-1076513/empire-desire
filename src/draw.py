import pygame as pg
import input

top_right = 303

def draw(w, clock, font):
    fill(w)

    draw_char(w)
    draw_fps(w, clock, font)

    blit(w)

def fill(w):
    w.render.fill("gray30")
    w.screen.fill("wheat4")

def blit(w):
    w.screen.blit(pg.transform.scale(w.render, (w.screen_width, w.screen_height)), ((w.screen.get_width() - w.screen_width) // 2, (w.screen.get_height() - w.screen_height) // 2))
    pg.display.flip()

def draw_char(w):
    char = pg.image.load("gfx/AxemanCyan.png").convert_alpha()
    w.render.blit(char, input.pos)

def draw_fps(w, clock, font):
    if w.debug:
        if clock.get_fps() >= 30:
            fps = font.render(str(int(clock.get_fps())), False, "green")
        else:
            fps = font.render(str(int(clock.get_fps())), False, "red")
        w.render.blit(fps, (top_right, 0))
