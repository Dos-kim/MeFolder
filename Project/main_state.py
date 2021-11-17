import random
import json
import os

from pico2d import *

import game_framework


from character import Main_char



name = "MainState"

main_char = None




def enter():
    global main_char
    main_char = Main_char()




def exit():
    pass



def pause():
    pass


def resume():
    pass


def key_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            main_char.handle_event(event)



def update():
    main_char.update()
    #If my computer dont' use delay, frame_rate => 500
    delay(0.02)

def draw():
    clear_canvas()
    main_char.draw()
    update_canvas()






