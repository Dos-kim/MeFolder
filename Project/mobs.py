from pico2d import *
import random

class mob_s:

    def __init__(self):
        global find_mob

        self.mob = find_mob

        if self.mob == 0:
            self.image = load_image('mmonkey.png') # 5760/12 = 480 , 3840 / 8 = 480
        elif self.mob == 1:
            self.image = load_image('mbird.png') # 3840/12 = 320 , 2560 / 8 = 320
        elif self.mob == 2:
            self.image = load_image('mcat.png') # 5760/12 = 480 , 3840 / 8 = 480

        self.species = random.randint(0, 7) # 8종의 몹 색깔중 랜덤

        self.x, self.y = random.randint(100, 1400), 270 # x 축위치 랜덤

        if self.species > 3:
            self.frame = (self.species - 4) * 3 #시작 프레임위치
        else:
            self.frame = self.species * 3
        self.round = self.x

    def action(self):
        pass

    def get_frame(self):

        self.frame = ((self.frame + 1) % 3) + (self.species * 3)

    def draw(self):

        self.get_frame()

        if self.species > 3:
            if self.mob == 0 or self.mob == 2:
                self.image.clip_draw(self.frame * 480, 480 * 5, 480, 480, self.x, self.y, 80, 80)
            elif self.mob == 1:
                self.image.clip_draw(self.frame * 320, 320 * 5, 320, 320, self.x, self.y, 80, 80)
        else:
            if self.mob == 0 or self.mob == 2:
                self.image.clip_draw(self.frame * 480, 480 * 1, 480, 480, self.x, self.y, 80, 80)
            elif self.mob == 1:
                self.image.clip_draw(self.frame * 320, 320 * 1, 320, 320, self.x, self.y, 80, 80)
