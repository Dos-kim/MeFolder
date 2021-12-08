from pico2d import *
import game_world
import server
import game_framework

from ground import Background
from character import Main_char
from brick import Brick
from mobs import *


name = "MainState"




def enter():
    server.main_char = Main_char()
    game_world.add_object(server.main_char, 1)

    # server.mobs = [Bird(), Monkey(), Cat()]
    # game_world.add_objects(server.mobs, 1)

    server.background = Background()
    game_world.add_object(server.background, 0)

    server.bricks = Brick()
    game_world.add_object(server.bricks, 0)

def exit():
    game_world.clear()



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
            server.main_char.handle_event(event)



def update():
    for game_object in game_world.all_objects():
        game_object.update()
    #If my computer dont' use delay, frame_rate => 500

def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    # Someday, delay out
    # delay(0.025)
    update_canvas()



def obj_location():
    pass




