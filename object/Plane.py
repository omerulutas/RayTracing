from object.Object3D import Object3D


class Plane(Object3D):

    def __init__(self, p_normal, p_d, p_color):
        super().__init__(p_color)
        self.normal = p_normal
        self.d = p_d

    def intersect(self, Ray, hit, tmin):
        print("plane")



