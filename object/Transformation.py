from object.Object3D import Object3D


class Transformation(Object3D):

    def __init__(self, p_m, p_object: Object3D):
        p_color = (2, 2, 1)
        super().__init__(p_color)
        self.m = p_m
        self.object = p_object

    def intersect(self, Ray, hit, tmin):
        print("Transformation")
