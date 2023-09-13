import pygame as pg
import input
import game
import character

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
    match game.char.state:
        case character.State.IDLE:
            game.char.counter = 0
            game.char.attack_counter = 0
            game.char.current_frame = 0
            rect = pg.Rect(game.char.current_frame, game.char.direction.value * 16, 16, 16)
        case character.State.MOVING:
            game.char.counter += 1
            if game.char.current_frame < 16 * 4:
                if game.char.counter % game.char.anim_speed == 0:
                    game.char.current_frame += 16
            else:
                if game.char.counter % game.char.anim_speed == 0:
                    game.char.current_frame = 0
            rect = pg.Rect(game.char.current_frame, game.char.direction.value * 16, 16, 16)
        case character.State.ATTACKING:
            game.char.attack_counter += 1
            match game.char.direction:
                case character.Direction.DOWN:
                    if game.char.attack_frame < 16 * 2:
                        if game.char.attack_counter % game.char.anim_speed == 0:
                            game.char.attack_frame += 16
                    else:
                        if game.char.attack_counter % game.char.anim_speed == 0:
                            game.char.attack_frame = 0
                    rect = pg.Rect(game.char.attack_frame, 80, 16, 16)
                case _:
                    if game.char.attack_frame >= 16: # error checking
                        game.char.attack_frame = 16
                    elif game.char.attack_frame < 16:
                        if game.char.attack_counter % game.char.anim_speed == 0:
                            game.char.attack_frame += 16
                    else:
                        if game.char.attack_counter % game.char.anim_speed == 0:
                            game.char.attack_frame = 0
                            
                    match game.char.direction:
                        case character.Direction.RIGHT:
                            rect = pg.Rect(48, 64 + game.char.attack_frame, 16, 16)
                        case character.Direction.UP:
                            rect = pg.Rect(64, 64 + game.char.attack_frame, 16, 16)
                        case character.Direction.LEFT:
                            rect = pg.Rect(80, 64 + game.char.attack_frame, 16, 16)

    AxemanSheet = pg.image.load("gfx/AxemanCyan.png").convert_alpha()
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
