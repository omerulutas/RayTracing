from camera.Camera import Camera
from Ray import Ray
import numpy as np

# OrthographicCamera is a Camera
# this class extended from Camera class
class OrthographicCamera(Camera):

    # OrthographicCamera has center, direction, up vectors and size features
    def __init__(self, p_center, p_direction, p_up, p_size):
        self.center = np.array(p_center)
        self.direction = np.array(p_direction)
        self.up = np.array(p_up)
        self.size = p_size

    # generate_ray function generate ray according to x and y values
    # and than returns created ray instance
    def generate_ray(self, x, y):
        a = np.array(self.direction)
        b = np.array(self.up)
        horizontal = np.cross(b, a)
        ray_origin = self.center + (x - 0.5) * self.size * horizontal + (y - 0.5) * self.size * self.up
        ray_direction = self.direction
        ray = Ray(ray_origin, ray_direction)
        return ray
