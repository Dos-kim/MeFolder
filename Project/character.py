from pico2d import *
import pico2d

direct = 0
upco = 0

class main_char:

    def __init__(self):
        global direct
        self.image = load_image('sdog.png')
        self.x, self.y = 500, 300
        self.frame = 12
        self.direction = 0
        self.jumc = 0

    def action(self):
        global direct, upco
        self.direction = direct

        if upco == 1:
            self.jumc = 14
        if upco == -1:
            self.jumc = 7

        if self.jumc != 0:
            self.jump()
        elif self.jumc == 0 and self.direction == 0:
            self.stand()
        elif self.jumc == 0 and self.direction == 1 or self.direction == -1:
            self.running()

    def jump(self):
        global upco


        if direct == -1:
            self.direction = -1
        elif direct == 1:
            self.direction = 1

        if self.direction == 1:
            self.frame += 1
            self.x += self.direction * 5
            if self.frame == 19:
                self.frame = 12
        elif self.direction == -1:
            self.frame -= 1 # 3 ~ 11
            self.x += self.direction * 5
            if self.frame == 5:
                self.frame = 11

        if self.jumc > 7:
            self.y += 5
            self.image.clip_draw(self.frame * 573, 523 * 8, 573, 523, self.x, self.y, 100, 100)
            self.jumc -= 1
        elif self.jumc <= 7:
            self.y -= 5
            if self.y <= 300:
                self.y = 300
                upco = 0
            self.image.clip_draw(self.frame * 573, 523 * 7, 573, 523, self.x, self.y, 100, 100)
            self.jumc -= 1


    def stand(self):

        if self.frame >= 12:
            self.frame += 1 # 한칸이동 12번 프레임으로 변경
            if self.frame >= 19:
                self.frame = 12
        elif self.frame < 12:
            self.frame -= 1 # 한칸이동 11번 프레임으로 변경
            if self.frame <= 4:
                self.frame = 11

        self.image.clip_draw(self.frame * 573, 523 * 9, 573, 523, self.x, self.y, 100, 100)

    def running(self):

        if direct == -1:
            self.direction = -1
        elif direct == 1:
            self.direction = 1

        if self.direction == 1:
            self.frame += 1
            self.x += self.direction * 5
            if self.frame == 21:
                self.frame = 12
        elif self.direction == -1:
            self.frame -= 1 # 3 ~ 11
            self.x += self.direction * 5
            if self.frame == 2:
                self.frame = 11

        self.image.clip_draw(self.frame * 573, 523 * 6, 573, 523, self.x, self.y, 100, 100)


def dog_events(dog):
    global start, direct, upco
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            start = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                direct = 1
            elif event.key == SDLK_LEFT:
                direct = -1
            elif event.key == SDLK_SPACE:
                upco = 1

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                direct = 0
                if c_int == 79:
                    direct = -1
            elif event.key == SDLK_LEFT:
                direct = 0
                if c_int == 80:
                    direct = 1
            elif event.key == SDLK_SPACE:
                upco = -1


open_canvas(1600, 900)

mdog = main_char()

start = True

while start:

    dog_events(mdog)
    delay(0.03)
    clear_canvas()

    mdog.action()


    update_canvas()
