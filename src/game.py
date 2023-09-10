from enum import Enum
import pygame as pg
import window
import input
import draw

class GameState(Enum):
    TITLE = 1
    MENU = 2
    GAME = 3

def init():
    pg.init()
    w = window.Window()
    clock = pg.time.Clock()
    font = pg.font.Font("gfx/alagard.ttf", w.font_size)
    state = GameState(GameState.GAME)
    pg.display.set_caption(w.title)
    return font, clock, w, state

font, clock, w, state = init()

def run():
    while w.running:
        clock.tick(60)
        input.get_input()

        match state:
            case state.TITLE:
                pass
            case state.MENU:
                pass
            case state.GAME:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        w.running = False
                    if event.type == pg.VIDEORESIZE:
                        window.scale_window(w)
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_ESCAPE:
                            w.running = False
                        if event.key == pg.K_RETURN and event.mod & pg.KMOD_ALT:
                            window.toggle_fullscreen(w)
                        if event.key == pg.K_SPACE:
                            coin_sfx = pg.mixer.Sound("sfx/coin.wav")
                            coin_sfx.play()

        draw.draw(w, clock, font)
    pg.quit()
