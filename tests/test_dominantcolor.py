import pytest
import os
import urllib.request
from imagedominantcolor.dominantcolor import DominantColor


this_dir = os.path.dirname(os.path.realpath(__file__))


def test_all():

    orange_fruit_url = "https://user-images.githubusercontent.com/64683866/151797629-ce73377f-9a6a-433c-a518-90bb848bf277.png"
    orange_fruit_file_path = os.path.join(this_dir, "orange_fruit.jpeg")
    urllib.request.urlretrieve(orange_fruit_url, orange_fruit_file_path)
    dominantcolor = DominantColor(orange_fruit_file_path)
    os.remove(orange_fruit_file_path)
    assert dominantcolor.dominant_color == "r"
    assert str(dominantcolor) == "r"
    assert dominantcolor.rgb == (256, 0, 0)
    assert dominantcolor.rgbl == (256, 0, 0, 0)
    assert dominantcolor.r == 256
    assert dominantcolor.g == 0
    assert dominantcolor.b == 0
    assert dominantcolor.l == 0
    assert dominantcolor.mpd == 25
    assert dominantcolor.total_pixels == 256
    assert dominantcolor.resize_value == 16
    assert dominantcolor.minimum_percent_difference_of_rgb == 10
    assert DominantColor.resize_value == 16
    assert DominantColor.minimum_percent_difference_of_rgb == 10
    assert (
        repr(dominantcolor)
        == "DominantColor(r:256 g:0 b:0 l:0; dominant_color:r; resize_value:16; minimum_percent_difference_of_rgb:10)"
    )

    green_new_delhi_url = "https://user-images.githubusercontent.com/64683866/151797941-509e0c96-d706-43b5-b849-812a7818dff8.png"
    green_new_delhi_file_path = os.path.join(this_dir, "green_new_delhi.jpeg")
    urllib.request.urlretrieve(green_new_delhi_url, green_new_delhi_file_path)
    dominantcolor = DominantColor(green_new_delhi_file_path)
    os.remove(green_new_delhi_file_path)
    assert dominantcolor.dominant_color == "g"

    blue_jelly_fish_url = "https://user-images.githubusercontent.com/64683866/151797390-ed38cb0d-d917-4b19-9ff2-2438ab6193f4.png"
    blue_jelly_fish_file_path = os.path.join(this_dir, "blue_jelly_fish.jpeg")
    urllib.request.urlretrieve(blue_jelly_fish_url, blue_jelly_fish_file_path)
    dominantcolor = DominantColor(blue_jelly_fish_file_path)
    os.remove(blue_jelly_fish_file_path)
    assert dominantcolor.dominant_color == "b"

    # GitHub converts the pixel to RGB tuple from int, but wayback machine does not.
    grey_apple_url = "https://web.archive.org/web/20220131133631if_/https://media.geeksforgeeks.org/wp-content/uploads/gray.jpeg"
    grey_apple_file_path = os.path.join(this_dir, "grey_apple.jpeg")
    urllib.request.urlretrieve(grey_apple_url, grey_apple_file_path)
    dominantcolor = DominantColor(grey_apple_file_path)
    os.remove(grey_apple_file_path)
    assert dominantcolor.dominant_color == "l"

    rgb_strip_url = "https://user-images.githubusercontent.com/64683866/151845374-dd1a83e5-3265-491e-830d-39be120af65b.png"
    rgb_strip_file_path = os.path.join(this_dir, "rgb_strip.jpeg")
    urllib.request.urlretrieve(rgb_strip_url, rgb_strip_file_path)
    dominantcolor = DominantColor(rgb_strip_file_path)
    os.remove(rgb_strip_file_path)
    assert dominantcolor.dominant_color == "n"
