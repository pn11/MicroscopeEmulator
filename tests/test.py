import numpy as np
from microscope_emulator import MicroscopeEmulator

img = np.zeros((100, 100, 100), dtype=np.uint8)
ms = MicroscopeEmulator(img, (10, 10))

for i in range(100):
    ms.move_x(1)
    print(ms.get_view())

