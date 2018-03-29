from PIL import Image
from pathlib import Path
import os

from FileReader import JsonReader
from Hit import Hit
from object.Group import Group


class RayCasting:

    # When we want to show any thing we need a few things
    # so we need scene frame, background color, camera and objects
    # this funtion carries above needs
    def get_ray_casing_scene(self, pScene, near, far):

        file_reader = JsonReader(pScene)
        orthographic_cam = file_reader.orthographic_camera_factory()
        background_color = file_reader.background_color_factory()
        file_group = file_reader.group_factory()
        group = Group((0, 0, 0), file_group)

        hit = Hit(0, [0, 0, 0])

        frame_size = (100, 100)
        image = Image.new('RGB', frame_size, background_color)
        image_depth = Image.new('RGB', frame_size, background_color)

        tmin = 0.1
        # for each pixel
        for y in range(frame_size[0]):
            for x in range(frame_size[1]):
                ray = orthographic_cam.generate_ray(1.0 * x / frame_size[0], 1.0 * y / frame_size[1])

                group.intersect(ray, hit, tmin)

                depth = (far - hit.t) / (far - near)
                depth_color = (int(depth * 255))
                depth_color_tuple = (depth_color, depth_color, depth_color)

                image.putpixel((y, x), group.color)
                image_depth.putpixel((y, x), depth_color_tuple)

        # this section is working for colored images
        x = os.path.splitext(pScene)[0]
        print(x)
        image.show()
        image.save(x + ".jpg")
        image.close()

        # this section is working for uncolored images
        image_depth.show()
        image_depth.save(x + "_depth.jpg")
        image_depth.close()
