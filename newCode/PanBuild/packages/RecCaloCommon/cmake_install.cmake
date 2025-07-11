# Install script for directory: /home/sferrar2/Mar2Gau/TrackPerfWorkspace/packages/RecCaloCommon

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
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libRecCaloCommon.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libRecCaloCommon.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libRecCaloCommon.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/sferrar2/Mar2Gau/TrackPerfWorkspace/PanBuild/packages/RecCaloCommon/libRecCaloCommon.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libRecCaloCommon.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libRecCaloCommon.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libRecCaloCommon.so"
         OLD_RPATH "/home/sferrar2/Mar2Gau/TrackPerfWorkspace/PanBuild/.plugins:/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/fastjet-3.4.2-qagz5jf2js2byqmpsldsnsysogebjwnt/lib/libfastjet.so:/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/gaudi-39.2-ychr4p4pzwwdbahztcq7wfjltfaj2wdc/lib:/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/edm4hep-0.99.1-rggcjcxooc5nqgquwx6wdkz2sxnzxyet/lib:/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/fastjet-3.4.2-qagz5jf2js2byqmpsldsnsysogebjwnt/lib:/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/boost-1.87.0-4ehojkamvq7xbkdq5m35bhiyttyyv5jr/lib:/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/intel-tbb-2022.0.0-3lxkblvzkkayyczw44chohcfvry2b6vj/lib:/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/root-6.32.08-jsyx2eymz5r2dzthktmtreky4jnsyyf3/lib:/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/python-3.11.9-nnhlethncovu5syjutsqrxoaq6ipd3af/lib:/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/podio-1.2-quistl6hwrmp2oaqsktfau6no2irlay2/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libRecCaloCommon.so")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/sferrar2/Mar2Gau/TrackPerfWorkspace/packages/RecCaloCommon/include/")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "dev" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libRecCaloCommon.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libRecCaloCommon.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libRecCaloCommon.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/sferrar2/Mar2Gau/TrackPerfWorkspace/PanBuild/packages/RecCaloCommon/libRecCaloCommon.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libRecCaloCommon.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libRecCaloCommon.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libRecCaloCommon.so"
         OLD_RPATH "/home/sferrar2/Mar2Gau/TrackPerfWorkspace/PanBuild/.plugins:/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/fastjet-3.4.2-qagz5jf2js2byqmpsldsnsysogebjwnt/lib/libfastjet.so:/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/gaudi-39.2-ychr4p4pzwwdbahztcq7wfjltfaj2wdc/lib:/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/edm4hep-0.99.1-rggcjcxooc5nqgquwx6wdkz2sxnzxyet/lib:/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/fastjet-3.4.2-qagz5jf2js2byqmpsldsnsysogebjwnt/lib:/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/boost-1.87.0-4ehojkamvq7xbkdq5m35bhiyttyyv5jr/lib:/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/intel-tbb-2022.0.0-3lxkblvzkkayyczw44chohcfvry2b6vj/lib:/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/root-6.32.08-jsyx2eymz5r2dzthktmtreky4jnsyyf3/lib:/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/python-3.11.9-nnhlethncovu5syjutsqrxoaq6ipd3af/lib:/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/podio-1.2-quistl6hwrmp2oaqsktfau6no2irlay2/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libRecCaloCommon.so")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "dev" OR NOT CMAKE_INSTALL_COMPONENT)
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
if(CMAKE_INSTALL_LOCAL_ONLY)
  file(WRITE "/home/sferrar2/Mar2Gau/TrackPerfWorkspace/PanBuild/packages/RecCaloCommon/install_local_manifest.txt"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
endif()
