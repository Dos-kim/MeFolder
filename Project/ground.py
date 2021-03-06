from pico2d import *
import server

class Background:

    def __init__(self):
        self.image = load_image('forest/grass.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h


    def draw(self):
        # fill here
        self.image.clip_draw_to_origin(self.window_left, self.window_bottom, server.background.canvas_width, server.background.canvas_height, 0, 0 )
        pass

    def update(self):
        # fill here
        self.window_left = clamp(0, int(server.main_char.x) -server.background.canvas_width // 2, server.background.w - server.background.canvas_width)
        self.window_bottom = clamp(0, int(server.main_char.y) - server.background.canvas_height // 2, server.background.h - server.background.canvas_height)
        pass

    def handle_event(self, event):
        pass








#
# class Background:
#     def __init__(self):
#         self.image = load_image('forest/grass.png')
#
#     def update(self):
#         pass
#
#     def draw(self):
#         self.image.draw(7480, 600)
#
#
#     # fill here
#     def get_bb(self):
#         return 0, 0, 0, 0
