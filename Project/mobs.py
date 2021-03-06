from pico2d import *
import game_framework
import random


Bird_image_size = 320
Cat_image_size = 480
Monkey_image_size = 480

Monkey_size = 80       # size is pixel
Bird_size = 40
Cat_size = 60

PPM = (80.0 / 0.90)              # 80 pixel 90 cm pixel per meter
SPH_Monkey = 20.0                                      # Km / Hour , monkey speed
SPH_Bird = 123.0                                     # Km / Hour , bird speed
SPH_Cat = 35.0                                      # Km / Hour , cat speed
SPS_Monkey = (SPH_Monkey * 1000.0 / 60.0 / 60.0)            # Meter / Sec , monkey speed
SPS_Bird = (SPH_Bird * 1000.0 / 60.0 / 60.0)            # Meter / Sec , bird speed
SPS_Cat = (SPH_Cat * 1000.0 / 60.0 / 60.0)            # Meter / Sec , cat speed

SPP_Monkey = (SPS_Monkey * PPM)             # Pixel / Sec , monkey speed
SPP_Bird = (SPS_Bird * PPM)             # Pixel / Sec , bird speed
SPP_Cat = (SPS_Cat * PPM)             # Pixel / Sec , cat speed


TPA = 0.3
APT = 1.0 / TPA
FPA = 8


#-------------------------------------
#-------------------------------------


class Mob:
    image = None

    def __init__(self):
        self.x = 0
        self.y = 0
        self.s_point = 0
        self.dir = 0
        self.selection = 0
        self.frame = 0
        self.SPP = 0
        self.Mob_size = 0
        self.image_size = 0

    def get_location(self, x, y, direction=None):
        if direction == None:
            direction = self.dir
        self.x = x
        self.s_point = x
        self.y = y
        self.dir = direction

    def move_area(self, a):
        if self.x >= self.s_point + a:
            self.x = self.s_point + a
            self.dir = 1
        elif self.x <= self.s_point - a:
            self.x = self.s_point - a
            self.dir = 0

    def update(self):
        self.move_area(500)
        self.frame = ((self.frame + FPA * APT * game_framework.frame_time) % 3) + self.selection * 3
        if self.dir == 0:
            self.x += self.SPP * game_framework.frame_time
        elif self.dir == 1:
            self.x -= self.SPP * game_framework.frame_time
        self.x = clamp(100, self.x, 1500)

    def draw(self):
        if self.dir == 0: # 0 is right
            self.image.clip_draw(int(self.frame) * self.image_size, 0 * self.image_size, self.image_size, self.image_size, self.x, self.y, self.Mob_size, self.Mob_size)
        else: # 1 is left
            self.image.clip_draw(int(self.frame) * self.image_size, 1 * self.image_size, self.image_size, self.image_size, self.x, self.y, self.Mob_size, self.Mob_size)




class Bird(Mob):

    def __init__(self):
        if Bird.image == None:
            Bird.image = load_image('mbird.png')
        self.x = 800
        self.s_point = self.x
        self.y = 800
        self.SPP = SPP_Bird
        self.Mob_size = Bird_size
        self.frame = 0
        self.dir = random.randint(0, 1)

        self.selection = random.randint(0, 3)
        self.image_size = Bird_image_size



class Monkey(Mob):

    def __init__(self):
        if Monkey.image == None:
            Monkey.image = load_image('mmonkey.png')
        self.x = 800
        self.s_point = self.x
        self.y = 600
        self.SPP = SPP_Monkey
        self.Mob_size = Monkey_size
        self.frame = 0
        self.dir = random.randint(0, 1)

        self.selection = random.randint(0, 3)
        self.image_size = Monkey_image_size



class Cat(Mob):

    def __init__(self):
        if Cat.image == None:
            Cat.image = load_image('mcat.png')
        self.x = 800
        self.s_point = self.x
        self.y = 400
        self.SPP = SPP_Cat
        self.Mob_size = Cat_size
        self.frame = 0
        self.dir = random.randint(0, 1)
        self.selection = random.randint(0, 3)
        self.image_size = Cat_image_size






























#
# class mob_s:
#
#     def __init__(self):
#         global find_mob
#
#         self.mob = find_mob
#
#         if self.mob == 0:
#             self.image = load_image('mmonkey.png') # 5760/12 = 480 , 3840 / 8 = 480
#         elif self.mob == 1:
#             self.image = load_image('mbird.png') # 3840/12 = 320 , 2560 / 8 = 320
#         elif self.mob == 2:
#             self.image = load_image('mcat.png') # 5760/12 = 480 , 3840 / 8 = 480
#
#         self.species = random.randint(0, 7) # 8?????? ??? ????????? ??????
#
#         self.x, self.y = random.randint(100, 1400), 270 # x ????????? ??????
#
#         if self.species > 3:
#             self.frame = (self.species - 4) * 3 #?????? ???????????????
#         else:
#             self.frame = self.species * 3
#         self.round = self.x
#
#     def action(self):
#         pass
#
#     def get_frame(self):
#
#         self.frame = ((self.frame + 1) % 3) + (self.species * 3)
#
#     def draw(self):
#
#         self.get_frame()
#
#         if self.species > 3:
#             if self.mob == 0 or self.mob == 2:
#                 self.image.clip_draw(self.frame * 480, 480 * 5, 480, 480, self.x, self.y, 80, 80)
#             elif self.mob == 1:
#                 self.image.clip_draw(self.frame * 320, 320 * 5, 320, 320, self.x, self.y, 80, 80)
#         else:
#             if self.mob == 0 or self.mob == 2:
#                 self.image.clip_draw(self.frame * 480, 480 * 1, 480, 480, self.x, self.y, 80, 80)
#             elif self.mob == 1:
#                 self.image.clip_draw(self.frame * 320, 320 * 1, 320, 320, self.x, self.y, 80, 80)
