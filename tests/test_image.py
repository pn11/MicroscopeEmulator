import numpy as np
from PIL import Image, ImageFilter

from microscope_emulator import MicroscopeEmulator

def test_create_image():
    img = np.random.randint(0, 256, (500, 500, 100))
    img = img.astype(np.uint8)
    ms = MicroscopeEmulator(img, (100, 100))
    im1 = Image.fromarray(ms.depth_image[:, :, 50])
    im1.save('test1.png')
    im2 = Image.fromarray(ms.get_view())
    im2.save('test2.png')
