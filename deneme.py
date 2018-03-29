import json

import sys

import os
from FileReader import JsonReader
from Hit import Hit
from Ray import Ray
from object.Transformation import Transformation
from object.Triangle import Triangle


class deneme():

    def dene(self):
        a =[0, 0, 0]
        b=[0, 0, 0]
        rar = Ray(a, b);
        hit = Hit(0, [0, 0, 0])

        file = JsonReader('scene\\scene5_sphere_triangle.json')
        ob = file.group_factory()

        for c in ob:
            c.intersect(rar, hit, 1 )




de = deneme()
de.dene()
