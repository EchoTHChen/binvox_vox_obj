修复了py-vox-io的镜像bug

1.cd py-vox-io-master
2.安装pyvox:python setup.py install

3.将.binvox转成.vox文件：cd ../ ,执行 python generate1.py（修改相应的文件名即可）

4.最后利用magicaVoxel或者线上方式转成OBJ文件。
（magicaVoxel:http://ephtracy.github.io/, download 0.99.6, 打开.vox文件, export .obj文件即可）

Reference:
binvox/viewvox
py-vox-io:https://github.com/gromgull/py-vox-io
magicaVoxel:http://ephtracy.github.io/, 0.99.6
