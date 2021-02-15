import numpy as np
from PIL import Image, ImageFilter

from microscope_emulator import MicroscopeEmulator

def test_api():
    img = np.random.randint(0, 256, (500, 500, 100))
    ms = MicroscopeEmulator(img, (100, 100))
    x, y, z = ms.get_view_point()
    assert x == 250
    assert y == 250
    assert z == 50
    ms.move_x(1)
    ms.move_y(-1)
    ms.move_z(100000)
    x, y, z = ms.get_view_point()
    assert x == 251
    assert y == 249
    assert z == 99
    print(ms.get_view())
    ms.set_view_point(100, 101, 99)
    x, y, z = ms.get_view_point()
    assert x == 100
    assert y == 101
    assert z == 99
    a = ms.get_pixel_value()
    b = ms.get_pixel_value(*ms.get_view_point())
    assert a == b
