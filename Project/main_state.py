from pico2d import *
import game_world
import game_framework


from character import Main_char
from mobs import *


name = "MainState"

main_char = None
mobs = None



def enter():
    global main_char
    main_char = Main_char()
    game_world.add_object(main_char, 1)

    global mobs
    mobs = [Bird(), Monkey(), Cat()]
    game_world.add_objects(mobs, 1)


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
            main_char.handle_event(event)



def update():
    for game_object in game_world.all_objects():
        game_object.update()
    #If my computer dont' use delay, frame_rate => 500

def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    delay(0.025)
    update_canvas()



def obj_location():
    pass




