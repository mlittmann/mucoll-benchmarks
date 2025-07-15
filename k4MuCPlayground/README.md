##Environment Setup:
If libraries have been previously built:
```
apptainer shell --cleanenv docker://ghcr.io/madbaron/mucoll-sim:master
source source /opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/mucoll-stack-master-fldyu2usa43rdect3x4xyibuzww5ptwz/setup.sh
cd /path/to/k4MuCWorkspace
source ./setupLibraries.sh
cd /path/to/k4MuCPlayground
source setup_digireco.sh
```

Otherwise, first clone [k4MuCWorkspace](https://github.com/samf25/k4MuCWorkspace) and follow the instructions in the `README.md` to build the new libraries.

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

##Debugging
If an issue is coming up with the steering files, the first thing to try to do is delete the __pycache__.py directory in the `/digitization/components/` and `/reconstruction/components/` directory. Then run
```
touch digitization/components/__init__.py
touch reconstruction/components/__init__.py
```
before trying to re-run your steering file.
