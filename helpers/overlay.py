import cv2

def overlayImage(s_img,l_img,pos):
    x_offset, y_offset = pos
    l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]] = s_img
    return l_img