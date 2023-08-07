from PIL import Image
from collections import Counter
from typing import Tuple, List


class DominantColor:

    resize_value: int = 16
    minimum_percent_difference_of_rgb: int = 10

    def __init__(self, image_path: str) -> None:
        self.image_path = image_path
        self.image = Image.open(self.image_path)
        self.dominant_color: str = ""
        self.r: int = 0
        self.g: int = 0
        self.b: int = 0
        self.l: int = 0
        self.resized_image = self.image.resize(
            (DominantColor.resize_value, DominantColor.resize_value), Image.Resampling.LANCZOS
        ).convert("RGBA")
        self.image.close()
        self.image_data = self.resized_image.getdata()
        self.generate_dominant_color_of_pixels_of_image_array()
        self.resized_image.close()
        self.counter = Counter(self.dominant_color_of_pixels_of_image_array)
        self.set_rgbl_value_of_image()
        self.set_dominat_color_of_image()
        self.rgb = (self.r, self.g, self.b)
        self.rgbl = (self.r, self.g, self.b, self.l)

    def __repr__(self) -> str:
        return (
            "DominantColor(r:%s g:%s b:%s l:%s; dominant_color:%s; resize_value:%s; minimum_percent_difference_of_rgb:%s)"
            % (
                self.r,
                self.g,
                self.b,
                self.l,
                self.dominant_color,
                str(self.resize_value),
                str(self.minimum_percent_difference_of_rgb),
            )
        )

    def __str__(self) -> str:
        return self.dominant_color

    def set_dominat_color_of_image(self) -> None:
        self.mpd = int(
            self.total_pixels * (DominantColor.minimum_percent_difference_of_rgb / 100)
        )

        if (
            max(
                set(self.dominant_color_of_pixels_of_image_array),
                key=self.dominant_color_of_pixels_of_image_array.count,
            )
            == "l"
        ):
            self.dominant_color = "l"
            return

        if (self.r - self.mpd) > self.g and (self.r - self.mpd) > self.b:
            self.dominant_color = "r"
            return
        if (self.g - self.mpd) > self.b and (self.g - self.mpd) > self.r:
            self.dominant_color = "g"
            return
        if (self.b - self.mpd) > self.r and (self.b - self.mpd) > self.g:
            self.dominant_color = "b"
            return
        self.dominant_color = "n"

    def set_rgbl_value_of_image(self) -> None:
        """
        Sets the value for attribute r,g,b and l.

        Note that these attributes indicates the number of
        pixels which have dominating r,g,b and l values repectively.

        The sum of r,g,b and l should be equal to total_pixels attribute.
        """
        self.r = self.counter.get("r", 0)
        self.g = self.counter.get("g", 0)
        self.b = self.counter.get("b", 0)
        self.l = self.counter.get("l", 0)

    def generate_dominant_color_of_pixels_of_image_array(self) -> None:

        self.total_pixels: int = 0
        self.dominant_color_of_pixels_of_image_array: List = []

        for i in range(DominantColor.resize_value):

            for j in range(DominantColor.resize_value):

                self.dominant_color_of_pixels_of_image_array.append(
                    self.dominant_color_of_pixel(self.image_data.getpixel((i, j)))
                )

                self.total_pixels += 1

    def dominant_color_of_pixel(self, pixel: Tuple[int, int, int, int]) -> str:

        r, g, b = pixel[0], pixel[1], pixel[2]

        if r > g and r > b:
            return "r"

        if g > b and g > r:
            return "g"

        if b > r and b > g:
            return "b"

        return "l"
