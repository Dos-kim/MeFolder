from pico2d import *
import game_framework
import server



class Dive:
    Image = None
    def __init__(self, x=None, y=None, mb=None, bb=None):
        if x == None:
            self.x = 0
        else:
            self.x = 0
        if y == None:
            self.y = 0
        else:
            self.y = y
        if mb == None:
            self.mb = 0
        else:
            self.mb = mb
        self.bb = bb


    def update(self):
        self.x -= server.main_char.velocity * game_framework.frame_time

    def get_bb(self):
        return self.x - self.bb, self.y, self.x + self.bb, self.y+1


    def draw(self):
        self.image.clip_draw(0, 0, 80, 80, self.x, self.y)
        draw_rectangle(*self.get_bb())