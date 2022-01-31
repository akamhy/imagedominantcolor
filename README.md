<div align="center">
<h1> ImageDominantColor </h1>
<h3>Get the dominant color of any image</h3>
</div>

<p align="center">
<a href="https://github.com/akamhy/imagedominantcolor/actions?query=workflow%3ATest"><img alt="Build Status" src="https://github.com/akamhy/imagedominantcolor/workflows/Test/badge.svg"></a>
<a href="https://codecov.io/gh/akamhy/imagedominantcolor"><img alt="codecov" src="https://codecov.io/gh/akamhy/imagedominantcolor/branch/main/graph/badge.svg?token=xCV7vQ9MJo"></a>
<a href="https://pypi.org/project/imagedominantcolor/"><img alt="pypi" src="https://img.shields.io/pypi/v/imagedominantcolor.svg"></a>
<a href="https://pepy.tech/project/imagedominantcolor?versions=1*"><img alt="Downloads" src="https://pepy.tech/badge/imagedominantcolor/month"></a>
<a href="https://github.com/akamhy/imagedominantcolor/commits/master"><img alt="GitHub lastest commit" src="https://img.shields.io/github/last-commit/akamhy/imagedominantcolor?color=blue&style=flat-square"></a>
<a href="#"><img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/imagedominantcolor?style=flat-square"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>


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
  - `l` - It is lowercase L and it means the image is a grayscale image. L is short for luminance. Most of the image lacks color and luminance is the dominant color.


### License
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/akamhy/imagedominantcolor/blob/main/LICENSE)

Copyright (c) 2022 Akash Mahanty.

Released under the MIT License. See
[license](https://github.com/akamhy/imagedominantcolor/blob/main/LICENSE) for details.
