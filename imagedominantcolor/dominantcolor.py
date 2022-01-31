from PIL import Image
from collections import Counter


class DominantColor:

    resize_value = 16
    minimum_percent_difference_of_rgb = 10

    def __init__(self, image_path):
        self.image_path = image_path
        self.image = Image.open(self.image_path)
        self.resized_image = self.image.resize(
            (DominantColor.resize_value, DominantColor.resize_value), Image.ANTIALIAS
        )
        self.image.close()
        self.image_data = self.resized_image.getdata()
        self.generate_dominant_color_of_pixels_of_image_array()
        self.resized_image.close()
        self.counter = Counter(self.dominant_color_of_pixels_of_image_array)
        self.set_rgbl_value_of_image()
        self.set_dominat_color_of_image()
        self.rgb = (self.r, self.g, self.b)
        self.rgbl = (self.r, self.g, self.b, self.l)

    def __repr__(self):
        return "DominantColor(r:%s g:%s b:%s l:%s; dominant_color:%s; resize_value:%s; minimum_percent_difference_of_rgb:%s)" % (
            self.r,
            self.g,
            self.b,
            self.l,
            self.dominant_color,
            str(self.resize_value),
            str(self.minimum_percent_difference_of_rgb),
        )

    def __str__(self):
        return self.dominant_color

    def set_dominat_color_of_image(self):
        self.mpd = int(
            self.total_pixels * (DominantColor.minimum_percent_difference_of_rgb / 100)
        )

        if (self.r - self.mpd) > self.g and (self.r - self.mpd) > self.b:
            self.dominant_color = "r"
            return
        if (self.g - self.mpd) > self.b and (self.g - self.mpd) > self.r:
            self.dominant_color = "g"
            return
        if (self.b - self.mpd) > self.r and (self.b - self.mpd) > self.g:
            self.dominant_color = "b"
            return
        self.dominant_color = "l"

    def set_rgbl_value_of_image(self):
        r = self.counter.get("r")
        g = self.counter.get("g")
        b = self.counter.get("b")
        l = self.counter.get("l")
        self.r = r if r else 0
        self.g = g if g else 0
        self.b = b if b else 0
        self.l = l if l else 0

    def generate_dominant_color_of_pixels_of_image_array(self):
        self.total_pixels = 0
        self.dominant_color_of_pixels_of_image_array = []
        for i in range(DominantColor.resize_value):
            for j in range(DominantColor.resize_value):
                self.dominant_color_of_pixels_of_image_array.append(
                    self.dominant_color_of_pixel(self.image_data.getpixel((i, j)))
                )
                self.total_pixels += 1

    def dominant_color_of_pixel(self, pixel):
        if type(pixel) == int:
            return "l"
        r, g, b = pixel[0], pixel[1], pixel[2]
        if r > g and r > b:
            return "r"
        if g > b and g > r:
            return "g"
        if b > r and b > g:
            return "b"
        return "l"
