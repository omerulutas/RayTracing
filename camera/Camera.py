from abc import ABC, abstractmethod


# Camera class is super class of camera types
class Camera(ABC):

    # Each camera has allocation point
    # This method will be implemented by sub classes
    @abstractmethod
    def generate_ray(self, x, y):
        pass