'''-------------------------------------------------------------'''
''' Reconstruction Steering File for the Muon Collider Detector '''
'''-------------------------------------------------------------'''
from GaudiKernel.Constants import INFO, WARNING, DEBUG
# Collect Arguements
from components.reco_args import get_reco_args
args = get_reco_args()

# Set Up Services
from components.reco_services import set_reco_services
[evtsvc, geoservice] = set_reco_services(args)

# Import the Algorithm List
from recoAlgList import makeRecoAlgList
algList = makeRecoAlgList(args)

'''-------------------------------------------------------------'''
'''    Run the Digitization Algorithms in the ApplicationMgr    '''
'''-------------------------------------------------------------'''
# Declare Input and Output for the IOSvc
from k4FWCore import IOSvc, ApplicationMgr
svc = IOSvc(
    "IOSvc",
    Input = ["digi_output.edm4hep.root"], # Input file from digitization
    Output = "reco_output.edm4hep.root" # Output file for reconstruction
)

# Run the Application Manager
ApplicationMgr(
    TopAlg = algList,
    EvtSel = 'NONE',
    EvtMax   = 10,
    ExtSvc = [evtsvc, geoservice],
    OutputLevel=INFO
)