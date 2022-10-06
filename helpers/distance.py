import math

def calc_distance(p1, p2):
    eDistance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
    #print(eDistance)
    return eDistance