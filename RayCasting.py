from PIL import Image

from FileReader import JsonReader
from Hit import Hit


class RayCasting:

    # When we want to show any thing we need a few things
    # so we need scene frame, background color, camera and objects
    # this funtion carries above needs
    def get_ray_casing_scene(self, pScene, near, far):

        file_reader = JsonReader(pScene)
        orthographic_cam = file_reader.orthographic_camera_factory()
        background_color = file_reader.background_color_factory()
        group = file_reader.group_factory()
        hit = Hit(0, [0, 0, 0])

        frame_size = (300, 300)
        image = Image.new('RGB', frame_size, background_color)
        image_depth = Image.new('RGB', frame_size, background_color)

        # for each pixel
        for y in range(frame_size[0]):
            for x in range(frame_size[1]):
                ray = orthographic_cam.generate_ray(1.0 * x / frame_size[0], 1.0 * y / frame_size[1])

                distance = 30
                pixel_color = background_color
                depth_color = background_color
                for s in group:

                    is_hit = s.intersect(ray, hit, 1)

                    if is_hit:
                        if distance > hit.t:
                            distance = hit.t
                            pixel_color = hit.color
                            depth = (far - hit.t) / (far - near)
                            deep_color = (int(depth * 255))
                            depth_color = (deep_color, deep_color, deep_color)

                image.putpixel((y, x), pixel_color)
                image_depth.putpixel((y, x), depth_color)

        # this section is working for colored images
        image.show()
        image.save(pScene + ".jpg")
        image.close()

        # this section is working for uncolored images
        image_depth.show()
        image_depth.save(pScene + "_depth.jpg")
        image_depth.close()