from pico2d import *
import random

direct = 0 # 방향을 위한 변수
upco = 0  # 점프를 위한 변수
start = True

class main_char:

    def __init__(self):
        global direct
        self.image = load_image('sdog.png') # 13752/12 =  573, 5230 /
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
            self.frame -= 1 # 5 ~ 11
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

class mob_s:

    def __init__(self):
        global find_mob
        self.image = []
        self.image.append(load_image('mmonkey.png')) # 5760/12 = 480 , 3840 / 8 = 480
        self.image.append(load_image('mbird.png')) # 3840/12 = 320 , 2560 / 8 = 320
        self.image.append(load_image('mcat.png')) # 5760/12 = 480 , 3840 / 8 = 480
        self.x, self.y = random.randint(100, 1400), 300 # x 축위치 랜덤
        self.species = random.randint(0, 7) # 8종의 몹 색깔중 랜덤
        if self.species > 3:
            self.frame = (self.species - 4) * 3 #시작 프레임위치
        else:
            self.frame = self.species * 3
        self.round = self.x
        self.mob = find_mob

    def action(self):

        self.draw()

    def get_frame(self):

        self.frame = ((self.frame + 1) % 3) + (self.species * 3)

    def draw(self):

        self.get_frame()

        if self.species > 3:
            if self.mob == 0:
                self.image[self.mob].clip_draw(self.frame * 480, 480 * 5, 480, 480, self.x, self.y, 100, 100)
            elif self.mob == 1:
                self.image[self.mob].clip_draw(self.frame * 320, 320 * 5, 320, 320, self.x, self.y, 100, 100)
            elif self.mob == 2:
                self.image[self.mob].clip_draw(self.frame * 480, 480 * 5, 480, 480, self.x, self.y, 100, 100)
        else:
            if self.mob == 0:
                self.image[self.mob].clip_draw(self.frame * 480, 480 * 1, 480, 480, self.x, self.y, 100, 100)
            elif self.mob == 1:
                self.image[self.mob].clip_draw(self.frame * 320, 320 * 1, 320, 320, self.x, self.y, 100, 100)
            elif self.mob == 2:
                self.image[self.mob].clip_draw(self.frame * 480, 480 * 1, 480, 480, self.x, self.y, 100, 100)

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

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
            elif event.key == SDLK_ESCAPE:
                start = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                direct = 0
            elif event.key == SDLK_LEFT:
                direct = 0
            elif event.key == SDLK_SPACE:
                upco = -1


def main_loop():
    global find_mob

    open_canvas(1600, 900)

    mdog = main_char()

    mobq = []

    for i in range(4):
        find_mob = random.randint(0,2)
        mobq += [mob_s()]


    while start:
        clear_canvas()
        # for mob_s in mobq:
        #     mob_s.action()
        for i in range(3):
            mobq[i].action()
        mdog.action()
        dog_events(mdog)
        delay(0.03)

        update_canvas()


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

