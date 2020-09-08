# import numpy as np
from pyvox.models import Vox
from pyvox.writer import VoxWriter
import binvox_rw
# def showVoxel(voxel):
#     fig = plt.figure()
#     ax = fig.gca(projection='3d')
 
#     ax.voxels(voxel, edgecolor="k")
#     plt.show()
 
 
# # ma = np.random.choice([0,1], size=(10,10,10), p=[0.95, 0.05])#意思是在10*10*10的空间中以一定的概率选择一部分点为1
f=open("scene0001_00_scanned.binvox", "rb")
ma = binvox_rw.read_as_3d_array(f)
data = ma.data

# data = data[:, ::-1, :]#y
# data = data[::-1, :, :]#x

print("data.shape:",data.shape)
vox = Vox.from_dense(data)
# print(vox)
# print(len(vox))
print("")

VoxWriter('test.vox', vox).write()

f.close()
# showVoxel(ma.data)
#然后再利用magicaVoxel或者线上方式转成OBJ文件。