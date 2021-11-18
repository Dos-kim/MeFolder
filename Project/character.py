from pico2d import *
import game_framework

# Location Number
RIGHT = 12
LEFT = 11
STANDING = 9
JUMPUP = 8
JUMPDOWN = 7
RUNNING = 6
char_size = 80  # size value is pixel
# time

# main event

RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, \
LSHIFT_DOWN, LSHIFT_UP, BACKR_TIMER, SPACE_DOWN, SPACE_UP, BACKS_TIMER = range(10)

# key table
key_event_table = {
    #move
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    #Dash Not yet
    (SDL_KEYDOWN, SDLK_LSHIFT): LSHIFT_DOWN,
    (SDL_KEYUP, SDLK_LSHIFT): LSHIFT_UP,
    #Jump
    (SDL_KEYDOWN, SDLK_SPACE): SPACE_DOWN,
    (SDL_KEYUP, SDLK_SPACE): SPACE_UP
}

# Speed

PPM = (80.0 / 0.90)              # 80 pixel 90 cm pixel per meter
RSPH = 30.0                     # Km / Hour , run speed(dog)
RSPM = (RSPH * 1000.0 / 60.0)   # Meter / Minute , run speed
RSPS = (RSPM / 60.0)            # Meter / Sec , run speed
RSPP = (RSPS * PPM)             # Pixel / Sec , run speed



#-------------------character action------------
#-------------------character action------------
class JumpState:
    def enter(main_char, event):
        if event == SPACE_DOWN:
            if main_char.y > 90: # not touching grand exeception or run double jump
                pass
            else:
                main_char.timer = 1000
        elif event == SPACE_UP:
            if main_char.timer >= 500:
                main_char.timer = 500
            if main_char.y == 90:
                main_char.timer = 0
                if main_char.velocity != 0:
                    main_char.add_event(BACKR_TIMER)
                elif main_char.velocity == 0 :
                    main_char.add_event(BACKS_TIMER)

        if event == RIGHT_DOWN:
            main_char.velocity += RSPP
        elif event == LEFT_DOWN:
            main_char.velocity -= RSPP
        elif event == RIGHT_UP:
            main_char.velocity -= RSPP
        elif event == LEFT_UP:
            main_char.velocity += RSPP

    def exit(main_char, event):
        pass

    def do(main_char):
        #frame
        if main_char.dir > 0:
            main_char.frame += 1
            if main_char.frame >= RIGHT + 6:
                main_char.frame = RIGHT
        else:
            main_char.frame -= 1
            if main_char.frame <= LEFT - 6:
                main_char.frame = LEFT
        #jump time
        main_char.timer -= 1
        if main_char.timer > 500:
            main_char.y += RSPP * game_framework.frame_time
            if main_char.y >= 300:
                main_char.y = 300
                main_char.timer = 500
        elif main_char.timer <= 500:
            main_char.y -= RSPP * game_framework.frame_time
            if main_char.y <= 90:
                main_char.y = 90
                main_char.timer = 0
                if main_char.velocity != 0:
                    main_char.add_event(BACKR_TIMER)
                else:
                    main_char.add_event(BACKS_TIMER)

        # side move
        main_char.x += main_char.velocity * game_framework.frame_time
        main_char.x = clamp(600, main_char.x, 1600 - 600)

    def draw(main_char):

        if main_char.timer > 500:
            if main_char.dir > 0:
                main_char.image.clip_draw(main_char.frame * 573, 523 * JUMPUP, 573, 523, main_char.x, main_char.y, char_size, char_size)
            else:
                main_char.image.clip_draw(main_char.frame * 573, 523 * JUMPUP, 573, 523, main_char.x, main_char.y, char_size, char_size)
        elif main_char.timer <= 500:
            if main_char.dir > 0:
                main_char.image.clip_draw(main_char.frame * 573, 523 * JUMPDOWN, 573, 523, main_char.x, main_char.y, char_size, char_size)
            else:
                main_char.image.clip_draw(main_char.frame * 573, 523 * JUMPDOWN, 573, 523, main_char.x, main_char.y, char_size, char_size)

class StandState:
    def enter(main_char, event):
        if event == RIGHT_DOWN:
            main_char.velocity += RSPP
        elif event == LEFT_DOWN:
            main_char.velocity -= RSPP
        elif event == RIGHT_UP:
            main_char.velocity -= RSPP
        elif event == LEFT_UP:
            main_char.velocity += RSPP


    def exit(main_char, event):
        pass

    def do(main_char):
        if main_char.dir > 0:
            main_char.frame += 1
            if main_char.frame >= RIGHT + 6:
                main_char.frame = RIGHT
        else:
            main_char.frame -= 1
            if main_char.frame <= LEFT - 6:
                main_char.frame = LEFT

    def draw(main_char):

        if main_char.dir > 0:
            main_char.image.clip_draw(main_char.frame * 573, 523 * STANDING, 573, 523, main_char.x, main_char.y, char_size, char_size)
        else:
            main_char.image.clip_draw(main_char.frame * 573, 523 * STANDING, 573, 523, main_char.x, main_char.y, char_size, char_size)

