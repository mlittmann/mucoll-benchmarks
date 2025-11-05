##Environment Setup:
With the new image everything will work out-of-the-box. The path to the setup script might change in different 
versions so use tab-complete to fill in the ellipses:
```
apptainer shell --cleanenv docker://ghcr.io/muoncollidersoft/mucoll-sim-alma9:full_gaudi_test 
source source /opt/spack/opt/spack/.../linux-almalinux9-x86_64/mucoll-stack-.../setup.sh
cd /path/to/k4MuCPlayground
source setup_digireco.sh
```

##Set Environment Variables
The Simulation, Digitization, and Reconstruction steps all use environment variables for the geometry.
`MUCOLL_GEO` (Sim, Digi, Reco)
`MUCOLL_MATMAP`, `MUCOLL_TGEO`, `MUCOLL_TGEO_DESC` (Reco)
Before getting started. Make sure to set these to where you want them to point like this:
`export MUCOLL_GEO=/opt/spack/opt/spack/.../k4geo-main.../share/k4geo/MuColl/MAIA/compact/MAIA_v0/MAIA_v0.xml`

All of the Geometry Files (MuColl_v1, MuSIC, MAIA) live in the `k4geo` directory (`.../share/k4geo/MuColl/`). 
All of the Tracking geometries live in the `k4actstracking` directory (`.../share/k4ActsTracking/data/`).

##Generation
```
python ../generation/pgun/pgun_edm4hep.py \
-p 1 -e 1 --pdg 11 --pt 100 --theta 10 170 -- gen_output.edm4hep.root
```

##Simulation
```
ddsim --steeringFile ../simulation/steer_baseline.py --numberOfEvents 1
```

##Digitization
```
k4run ../digitization/digi_steer.py 
```

##Reconstruction
```
cp -r ../reconstruction/PandoraSettings/ ./
k4run ../reconstruction/reco_steer.py
```

##Input/Output
You can change the input/output files for sim with:
```
--inputFiles INPUT_FILE_NAME.edm4hep.root --outputFile OUTPUT_FILE_NAME.edm4hep.root
```
You can change the input/output files for digi/reco with: 
```
--IOSvc.Input INPUT_FILE_NAME.edm4hep.root --IOSvc.Output OUTPUT_FILE_NAME.edm4hep.root
```

##Debugging
If an issue is coming up with the steering files, the first thing to try to do is delete the __pycache__.py directory in the `/digitization/components/` and `/reconstruction/components/` directory. Then run
```
touch digitization/components/__init__.py
touch reconstruction/components/__init__.py
```
before trying to re-run your steering file.
