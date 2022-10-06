import time
from pynput.mouse import Button, Controller
from helpers.distance import calc_distance
from helpers.screen_w_h import get_screen_w_h

class Cursor:
    def __init__(self, initial_pointer_value):
        self.initial_pointer_value = initial_pointer_value
        self.mouse = Controller()
    

    def left_click(self):
        self.mouse.press(Button.left)
        self.mouse.release(Button.left)

    def right_click(self):
        self.mouse.press(Button.right)
        self.mouse.release(Button.right)

    def move_cursor(self, index_pos, thumb_pos, ring_pos, little_pos):

        new_pos = (little_pos[0] + self.initial_pointer_value[0], little_pos[1] + self.initial_pointer_value[1])
        self.mouse.position = new_pos

        if calc_distance(index_pos, thumb_pos) < 50:
            self.mouse.press(Button.left)
        else:
            self.mouse.release(Button.left)
            
        # if calc_distance(thumb_pos, ring_pos) < 50:
        #     self.initial_pointer_value = little_pos