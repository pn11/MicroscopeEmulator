import numpy as np

class MicroscopeEmulator:
    def __init__(self, depth_image: np.ndarray, view_size: tuple):
        ndim = depth_image.ndim
        if ndim == 3:  
            pass
        elif ndim == 2:
            # 2次元の場合は3次元に変換
            depth_image = depth_image[:,:,np.newaxis]
        else:
            print('depth_image must be ndim=2or3')
            raise ValueError

        # view_size 分の余白のある画像を作成
        sy, sx, sz = depth_image.shape
        vx, vy = view_size
        new_shape = (sy+vy*2, sx+vx*2, sz)
        nsy, nsx, nsz = new_shape
        self.depth_image = np.full(fill_value=255, shape=new_shape, dtype=depth_image.dtype)
        self.depth_image[vy:vy+sy, vx:vx+sx, :] = depth_image

        # デフォルトでは画像の中心にフォーカス
        self.inner_view_point = [nsy//2, nsx//2, nsz//2]
        self.view_size = view_size

    def move_x(self, i: int):
        self._move(i, axis=0)

    def move_y(self, i: int):
        self._move(i, axis=1)

    def move_z(self, i: int):
        self._move(i, axis=2)

    def _move(self, i:int, axis: int):
        p = self.inner_view_point
        p[axis] += i
        p = self._get_original_point(*p)
        self.set_view_point(*p)

    def get_view(self):
        px, py, pz = self.inner_view_point
        vx, vy = self.view_size
        yslice = slice(py-vy//2, py-vy//2+vy)
        xslice = slice(px-vx//2, px-vx//2+vx)
        return self.depth_image[yslice, xslice, pz]

    def get_current_image(self):
        _, _, pz = self.inner_view_point
        vx, vy = self.view_size
        return self.depth_image[vy:-vy, vx:-vx, pz]
    
    def set_view_point(self, x: int, y: int, z: int):
        sy, sx, sz = self.depth_image.shape
        vx, vy = self.view_size
        x, y, z = self._get_inner_point(x, y, z)
        
        # 視野が画像からはみ出さないようにする
        sx, sy, sz = self.depth_image.shape
        low_y = vy
        up_y = sy - vy - 1
        low_x = vx
        up_x = sx - vx - 1
        low_z = 0
        up_z = sz - 1

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
        return x+vx, y+vy, z

    def get_view_mean(self):
        return np.mean(self.get_view())

    def get_image_mean(self):
        return np.mean(self.get_current_image())
    
    def get_darkest_position(self, num_layers: int, num_pixels: int):
        px, py, pz = self.inner_view_point
        sy, sx, sz = self.depth_image.shape        
        minz = max(0, pz-num_layers)
        maxz = min(sz-1, pz+num_layers)
        minx = max(0, px-num_pixels)
        maxx = min(sx-1, px+num_pixels)
        miny = max(0, py-num_pixels)
        maxy = min(sy-1, py+num_pixels)

        val_darkest = 255
        pos_darkests = []
        for z in range(minz,maxz+1):
            val_temp = np.min(self.depth_image[miny:maxy+1, minx:maxx, z])
            if val_temp < val_darkest:
                val_darkest = val_temp

        for z in range(minz,maxz+1): 
            pos_temp = np.argmin(self.depth_image[miny:maxy+1, minx:maxx, z])
            pos_darkests.append(pos_temp)

        min_dist = 9999
        min_pos = None
        pos_viewpoint = np.array([py, px, pz])
        for p in pos_darkests:
            dist_temp = np.linalg.norm(pos_viewpoint-p)
            if dist_temp < min_dist:
                min_dist = dist_temp
                min_pos = [p[1],p[0],p[2]]

        return min_pos
