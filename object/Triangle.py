import Hit
import Ray
from object.Object3D import Object3D


class Triangle(Object3D):

    def __init__(self, v1, v2, v3):
        p_color = (2, 2, 1)
        super().__init__(p_color)

    def intersect(self, ray: Ray, hit: Hit, tmin):
        print("Triangle")
