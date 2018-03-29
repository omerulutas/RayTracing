from object.Object3D import Object3D
from Ray import Ray
from Hit import Hit
import numpy as np


# This is 3D sphere class, also this class is Object3D
class Sphere(Object3D):

    # Each Sphere object has color, radius and center
    def __init__(self, color, pRadius, pCenter):
        super().__init__(color)
        self.radius = np.array(pRadius)
        self.center = np.array(pCenter)

    # THis intersect function is used for controlling intersection with sphere and ray
    # if sphere and ray have intersection than returns true and set hit's color and t value
    def intersect(self, ray: Ray, hit: Hit, tmin):
        # create a vector from origin to center
        #L
        originCenterVec = ray.origin - self.center

        # define equation coefficients
        a = np.dot(ray.direction, ray.direction)

        #tc
        b = 2 * np.dot(originCenterVec, ray.direction)


        c = np.dot(originCenterVec, originCenterVec) - self.radius * self.radius

        # calculate discriminant of the intersection test
        disc = b * b - 4 * a * c

        # if disc less than 0 it means that there is no intersection and return false
        if disc < 0:
            return False

        # if disc more than 0 it means that there is a intersection
        else:
            disc_root = np.sqrt(disc)

            # if disc_root is equal to 0 than there is a one intersection and this is tangent
            # and set disc_root to t value
            if disc_root == 0:
                t = (disc - b) / 2 * a

            # if disc_root is more than 0 it shows that there are two intersection
            # and select nearest intersection point
            else:
                t0 = (-b - disc_root) / (2 * a)
                t1 = (-b + disc_root) / (2 * a)

                if t0 < t1:
                    t = t0
                else:
                    t = t1

            if t < tmin:
                hit.color = (0, 0, 0)
                return False

            else:
                hit.color = self.color
                hit.t = t

                return True
