import json
import os
import sys
from camera.OrthographicCamera import OrthographicCamera
from camera.PerspectiveCamera import PerspectiveCamera
from object.Sphere import Sphere
from object.Plane import Plane
from object.Triangle import Triangle
from Light import Light
from object.Transformation import Transformation


# JsonReader class is used for reading data from json file and create objects
class JsonReader:

    def __init__(self, fileName):

        self.data = json  #
        # Firstly we need to hand root directory
        self.get_json_object(fileName)

    def get_json_object(self, file):
        with open(file) as data_file:
            json_data = json.load(data_file)
            self.data = json_data

    # orthographic_camera_factory function is a orthographic camera factory
    # creates orthographic camera by using necessary parameters
    def orthographic_camera_factory(self):
        orthographic_camera = self.data['orthocamera']
        center = orthographic_camera['center']
        direction = orthographic_camera['direction']
        up = orthographic_camera['up']
        size = int(orthographic_camera['size'])
        return OrthographicCamera(center, direction, up, size)

    def perspective_camera_factory(self):
        perspective_camera = self.data['perspectivecamera']
        center = perspective_camera['center']
        direction = perspective_camera['direction']
        up = perspective_camera['up']
        angle = perspective_camera['angle']
        return PerspectiveCamera(center, direction, up, angle)

    # background_color_factory creates background color by using json file item
    def background_color_factory(self):
        return tuple(self.data['background']['color'])

    # # background_ambient_factory creates background ambient by using json file item
    def background_ambient_factory(self):
        return tuple(self.data['background']['ambient'])

    # light_factory creates light class by using necessary parameters
    def light_factory(self):
        direction = self.data['light']['direction']
        color = self.data['light']['color']
        return Light(direction, color)

    def sphere_factory(self, sphere):
        center = sphere['center']
        radius = float(sphere['radius'])
        color = tuple(sphere['color'])
        return Sphere(color, radius, center)

    def plane_factory(self, plane):
        normal = plane['normal']
        offset = plane['offset']
        color = tuple(plane['color'])
        return Plane(normal, offset, color)

    def triangle_factory(self, triangle):
        v1 = triangle['v1']
        v2 = triangle['v2']
        v3 = triangle['v3']
        return Triangle(v1, v2, v3)

    def transform_factory(self, transform):
        if isinstance(transform, dict) and 'zrotate' in transform:
            zrotatev = transform['zrotate']
        scale = transform['scale']
        sphere = self.sphere_factory(transform['sphere'])

        return Transformation(scale, sphere)

    # group_factory function creates object list and return the created list
    def group_factory(self):
        group = self.data['group']
        item_list = []

        for item in group:
            if isinstance(item, dict) and 'sphere' in item:
                item_list.append(self.sphere_factory(item['sphere']))

            if isinstance(item, dict) and 'plane' in item:
                item_list.append(self.plane_factory(item['plane']))

            if isinstance(item, dict) and 'triangle' in item:
                item_list.append(self.triangle_factory(item['triangle']))

            if isinstance(item, dict) and 'transform' in item:
                item_list.append(self.transform_factory(item['transform']))

        return item_list
