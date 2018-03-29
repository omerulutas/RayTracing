from PIL import Image
from Hit import Hit
from FileReader import JsonReader
from RayCasting import RayCasting


class Driver:

    def ray_casting(self):
        ray_casting_scene = RayCasting

        scenes = ['scene\\scene1', 'scene\\scene2']
        far = [11, 11.5]
        near = [9, 8]
        for i in range(len(scenes)):
            ray_casting_scene.get_ray_casing_scene(scenes[i], near[i], far[i])

    def get_ray_tracing_scene(self):
        print("ray tracing")


# this function is main function of the system
def main():
    d = Driver()

    selection = input('Enter your selection: '
                      '\n1 for Ray casting '
                      '\n2 for Ray tracing\n')

    if selection == '1':
        d.ray_casting()

    elif selection == '2':
        d.get_ray_tracing_scene()


main()
