from pico2d import *

class running_Char:
    def __init__(self):
        self.image = load_image('shadow dog sprite sheet.png')
        self.x , self.y = 500, 300
        self.frame = 0

    def update(self):
        self.x += 1
        self.frame = (self.frame + 1) % 9
        delay(0.03)

    def running(self):
        self.image.clip_draw(self.frame * 573, 523 * 6, 573, 523, self.x, self.y)


def run_events():
    global run
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            run = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            run = False

open_canvas(2400, 1400)

run_ch = running_Char()

run = True

while run:
    run_events()

    run_ch.update()

    clear_canvas()

    run_ch.running()

    update_canvas()

