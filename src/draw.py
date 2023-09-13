import pygame as pg
import input
import game

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
    game.char.counter += 1

    if game.char.moving:
        if game.char.current_frame < 16 * 4:
            if game.char.counter % 5 == 0:
                game.char.current_frame += 16
        else:
            if game.char.counter % 5 == 0:
                game.char.current_frame = 0
    else:
        game.char.current_frame = 0
        
    AxemanSheet = pg.image.load("gfx/AxemanCyan.png").convert_alpha()
    rect = pg.Rect(game.char.current_frame, game.char.direction.value * 16, 16, 16)
    char = AxemanSheet.subsurface(rect)
    w.render.blit(char, input.pos)

def draw_fps(w, clock, font):
    if w.debug:
        if clock.get_fps() >= 30:
            fps = font.render(str(int(clock.get_fps())), False, "green")
        else:
            fps = font.render(str(int(clock.get_fps())), False, "red")
        top_right = 303
        w.render.blit(fps, (top_right, 0))
