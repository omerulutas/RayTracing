from object.Object3D import Object3D


# Group class stores list of the 3D objects (for now just spheres)
class Group(Object3D):

    def __init__(self):
        self.objects = []

    def intersect(self, ray, hit, tmin):
        for object in self.objects:
            object.intersect(self, ray, hit, tmin)
