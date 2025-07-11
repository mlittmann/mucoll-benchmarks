##Environment Setup:
```
apptainer shell --cleanenv docker://ghcr.io/madbaron/mucoll-sim:master
source source /opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/mucoll-stack-master-fldyu2usa43rdect3x4xyibuzww5ptwz/setup.sh
cd ../newCode
source ../newCode/setupPandora.sh
cd ../k4MuCPlayground
```

##Generation
```
python ../generation/pgun/pgun_lcio.py -p 1 -e 1 --pdg 11 --pt 100 --theta 10 170 -- gen_output.slcio
```

##Simulation
```
ddsim --steeringFile ../simulation/steer_baseline.py --inputFile gen_output.slcio --outputFile sim_output.edm4hep.root --compactFile /path/to/your/geometry/compact/file/of/choice/MAIA_v0.xml
```

##Digitization
```
k4run ../digitization/digi_steer.py --DD4hepXMLFile /path/to/your/geometry/compact/file/of/choice/MAIA_v0.xml
```

##Reconstruction
```
cp -r ../reconstruction/PandoraSettings/ ./
k4run ../reconstruction/reco_steer.py --DD4hepXMLFile /path/to/your/geometry/compact/file/of/choice/MAIA_v0.xml
```

