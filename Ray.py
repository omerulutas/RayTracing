import numpy as np


# Ray class has origin and direction information
class Ray:

    def __init__(self, p_origin, p_direction):
        self.origin = np.array(p_origin)
        self.direction = np.array(p_direction)
