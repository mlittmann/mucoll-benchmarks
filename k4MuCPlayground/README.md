##Environment Setup:
With the new image everything will work out-of-the-box. The path to the setup script might change in different versions so use tab-complete to fill in the ellipses:
```
apptainer shell --cleanenv docker://ghcr.io/muoncollidersoft/mucoll-sim-alma9:full_gaudi_test 
source source /opt/spack/opt/spack/.../linux-almalinux9-x86_64/mucoll-stack-.../setup.sh
cd /path/to/k4MuCPlayground
source setup_digireco.sh
```



##Generation
```
python ../generation/pgun/pgun_edm4hep.py -p 1 -e 1 --pdg 11 --pt 100 --theta 10 170 -- gen_output.edm4hep.root
```

##Simulation
```
ddsim --steeringFile ../simulation/steer_baseline.py --inputFile gen_output.edm4hep.root --outputFile sim_output.edm4hep.root --compactFile /path/to/your/geometry/compact/file/of/choice/MAIA_v0.xml
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
