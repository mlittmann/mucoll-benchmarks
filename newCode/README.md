# Building the Library

Follow these steps to properly build the library:

## Build Instructions

1. Make sure you are in the container:
```
apptainer shell --cleanenv docker://ghcr.io/madbaron/mucoll-sim:master
source source /opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/mucoll-stack-master-fldyu2usa43rdect3x4xyibuzww5ptwz/setup.sh
```

2. Make needed directories:
```
mkdir build install
cd build
```

3. Find Dependancies:
```
cmake .. -DCMAKE_INSTALL_PREFIX=../install
```

4. Build Libraries:
```
cmake --build . -j $(nproc) -t install
```

5. Add to path:
```
cd ..
source setupLibraries.sh
```