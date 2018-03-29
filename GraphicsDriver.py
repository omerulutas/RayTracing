import sys

import os
from PIL import Image
from Hit import Hit
from FileReader import JsonReader
from RayCasting import RayCasting
from RayTracing import RayTracing


class Driver:

    def __init__(self, p_rayCasting: RayCasting, p_rayTracing: RayTracing):
        self.rayCasting = p_rayCasting
        self.rayTracing = p_rayTracing

    def rayCasting_actions(self, scene, near, far):
        self.rayCasting.get_ray_casing_scene(scene, near, far)

    def get_ray_tracing_scene(self):
        print("ray tracing")

    def file_selector(self):
        fn = getattr(sys.modules['__main__'], '__file__')
        root_path = os.path.abspath(os.path.dirname(fn))
        root_path = root_path + '\\' + 'scene\\ray_casting\\scene1.json'

        return root_path


# this function is main function of the system
def main():
    casting = RayCasting()
    tracing = RayTracing()
    d = Driver(casting, tracing)
    d.file_selector()

    print(d.file_selector())
    selection = input('Enter your selection: '
                      '\n1 for Ray casting '
                      '\n2 for Ray tracing\n')

    if selection == '1':
        scenes = ['scene\\ray_casting\\scene1.json', 'scene\\ray_casting\\scene2.json']
        far = [11, 11.5]
        near = [9, 8]
        for i in range(len(scenes)):
            d.rayCasting_actions(scenes[i], near[i], far[i])

    elif selection == '2':
        d.get_ray_tracing_scene()


main()
