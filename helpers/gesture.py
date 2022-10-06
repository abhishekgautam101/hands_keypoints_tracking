import numpy as np
from helpers.distance import calc_distance
from helpers.overlay import overlayImage

def check_gesture(image,image_width, image_height, index_pos, thumb_pos, img1, img1_pos):
    index_x, index_y = index_pos
    thumb_x, thumb_y = thumb_pos

    if calc_distance(index_pos, thumb_pos) < 30:
        #print("clicked")
        try:
            image = overlayImage(img1, image, index_pos)
            img1_pos = index_pos
        except Exception as e:
            pass
    

    return image, img1_pos