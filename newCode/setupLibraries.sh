buildDir="${PWD}/install"

export PATH=${buildDir}/bin:$PATH
export LD_LIBRARY_PATH=${buildDir}/lib:${buildDir}/lib64:$LD_LIBRARY_PATH
export ROOT_INCLUDE_PATH=${buildDir}/include:$ROOT_INCLUDE_PATH
export PYTHONPATH=${buildDir}/python:$PYTHONPATH
cd ..
export PYTHONPATH=${PWD}/digitization:$PYTHONPATH
export PYTHONPATH=${PWD}/reconstruction:$PYTHONPATH
export CMAKE_PREFIX_PATH=${buildDir}:$CMAKE_PREFIX_PATH
cd k4MuCPlayground


export LD_LIBRARY_PATH=/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/acts-32.1.0-yacvft6qr5l5ra67k7ss4mnvfbju6qza/lib:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/vdt-0.4.4-243z3wcxk4gkd7j2jlxcrdfa27bq46az/lib/:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/xerces-c-3.3.0-7udplkbcss57oci6gkpochnq4yatplgw/lib/:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/gsl-2.8-w5snzrtm5dmifsgmjycqz6ldj5ofuul6/lib/:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/clhep-2.4.7.1-pi7m3sbrmz5ex4audlodc5vaqc2o4zg7/lib/:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/pandorasdk-3.4.2-33sx55dznpsqceud6wlroqaru7v4cpqo/lib:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/marlintrk-2.9.2-kibtsh7cumdyybrpvzliguwbtubqul6t/lib:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/lccontent-3.1.6-ixnoiwljthdbi7abfwfptolewzacdleb/lib:$LD_LIBRARY_PATH
