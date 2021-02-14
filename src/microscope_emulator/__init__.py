import numpy as np

class MicroscopeEmulator:
    def __init__(self, depth_image: np.ndarray, view_size: tuple):
        self.depth_image = depth_image
        self.view_size = view_size
        self.view_point = [None]*3
        self.set_view_point(0, 0, 0)

    def move_x(self, i: int):
        self._move(i, axis=1)

    def move_y(self, i: int):
        self._move(i, axis=0)

    def move_z(self, i: int):
        self._move(i, axis=2)

    def _move(self, i:int, axis: int):
        shape = self.depth_image.shape
        org_val = self.view_point[axis]
        self.view_point[axis] = min(max(org_val+i, 0), shape[axis])
            
    def get_view(self):
        py, px, pz = self.view_point
        vy, vx = self.view_size
        yslice = slice(py-vy//2, py-vy//2+vy)
        xslice = slice(px-vx//2, px-vx//2+vx)
        return self.depth_image[yslice, xslice, pz]
    
    def set_view_point(self, x: int, y: int, z: int):
        sy, sx, sz = self.depth_image.shape
        vx, vy = self.view_size
        
        # 視野が画像からはみ出さないようにする
        self.view_point[1] = min(max(x, vx//2), sx+vx//2-vx)
        self.view_point[0] = min(max(y, vy//2), sy+vy//2-vy)
        self.view_point[2] = min(max(z, 0), sz)
