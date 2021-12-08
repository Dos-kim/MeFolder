from pico2d import *
import game_framework

class Brick:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.image = load_image('forest/first_ground.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(1670, -10)
