from object.Object3D import Object3D


# Group class stores list of the 3D objects (for now just spheres)
class Group(Object3D):

    def __init__(self):
        self.objects = []

    def __init__(self, color, group):
        super().__init__(color)
        self.objects = group

    def intersect(self, ray, hit, tmin):
        t_max = 10000
        self.color = (0, 0, 0)
        for object in self.objects:
            is_hit = object.intersect(ray, hit, tmin)
            if is_hit:
                if hit.t < t_max:
                    t_max = hit.t
                    self.color = object.color

        hit.t = t_max

