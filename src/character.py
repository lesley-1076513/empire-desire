from enum import Enum

class Direction(Enum):
    DOWN = 0
    UP = 1
    RIGHT = 2
    LEFT = 3

class State(Enum):
    IDLE = 0
    MOVING = 1
    ATTACKING = 2

class Character():
    def __init__(self):
        self.state = State.IDLE
        self.direction = Direction.DOWN
        self.anim_speed = 8 # willekeurig
        self.current_frame = 0
        self.counter = 0
        self.frame = 0
        self.attack_counter = 0
        self.attack_frame = 0