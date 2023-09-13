from enum import Enum

class Direction(Enum):
    DOWN = 0
    UP = 1
    RIGHT = 2
    LEFT = 3

class Character():
    def __init__(self):
        self.moving = False
        self.direction = Direction.DOWN
        self.counter = 0
        self.current_frame = 0
        self.frame = 0