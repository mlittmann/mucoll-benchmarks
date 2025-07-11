# Install script for directory: /home/sferrar2/Mar2Gau/TrackPerfWorkspace/packages/MuonCVXDDigitiser

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/sferrar2/Mar2Gau/TrackPerfWorkspace/PanInstall")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "0")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

# Set path to fallback-tool for dependency-resolution.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "/usr/bin/objdump")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libMuonCVXDigitiserPlugins.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libMuonCVXDigitiserPlugins.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libMuonCVXDigitiserPlugins.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE MODULE FILES "/home/sferrar2/Mar2Gau/TrackPerfWorkspace/PanBuild/packages/MuonCVXDDigitiser/libMuonCVXDigitiserPlugins.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libMuonCVXDigitiserPlugins.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libMuonCVXDigitiserPlugins.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libMuonCVXDigitiserPlugins.so"
         OLD_RPATH "/home/sferrar2/Mar2Gau/TrackPerfWorkspace/PanBuild/.plugins:/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/root-6.32.08-jsyx2eymz5r2dzthktmtreky4jnsyyf3/lib:/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/dd4hep-1.30-j2jj745at6w5zthjmehpezpusgfkxeiu/lib:/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/k4fwcore-1.2-z6mprl6resh6siyzmlzoplhdulcyplmy/lib:/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/gsl-2.8-w5snzrtm5dmifsgmjycqz6ldj5ofuul6/lib:/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/clhep-2.4.7.1-pi7m3sbrmz5ex4audlodc5vaqc2o4zg7/lib:/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/xerces-c-3.3.0-7udplkbcss57oci6gkpochnq4yatplgw/lib:/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/gaudi-39.2-ychr4p4pzwwdbahztcq7wfjltfaj2wdc/lib:/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/boost-1.87.0-4ehojkamvq7xbkdq5m35bhiyttyyv5jr/lib:/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/intel-tbb-2022.0.0-3lxkblvzkkayyczw44chohcfvry2b6vj/lib:/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/python-3.11.9-nnhlethncovu5syjutsqrxoaq6ipd3af/lib:/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/podio-1.2-quistl6hwrmp2oaqsktfau6no2irlay2/lib:/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/vdt-0.4.4-spajvmfpbzv3yllbrbg7vw26horykqxp/lib:/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/edm4hep-0.99.1-rggcjcxooc5nqgquwx6wdkz2sxnzxyet/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libMuonCVXDigitiserPlugins.so")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE FILE FILES "/home/sferrar2/Mar2Gau/TrackPerfWorkspace/PanBuild/MuonCVXDDigitiser.components")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/python/MuonCVXDDigitiser" TYPE FILE FILES
    "/home/sferrar2/Mar2Gau/TrackPerfWorkspace/PanBuild/packages/MuonCVXDDigitiser/genConfDir/MuonCVXDDigitiser/MuonCVXDigitiserPluginsConf.py"
    "/home/sferrar2/Mar2Gau/TrackPerfWorkspace/PanBuild/packages/MuonCVXDDigitiser/genConfDir/MuonCVXDDigitiser/__init__.py"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE FILE FILES "/home/sferrar2/Mar2Gau/TrackPerfWorkspace/PanBuild/MuonCVXDDigitiser.confdb")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE FILE FILES "/home/sferrar2/Mar2Gau/TrackPerfWorkspace/PanBuild/MuonCVXDDigitiser.confdb2")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "shlib" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libMuonCVXDigitiserPlugins.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libMuonCVXDigitiserPlugins.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libMuonCVXDigitiserPlugins.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE MODULE FILES "/home/sferrar2/Mar2Gau/TrackPerfWorkspace/PanBuild/packages/MuonCVXDDigitiser/libMuonCVXDigitiserPlugins.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libMuonCVXDigitiserPlugins.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libMuonCVXDigitiserPlugins.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libMuonCVXDigitiserPlugins.so"
         OLD_RPATH "/home/sferrar2/Mar2Gau/TrackPerfWorkspace/PanBuild/.plugins:/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/root-6.32.08-jsyx2eymz5r2dzthktmtreky4jnsyyf3/lib:/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/dd4hep-1.30-j2jj745at6w5zthjmehpezpusgfkxeiu/lib:/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/k4fwcore-1.2-z6mprl6resh6siyzmlzoplhdulcyplmy/lib:/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/gsl-2.8-w5snzrtm5dmifsgmjycqz6ldj5ofuul6/lib:/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/clhep-2.4.7.1-pi7m3sbrmz5ex4audlodc5vaqc2o4zg7/lib:/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/xerces-c-3.3.0-7udplkbcss57oci6gkpochnq4yatplgw/lib:/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/gaudi-39.2-ychr4p4pzwwdbahztcq7wfjltfaj2wdc/lib:/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/boost-1.87.0-4ehojkamvq7xbkdq5m35bhiyttyyv5jr/lib:/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/intel-tbb-2022.0.0-3lxkblvzkkayyczw44chohcfvry2b6vj/lib:/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/python-3.11.9-nnhlethncovu5syjutsqrxoaq6ipd3af/lib:/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/podio-1.2-quistl6hwrmp2oaqsktfau6no2irlay2/lib:/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/vdt-0.4.4-spajvmfpbzv3yllbrbg7vw26horykqxp/lib:/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/edm4hep-0.99.1-rggcjcxooc5nqgquwx6wdkz2sxnzxyet/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libMuonCVXDigitiserPlugins.so")
    endif()
  endif()
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
if(CMAKE_INSTALL_LOCAL_ONLY)
  file(WRITE "/home/sferrar2/Mar2Gau/TrackPerfWorkspace/PanBuild/packages/MuonCVXDDigitiser/install_local_manifest.txt"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
endif()
