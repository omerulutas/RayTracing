from abc import ABC, abstractmethod


# This class is super class of 3D Objects
class Object3D(ABC):

    # Every object has color so we need to assign object color
    def __init__(self, rgb):
        self.color = rgb

    # Each object has it own intersection function, so this function will override by sub classes
    @abstractmethod
    def intersect(self, Ray, hit, tmin):
        pass
