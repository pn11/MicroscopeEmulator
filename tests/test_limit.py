import numpy as np
from microscope_emulator import MicroscopeEmulator

img = np.zeros((100, 100, 100), dtype=np.uint8)
ms = MicroscopeEmulator(img, (10, 10))

def test_limit_x():
    for i in range(1000):
        ms.move_x(1)
        print(ms.get_view())
    for i in range(1000):
        ms.move_x(-1)
        print(ms.get_view())

def test_limit_y():
    for i in range(1000):
        ms.move_y(1)
        print(ms.get_view())
    for i in range(1000):
        ms.move_y(-1)
        print(ms.get_view())

def test_limit_z():
    for i in range(1000):
        ms.move_x(1)
        print(ms.get_view())
    for i in range(1000):
        ms.move_x(-1)
        print(ms.get_view())
