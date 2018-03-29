from abc import abstractmethod

from camera.Camera import Camera


class PerspectiveCamera(Camera):

    def __init__(self, p_center, p_direction, p_up, p_angle):
        self.center = p_center
        self.direction = p_direction
        self.up = p_up
        self.agnle = p_angle

    def generate_ray(self, x, y):
        pass