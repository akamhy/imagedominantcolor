<div align="center">
<img src="https://raw.githubusercontent.com/akamhy/imagedominantcolor/main/assets/image_dominant_color_logo.svg" width="300"><br>
<h3>Get the dominant color of any image</h3>
</div>

<p align="center">
<a href="https://github.com/akamhy/imagedominantcolor/actions?query=workflow%3ATest"><img alt="Build Status" src="https://github.com/akamhy/imagedominantcolor/workflows/Test/badge.svg"></a>
<a href="https://codecov.io/gh/akamhy/imagedominantcolor"><img alt="codecov" src="https://codecov.io/gh/akamhy/imagedominantcolor/branch/main/graph/badge.svg?token=xCV7vQ9MJo"></a>
<a href="https://pypi.org/project/imagedominantcolor/"><img alt="pypi" src="https://img.shields.io/pypi/v/imagedominantcolor.svg"></a>
<a href="https://pepy.tech/project/imagedominantcolor?versions=1*"><img alt="Downloads" src="https://pepy.tech/badge/imagedominantcolor/month"></a>
<a href="#"><img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/imagedominantcolor?style=flat-square"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

### Introduction
ImageDominantColor is a Python package/library for **detecting dominant color of images**.

It can take any input image and tell the dominant color of the image. It doesn't use k-means clustering for detecting dominant color but instead quantizes the individual pixels and calculates the statistical mode of the quantized values.

ImageDominantColor does not depend on numpy unlike most of the other implementations for the same task and is also fast and minimalist.


What ImageDominantColor is not?
> ImageDominantColor does not calculates the average color of the image. Also note that the average color of an image is not same as its dominant color.


### Installation

  - Using [pip](https://en.wikipedia.org/wiki/Pip_(package_manager)):

```bash
pip install imagedominantcolor -U
```

  - Install directly from GitHub:

```bash
pip install git+https://github.com/akamhy/imagedominantcolor.git
```


### Usage
```python
>>> from imagedominantcolor import DominantColor
>>> file_path = "blue_butterfly.jpg" # Blue color is dominant
>>> dominantcolor = DominantColor(file_path)
>>> dominantcolor.dominant_color
'b'
>>> dominantcolor.rgb
(3, 6, 244)
>>> dir(dominantcolor)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'b', 'counter', 'dominant_color', 'dominant_color_of_pixel', 'dominant_color_of_pixels_of_image_array', 'g', 'generate_dominant_color_of_pixels_of_image_array', 'image', 'image_data', 'image_path', 'l', 'minimum_percent_difference_of_rgb', 'mpd', 'r', 'resize_value', 'resized_image', 'rgb', 'rgbl', 'set_dominat_color_of_image', 'set_rgbl_value_of_image', 'total_pixels']
>>> dominantcolor.total_pixels
256
>>> dominantcolor.r
3
>>> dominantcolor.g
6
>>> dominantcolor.b
244
>>> dominantcolor.l
3
>>> dominantcolor.rgbl
(3, 6, 244, 3)
>>> repr(dominantcolor)
'DominantColor(r:3 g:6 b:244 l:3; dominant_color:b; resize_value:16; minimum_percent_difference_of_rgb:10)'
>>> str(dominantcolor)
'b'
>>>
```

Output dominant color and what their meanings are:

  - `r` - Red is the dominant color in the image.
  - `g` - Green is the dominant color for the image.
  - `b` - Blue is the dominant color.
  - `l` - It is lowercase L and it implies that the image is a mostly a grayscale image. L for luminance and most of the image lacks color.
  - `n` - None of the color out of r, g and b are dominant but the image is not grayscale. It implies that the image has equal regions where 2 or 3 colors dominate, [example here](https://user-images.githubusercontent.com/64683866/151845374-dd1a83e5-3265-491e-830d-39be120af65b.png). You can check the rgb attribute to decide what to do with such cases.

What are `r`, `g`, `b` and `l` attributes of `DominantColor` objects?
> The library shrinks the image before checking the dominant color and the default resize value is 256. Thus every image is shrunk to a 256 pixels image.
The r,g,b and l attributes indicate the number of pixels which have r,g,b and l as dominating value.

### License
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/akamhy/imagedominantcolor/blob/main/LICENSE)

Copyright (c) 2022 Akash Mahanty.

Released under the MIT License. See
[license](https://github.com/akamhy/imagedominantcolor/blob/main/LICENSE) for details.
