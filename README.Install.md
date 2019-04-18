# Deep Mimic Installation Guide with Linux


Project page: [https://xbpeng.github.io/projects/DeepMimic/index.html](https://xbpeng.github.io/projects/DeepMimic/index.html) 

Repo: [https://github.com/bsivanantham/DeepMimic](https://github.com/bsivanantham/DeepMimic) 

Note : It is better to use conda venv and python3.6. (Not compulsory)

## Bullet 2.87

[ https://github.com/bulletphysics/bullet3/archive/2.87.tar.gz]( https://github.com/bulletphysics/bullet3/archive/2.87.tar.gz)

Make sure cmake is installed (sudo apt-get install cmake, brew install cmake)

In a terminal type:

```
./build_cmake_pybullet_double.sh
cd build3
make install or try sudo make install
```
Note: When building Bullet, be sure to disable double precision with the build flag ```USE_DOUBLE_PRECISION=OFF```. and while executing a script if you have an error like pybullet.so already exist use 
```ln -f -s pybullet.so.2.87 pybullet.so``` instead of ```ln -f -s pybullet.dylib pybullet.so```

or
```
cd build3
	./premake4_linux --double gmake
	./premake4_linux64 --double gmake
	./premake4_osx --double --enable_pybullet gmake

cd gmake
make
```
Ignore if there is a shared memory error. Check if
```/usr/include``` or ```/usr/local/include``` has bullet file.

If the file is not available manually run ```gcc -I ``` and missing files names like ```-lGLEW -lGL -lGLU -lglut -lBulletDynamics -lBulletCollision -lLinearMath -lm -lstdc++``` to ```/usr/include```

## Eigen

[ https://github.com/eigenteam/eigen-git-mirror.git]( https://github.com/eigenteam/eigen-git-mirror.git)

Before starting, create another directory which we will call 'build_dir'.

```
mkdir build_dir
cd build_dir
cmake ..
make install 
```
The "make install" step may require administrator privileges
or else use "sudo".

## OpenGL

```
sudo apt-get update
sudo apt-get install libglu1-mesa-dev freeglut3-dev mesa-common-dev 
```
## Freeglut

Link to download : [freeglut]( https://downloads.sourceforge.net/project/freeglut/freeglut/3.0.0/freeglut-3.0.0.tar.gz?r=https%3A%2F%2Fsourceforge.net%2Fprojects%2Ffreeglut%2Ffiles%2Ffreeglut%2F3.0.0%2Ffreeglut-3.0.0.tar.gz%2Fdownload%3Fuse_mirror%3Ddatapacket%26download%3D&ts=1550193133)

Make sure you have the basics for compiling code, such as C compiler (e.g., GCC) and the make package.

```
cmake .
make
make install 
```
The "make install" step may require administrator privileges or else use "sudo".

## Glew

[https://github.com/nigels-com/glew.git]( https://github.com/nigels-com/glew.git)

Make sure you have the basics for compiling code, such as C compiler (e.g., GCC) and the make package.

Build
```
sudo apt-get install build-essential libxmu-dev libxi-dev libgl-dev
make
sudo make install
make clean
```
or using cmake
```
sudo apt-get install build-essential libxmu-dev libxi-dev libgl-dev cmake git
cd build
cmake ./cmake
make -j4
```

## Other Dependencies

Python:
- Python 3
- PyOpenGL (http://pyopengl.sourceforge.net/)
```
pip install PyOpenGL PyOpenGL_accelerate
```

- Tensorflow (https://www.tensorflow.org/)
     
Current release for CPU-only

``` pip install tensorflow ```

GPU package for CUDA-enabled GPU cards

``` pip install tensorflow-gpu ```

- MPI4Py (https://mpi4py.readthedocs.io/en/stable/install.html)

``` [sudo] pip install mpi4py```

Misc:
- SWIG (http://www.swig.org/)
- MPI 
 `sudo apt install libopenmpi-dev`
 
 # Deep Mimic Configuration and Execution

If everything is successfully installed as stated above and Mainly Bullet installed and checked the linking in `usr/include`.

Then
```
pip install -r requirements.txt
```

1. Modify the `Makefile` in `DeepMimicCore/` by specifying the following,
	- `EIGEN_DIR`: Eigen include directory
	- `BULLET_INC_DIR`: Bullet source directory
	- `PYTHON_INC`: python include directory
	- `PYTHON_LIB`: python lib directory

2. Build wrapper,
	```
	make python
	```
This should generate `DeepMimicCore.py` in `DeepMimicCore/`
but with some warning.

# How to Use
Follow the Repo: [https://github.com/bsivanantham/DeepMimic](https://github.com/bsivanantham/DeepMimic)
README.md
