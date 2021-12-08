from pico2d import *

class Background:
    def __init__(self):
        self.image = load_image('forest/grass.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(8400, 600)


    # fill here
    def get_bb(self):
        return 0, 0, 0, 0