class RunState:
    def enter(main_char, event):
        if event == RIGHT_DOWN:
            main_char.velocity += RSPP
        elif event == LEFT_DOWN:
            main_char.velocity -= RSPP
        elif event == RIGHT_UP:
            main_char.velocity -= RSPP
        elif event == LEFT_UP:
            main_char.velocity += RSPP
        main_char.dir = main_char.velocity

    def exit(main_char, event):
        pass

    def do(main_char):
        if main_char.dir > 0:
            main_char.frame += 1
            if main_char.frame >= RIGHT + 7:
                main_char.frame = RIGHT
        else:
            main_char.frame -= 1
            if main_char.frame <= LEFT - 7:
                main_char.frame = LEFT
        main_char.x += main_char.velocity * game_framework.frame_time
        main_char.x = clamp(600, main_char.x, 1600 - 600)

    def draw(main_char):
        if main_char.dir > 0:
            main_char.image.clip_draw(main_char.frame * 573, 523 * RUNNING, 573, 523, main_char.x, main_char.y, char_size, char_size)
        else:
            main_char.image.clip_draw(main_char.frame * 573, 523 * RUNNING, 573, 523, main_char.x, main_char.y, char_size, char_size)



#-------------- key state table--------------
#-------------- key state table--------------

next_state_table = {
    StandState: {RIGHT_DOWN: RunState, LEFT_DOWN: RunState, RIGHT_UP: RunState, LEFT_UP: RunState,
               SPACE_DOWN: JumpState, SPACE_UP: JumpState, BACKR_TIMER: RunState, BACKS_TIMER: StandState},

    JumpState: {RIGHT_DOWN: JumpState, LEFT_DOWN: JumpState, RIGHT_UP: JumpState, LEFT_UP: JumpState,
               SPACE_DOWN: JumpState, SPACE_UP: JumpState, BACKR_TIMER: RunState, BACKS_TIMER: StandState},

    RunState: {RIGHT_DOWN: StandState, LEFT_DOWN: StandState, RIGHT_UP: StandState, LEFT_UP: StandState,
               SPACE_DOWN: JumpState, SPACE_UP: JumpState, BACKR_TIMER: RunState, BACKS_TIMER: StandState},
}



# ------------------------main class-----------
# ------------------------main class-----------

class Main_char:

    def __init__(self):
        self.x, self.y = 800, 90
        self.image = load_image('sdog.png')
        self.frame = RIGHT
        self.dir = 1
        self.velocity = 0
        self.timer = 0
        self.event_que = []
        self.cur_state = StandState
        self.cur_state.enter(self, None)

    def add_event(self, event):
        #Y insert 0, event?
        self.event_que.insert(0, event)

    def update(self):
        # fill here
        self.cur_state.do(self) #state doing
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event) #exit state
            self.cur_state = next_state_table[self.cur_state][event] #find next state
            self.cur_state.enter(self, event) # enter state


    def draw(self):
        self.cur_state.draw(self)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)







# direct = 0 # 방향을 위한 변수
# upco = 0  # 점프를 위한 변수
# start = True
#
# class main_char:
#
#     def __init__(self):
#         global direct
#         self.image = load_image('sdog.png') # 13752/12 =  573, 5230 /
#         self.x, self.y = 500, 300
#         self.frame = 12
#         self.direction = 0
#         self.jumc = 0
#
#     def action(self):
#         global direct, upco
#         self.direction = direct
#
#         if upco == 1:
#             self.jumc = 14
#         if upco == -1:
#             self.jumc = 7
#
#         if self.jumc != 0:
#             self.jump()
#         elif self.jumc == 0 and self.direction == 0:
#             self.stand()
#         elif self.jumc == 0 and self.direction == 1 or self.direction == -1:
#             self.running()
#
#     def jump(self):
#         global upco
#
#
#         if direct == -1:
#             self.direction = -1
#         elif direct == 1:
#             self.direction = 1
#
#         if self.direction == 1:
#             self.frame += 1
#             self.x += self.direction * 5
#             if self.frame >= 19:
#                 self.frame = 12
#         elif self.direction == -1:
#             self.frame -= 1 # 5 ~ 11
#             self.x += self.direction * 5
#             if self.frame <= 5:
#                 self.frame = 11
#
#         if self.jumc > 7:
#             self.y += 5
#             self.image.clip_draw(self.frame * 573, 523 * 8, 573, 523, self.x, self.y, 100, 100)
#             self.jumc -= 1
#         elif self.jumc <= 7:
#             self.y -= 5
#             if self.y <= 300:
#                 self.y = 300
#                 upco = 0
#             self.image.clip_draw(self.frame * 573, 523 * 7, 573, 523, self.x, self.y, 100, 100)
#             self.jumc -= 1
#
#
#     def stand(self):
#
#         if self.frame >= 12:
#             self.frame += 1 # 한칸이동 12번 프레임으로 변경
#             if self.frame >= 19:
#                 self.frame = 12
#         elif self.frame < 12:
#             self.frame -= 1 # 한칸이동 11번 프레임으로 변경
#             if self.frame <= 4:
#                 self.frame = 11
#
#         self.image.clip_draw(self.frame * 573, 523 * 9, 573, 523, self.x, self.y, 100, 100)
#
#     def running(self):
#
#         if direct == -1:
#             self.direction = -1
#         elif direct == 1:
#             self.direction = 1
#
#         if self.direction == 1:
#             self.frame += 1
#             self.x += self.direction * 5
#             if self.frame == 21:
#                 self.frame = 12
#         elif self.direction == -1:
#             self.frame -= 1 # 3 ~ 11
#             self.x += self.direction * 5
#             if self.frame == 2:
#                 self.frame = 11
#
#         self.image.clip_draw(self.frame * 573, 523 * 6, 573, 523, self.x, self.y, 100, 100)
#
#
