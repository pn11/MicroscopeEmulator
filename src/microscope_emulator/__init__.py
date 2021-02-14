import numpy as np

class MicroscopeEmulator:
    def __init__(self, depth_image: np.ndarray, view_size: tuple):
        # view_size 分の余白のある画像を作成
        sy, sx, sz = depth_image.shape
        vx, vy = view_size
        new_shape = (sy+vy*2, sx+vx*2, sz)
        nsx, nsy, nsz = new_shape
        self.depth_image = np.full(fill_value=255, shape=new_shape, dtype=depth_image.dtype)
        self.depth_image[vy:vy+sy, vx:vx+sx , :] = depth_image
        # デフォルトでは画像の中心にフォーカス
        self.inner_view_point = [nsy//2, nsx//2, nsz//2]
        self.view_size = view_size

    def move_x(self, i: int):
        self._move(i, axis=1)

    def move_y(self, i: int):
        self._move(i, axis=0)

    def move_z(self, i: int):
        self._move(i, axis=2)

    def _move(self, i:int, axis: int):
        p = self.inner_view_point
        p[axis] += i
        self.set_view_point(*p)

    def get_view(self):
        py, px, pz = self.inner_view_point
        vy, vx = self.view_size
        yslice = slice(py-vy//2, py-vy//2+vy)
        xslice = slice(px-vx//2, px-vx//2+vx)
        return self.depth_image[yslice, xslice, pz]
    
    def set_view_point(self, x: int, y: int, z: int):
        sy, sx, sz = self.depth_image.shape
        vx, vy = self.view_size
        x, y, z = self._get_inner_point(x, y, z)
        
        # 視野が画像からはみ出さないようにする
        sx, sy, sz = self.depth_image.shape
        low_y = sy + vy
        up_y = sy - vy - 1
        low_x = sx + vx
        up_x = sx - vx - 1
        low_z = 0
        up_z = sz- 1

        self.inner_view_point = [
            min(max(x, low_x), up_x),
            min(max(y, low_y), up_y),
            min(max(z, low_z), up_z)
        ] 

    def get_view_point(self):
        return self._get_original_point(*self.inner_view_point)

    def get_pixel_value(self, x=None, y=None, z=None):
        if x is None:
            x, y, z = self._get_original_point(*self.inner_view_point)
            return self.get_pixel_value(x, y, z)
        else:
            x, y, z = self._get_inner_point(x, y, z)
            return self.depth_image[y, x, z]

    def _get_original_point(self, x, y, z):
        # 余白追加前の座標を返す
        vx, vy = self.view_size
        return x-vx, y-vy, z

    def _get_inner_point(self, x, y, z):
        vx, vy = self.view_size
        return x-+vx, y+vy, z
