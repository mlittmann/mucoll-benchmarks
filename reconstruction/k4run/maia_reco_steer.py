from Configurables import ApplicationMgr
from Gaudi.Configuration import *

from Configurables import LcioEvent, EventDataSvc, MarlinProcessorWrapper
from k4MarlinWrapper.parseConstants import *

import os

from k4FWCore.parseArgs import parser

parser.add_argument("--enableIP", action="store_true", default=False, help="Enable IP overlay")

parser.add_argument(
    "--OverlayFullNumberBackground",
    help="Number of background files used for BIB overlay",
    type=str,
    default="192", 
)
parser.add_argument(
    "--outputFile",
    help="output directory and file",
    type=str,
    default="output_reco.slcio",
)
parser.add_argument(
    "--OverlayFullPathToMuPlus",
    help="Path to files for muplus BIB overlay",
    type=str,
    default="/path/to/muplus/",
)
parser.add_argument(
    "--OverlayFullPathToMuMinus",
    help="Path to files for muminus BIB overlay",
    type=str,
    default="/path/to/muminus/",
)
parser.add_argument(
    "--inputFile",
    help="Input LCIO file",
    type=str,
    required=True,
)

the_args = parser.parse_args()

algList = []
evtsvc = EventDataSvc()

CONSTANTS = {
}

parseConstants(CONSTANTS)

read = LcioEvent()
read.OutputLevel = INFO
read.Files = [the_args.inputFile]
algList.append(read)

EventNumber = MarlinProcessorWrapper("EventNumber")
EventNumber.OutputLevel = INFO
EventNumber.ProcessorType = "Statusmonitor"
EventNumber.Parameters = {
    "HowOften": ["1"]
}

MyAIDAProcessor = MarlinProcessorWrapper("MyAIDAProcessor")
MyAIDAProcessor.OutputLevel = INFO
MyAIDAProcessor.ProcessorType = "AIDAProcessor"
MyAIDAProcessor.Parameters = {
    "FileName": ["output_reco"],
    "FileType": ["root"]
}

Output_REC = MarlinProcessorWrapper("Output_REC")
Output_REC.OutputLevel = INFO
Output_REC.ProcessorType = "LCIOOutputProcessor"
Output_REC.Parameters = {
        "DropCollectionTypes": ["SimCalorimeterHit", "CalorimeterHit"],
        "DropCollectionNames": ["IBTrackerHits", "IETrackerHits", "IETrackerHitsRelations", "IBTrackerHitsRelations",
                                "OBTrackerHits", "OETrackerHits", "OETrackerHitsRelations", "OBTrackerHitsRelations",
                               "VBTrackerHits", "VETrackerHits", "VETrackerHitsRelations", "VBTrackerHitsRelations",
                                "InnerTrackerBarrelCollection", "InnerTrackerEndcapCollection",
                                "OuterTrackerBarrelCollection", "OuterTrackerEndcapCollection",
                                "VertexBarrelCollection", "VertexEndcapCollection",
                                "RelationMuonHit"
                                ],        
        "FullSubsetCollections": ["IBTrackerHitsConed", "IETrackerHitsConed", #CONED
                                "OBTrackerHitsConed", "OETrackerHitsConed", 
                                "VBTrackerHitsConed", "VETrackerHitsConed", 
                                
                                "InnerTrackerBarrelCollectionConed","InnerTrackerEndcapCollectionConed",
                                "OuterTrackerBarrelCollectionConed","OuterTrackerEndcapCollectionConed",
                                "VertexBarrelCollectionConed","VertexEndcapCollectionConed",

                                "IETrackerHitsRelationsConed","IBTrackerHitsRelationsConed",
                                "OETrackerHitsRelationsConed","OBTrackerHitsRelationsConed",
                                "VETrackerHitsRelationsConed","VBTrackerHitsRelationsConed"

                                    ], 
        "KeepCollectionNames": ["IBTrackerHitsConed", "IETrackerHitsConed", #CONED
                                "OBTrackerHitsConed", "OETrackerHitsConed", 
                                "VBTrackerHitsConed", "VETrackerHitsConed", 

                                "InnerTrackerBarrelCollectionConed","InnerTrackerEndcapCollectionConed",
                                "OuterTrackerBarrelCollectionConed","OuterTrackerEndcapCollectionConed",
                                "VertexBarrelCollectionConed","VertexEndcapCollectionConed",
 
                                "IETrackerHitsRelationsConed","IBTrackerHitsRelationsConed",
                                "OETrackerHitsRelationsConed","OBTrackerHitsRelationsConed",
                                "VETrackerHitsRelationsConed","VBTrackerHitsRelationsConed"                               
 
                                "SiTracks", "MCParticle_SiTracks",
                                "AllTracks"
                                ],
        "LCIOOutputFile": [the_args.outputFile],
        "LCIOWriteMode": ["WRITE_NEW"]
}

InitDD4hep = MarlinProcessorWrapper("InitDD4hep")
InitDD4hep.OutputLevel = INFO
InitDD4hep.ProcessorType = "InitializeDD4hep"
InitDD4hep.Parameters = {
    "DD4hepXMLFile": ["MAIA_v0/MAIA_v0.xml"], 
    "EncodingStringParameterName": ["GlobalTrackerReadoutID"]
}

VXDBarrelDigitiser = MarlinProcessorWrapper("VXDBarrelDigitiser")
VXDBarrelDigitiser.OutputLevel = INFO
VXDBarrelDigitiser.ProcessorType = "DDPlanarDigiProcessor"
VXDBarrelDigitiser.Parameters = {
    "CorrectTimesForPropagation": ["true"],
    "IsStrip": ["false"],
    "ResolutionT": ["0.03"],
    "ResolutionU": ["0.005"],
    "ResolutionV": ["0.005"],
    "SimTrackHitCollectionName": ["VertexBarrelCollection"],
    "SimTrkHitRelCollection": ["VBTrackerHitsRelations"],
    "SubDetectorName": ["Vertex"],
    "TimeWindowMax": ["0.15"],
    "TimeWindowMin": ["-0.09"],
    "TrackerHitCollectionName": ["VBTrackerHits"],
    "UseTimeWindow": ["true"]
}

VXDEndcapDigitiser = MarlinProcessorWrapper("VXDEndcapDigitiser")
VXDEndcapDigitiser.OutputLevel = INFO
VXDEndcapDigitiser.ProcessorType = "DDPlanarDigiProcessor"
VXDEndcapDigitiser.Parameters = {
    "CorrectTimesForPropagation": ["true"],
    "IsStrip": ["false"],
    "ResolutionT": ["0.03"],
    "ResolutionU": ["0.005"],
    "ResolutionV": ["0.005"],
    "SimTrackHitCollectionName": ["VertexEndcapCollection"],
    "SimTrkHitRelCollection": ["VETrackerHitsRelations"],
    "SubDetectorName": ["Vertex"],
    "TimeWindowMax": ["0.15"],
    "TimeWindowMin": ["-0.09"],
    "TrackerHitCollectionName": ["VETrackerHits"],
    "UseTimeWindow": ["true"]
}

InnerPlanarDigiProcessor = MarlinProcessorWrapper("InnerPlanarDigiProcessor")
InnerPlanarDigiProcessor.OutputLevel = INFO
InnerPlanarDigiProcessor.ProcessorType = "DDPlanarDigiProcessor"
InnerPlanarDigiProcessor.Parameters = {
    "CorrectTimesForPropagation": ["true"],
    "IsStrip": ["false"],
    "ResolutionT": ["0.06"],
    "ResolutionU": ["0.007"],
    "ResolutionV": ["0.090"],
    "SimTrackHitCollectionName": ["InnerTrackerBarrelCollection"],
    "SimTrkHitRelCollection": ["IBTrackerHitsRelations"],
    "SubDetectorName": ["InnerTrackers"],
    "TimeWindowMax": ["0.30"],
    "TimeWindowMin": ["-0.18"],
    "TrackerHitCollectionName": ["IBTrackerHits"],
    "UseTimeWindow": ["true"]
}

InnerEndcapPlanarDigiProcessor = MarlinProcessorWrapper(
    "InnerEndcapPlanarDigiProcessor")
InnerEndcapPlanarDigiProcessor.OutputLevel = INFO
InnerEndcapPlanarDigiProcessor.ProcessorType = "DDPlanarDigiProcessor"
InnerEndcapPlanarDigiProcessor.Parameters = {
    "CorrectTimesForPropagation": ["true"],
    "IsStrip": ["false"],
    "ResolutionT": ["0.06"],
    "ResolutionU": ["0.007"],
    "ResolutionV": ["0.090"],
    "SimTrackHitCollectionName": ["InnerTrackerEndcapCollection"],
    "SimTrkHitRelCollection": ["IETrackerHitsRelations"],
    "SubDetectorName": ["InnerTrackers"],
    "TimeWindowMax": ["0.30"],
    "TimeWindowMin": ["-0.18"],
    "TrackerHitCollectionName": ["IETrackerHits"],
    "UseTimeWindow": ["true"]
}

OuterPlanarDigiProcessor = MarlinProcessorWrapper("OuterPlanarDigiProcessor")
OuterPlanarDigiProcessor.OutputLevel = INFO
OuterPlanarDigiProcessor.ProcessorType = "DDPlanarDigiProcessor"
OuterPlanarDigiProcessor.Parameters = {
    "CorrectTimesForPropagation": ["true"],
    "IsStrip": ["false"],
    "ResolutionT": ["0.06"],
    "ResolutionU": ["0.007"],
    "ResolutionV": ["0.090"],
    "SimTrackHitCollectionName": ["OuterTrackerBarrelCollection"],
    "SimTrkHitRelCollection": ["OBTrackerHitsRelations"],
    "SubDetectorName": ["OuterTrackers"],
    "TimeWindowMax": ["0.30"],
    "TimeWindowMin": ["-0.18"],
    "TrackerHitCollectionName": ["OBTrackerHits"],
    "UseTimeWindow": ["true"]
}

OuterEndcapPlanarDigiProcessor = MarlinProcessorWrapper(
    "OuterEndcapPlanarDigiProcessor")
OuterEndcapPlanarDigiProcessor.OutputLevel = INFO
OuterEndcapPlanarDigiProcessor.ProcessorType = "DDPlanarDigiProcessor"
OuterEndcapPlanarDigiProcessor.Parameters = {
    "CorrectTimesForPropagation": ["true"],
    "IsStrip": ["false"],
    "ResolutionT": ["0.06"],
    "ResolutionU": ["0.007"],
    "ResolutionV": ["0.090"],
    "SimTrackHitCollectionName": ["OuterTrackerEndcapCollection"],
    "SimTrkHitRelCollection": ["OETrackerHitsRelations"],
    "SubDetectorName": ["OuterTrackers"],
    "TimeWindowMax": ["0.30"],
    "TimeWindowMin": ["-0.18"],
    "TrackerHitCollectionName": ["OETrackerHits"],
    "UseTimeWindow": ["true"]
}

VXDBarrelConer = MarlinProcessorWrapper("VXDBarrelConer")
VXDBarrelConer.OutputLevel = DEBUG
VXDBarrelConer.ProcessorType = "FilterConeHits"
VXDBarrelConer.Parameters = {
    "MCParticleCollection": ["MCParticle"],
    "TrackerHitInputCollections": ["VBTrackerHits"],
    "TrackerSimHitInputCollections": ["VertexBarrelCollection"],
    "TrackerHitInputRelations": ["VBTrackerHitsRelations"],
    "TrackerHitOutputCollections": ["VBTrackerHitsConed"],
    "TrackerSimHitOutputCollections": ["VertexBarrelCollectionConed"],
    "TrackerHitOutputRelations": ["VBTrackerHitsRelationsConed"],
    "DeltaRCut": ["0.4"],
    "ConeAroundStatus": ["22", "23", "51", "52"],
    "FillHistograms": ["false"]
}

VXDEndcapConer = MarlinProcessorWrapper("VXDEndcapConer")
VXDEndcapConer.OutputLevel = DEBUG
VXDEndcapConer.ProcessorType = "FilterConeHits"
VXDEndcapConer.Parameters = {
    "MCParticleCollection": ["MCParticle"],
    "TrackerHitInputCollections": ["VETrackerHits"],
    "TrackerSimHitInputCollections": ["VertexEndcapCollection"],
    "TrackerHitInputRelations": ["VETrackerHitsRelations"],
    "TrackerHitOutputCollections": ["VETrackerHitsConed"],
    "TrackerSimHitOutputCollections": ["VertexEndcapCollectionConed"],
    "TrackerHitOutputRelations": ["VETrackerHitsRelationsConed"],
    "DeltaRCut": ["0.4"],
    "ConeAroundStatus": ["22", "23", "51", "52"],
    "FillHistograms": ["false"]
}

InnerPlanarConer = MarlinProcessorWrapper("InnerPlanarConer")
InnerPlanarConer.OutputLevel = DEBUG 
InnerPlanarConer.ProcessorType = "FilterConeHits"
InnerPlanarConer.Parameters = {
    "MCParticleCollection": ["MCParticle"],
    "TrackerHitInputCollections": ["IBTrackerHits"],
    "TrackerSimHitInputCollections": ["InnerTrackerBarrelCollection"],
    "TrackerHitInputRelations": ["IBTrackerHitsRelations"],
    "TrackerHitOutputCollections": ["IBTrackerHitsConed"],
    "TrackerSimHitOutputCollections": ["InnerTrackerBarrelCollectionConed"],
    "TrackerHitOutputRelations": ["IBTrackerHitsRelationsConed"],
    "DeltaRCut": ["0.4"],
    "ConeAroundStatus": ["22", "23", "51", "52"],
    "FillHistograms": ["false"]
}

InnerEndcapConer = MarlinProcessorWrapper("InnerEndcapConer")
InnerEndcapConer.OutputLevel = DEBUG
InnerEndcapConer.ProcessorType = "FilterConeHits"
InnerEndcapConer.Parameters = {
    "MCParticleCollection": ["MCParticle"],
    "TrackerHitInputCollections": ["IETrackerHits"],
    "TrackerSimHitInputCollections": ["InnerTrackerEndcapCollection"],
    "TrackerHitInputRelations": ["IETrackerHitsRelations"],
    "TrackerHitOutputCollections": ["IETrackerHitsConed"],
    "TrackerSimHitOutputCollections": ["InnerTrackerEndcapCollectionConed"],
    "TrackerHitOutputRelations": ["IETrackerHitsRelationsConed"],
    "DeltaRCut": ["0.4"],
    "ConeAroundStatus": ["22", "23", "51", "52"],
    "FillHistograms": ["false"]
}

OuterPlanarConer = MarlinProcessorWrapper("OuterPlanarConer")
OuterPlanarConer.OutputLevel = DEBUG
OuterPlanarConer.ProcessorType = "FilterConeHits"
OuterPlanarConer.Parameters = {
    "MCParticleCollection": ["MCParticle"],
    "TrackerHitInputCollections": ["OBTrackerHits"],
    "TrackerSimHitInputCollections": ["OuterTrackerBarrelCollection"],
    "TrackerHitInputRelations": ["OBTrackerHitsRelations"],
    "TrackerHitOutputCollections": ["OBTrackerHitsConed"],
    "TrackerSimHitOutputCollections": ["OuterTrackerBarrelCollectionConed"],
    "TrackerHitOutputRelations": ["OBTrackerHitsRelationsConed"],
    "DeltaRCut": ["0.4"],
    "FillHistograms": ["false"],
    "ConeAroundStatus": ["22", "23", "51", "52"],
}

OuterEndcapConer = MarlinProcessorWrapper("OuterEndcapConer")
OuterEndcapConer.OutputLevel = DEBUG
OuterEndcapConer.ProcessorType = "FilterConeHits"
OuterEndcapConer.Parameters = {
    "MCParticleCollection": ["MCParticle"],
    "TrackerHitInputCollections": ["OETrackerHits"],
    "TrackerSimHitInputCollections": ["OuterTrackerEndcapCollection"],
    "TrackerHitInputRelations": ["OETrackerHitsRelations"],
    "TrackerHitOutputCollections": ["OETrackerHitsConed"],
    "TrackerSimHitOutputCollections": ["OuterTrackerEndcapCollectionConed"],
    "TrackerHitOutputRelations": ["OETrackerHitsRelationsConed"],
    "DeltaRCut": ["0.4"],
    "ConeAroundStatus": ["22", "23", "51", "52"],
    "FillHistograms": ["false"]
}

CKFTracking = MarlinProcessorWrapper("CKFTracking")
CKFTracking.OutputLevel = DEBUG
CKFTracking.ProcessorType = "ACTSSeededCKFTrackingProc"
CKFTracking.Parameters = {
    "CKF_Chi2CutOff": ["10"],
    "CKF_NumMeasurementsCutOff": ["1"],
    "CaloFace_Radius": ["1857"],
    "CaloFace_Z": ["2307"],
    "MatFile": ["MAIA_v0_material.json"],
    "PropagateBackward": ["False"],
    "DetectorSchema": ["MAIA_v0"],
    "RunCKF": ["True"],
    "SeedFinding_CollisionRegion": ["6"],
    # "SeedFinding_DeltaRMax": ["60"],
    # "SeedFinding_DeltaRMin": ["2"],
    # "SeedFinding_DeltaRMaxBottom": ["50"],
    # "SeedFinding_DeltaRMaxTop": ["50"],
    # "SeedFinding_DeltaRMinBottom": ["5"],
    # "SeedFinding_DeltaRMinTop": ["2"],
    "SeedFinding_ImpactMax": ["3"],
    "SeedFinding_MinPt": ["10000"],
    "SeedFinding_RMax": ["150"],
    "SeedFinding_ZMax": ["600"],
    "SeedFinding_RadLengthPerSeed": ["0.1"],
    # "SeedFinding_zBottomBinLen": ["1"],
    # "SeedFinding_zTopBinLen": ["1"],
    # "SeedFinding_phiBottomBinLen": ["1"],
    # "SeedFinding_phiTopBinLen": ["1"],
    "SeedFinding_SigmaScattering": ["50"], 
    "SeedingLayers": ["13", "2", "13", "6", "13", "10", "13", "14",
                      "14", "2", "14", "6", "14", "8", "14", "10", 
                      "15", "2", "15", "6", "15", "10", "15", "14",
                      "8", "2",
                      "17", "2",
                      "18", "2"],
    "TGeoFile": ["MAIA_v0.root"],
    "TGeoDescFile": ["MAIA_v0.json"],
    "TrackCollectionName": ["AllTracks"],
    "TrackerHitCollectionNames": ["VBTrackerHitsConed", "IBTrackerHitsConed", "OBTrackerHitsConed", "VETrackerHitsConed", "IETrackerHitsConed", "OETrackerHitsConed"] #CONED
}

TrackDeduper = MarlinProcessorWrapper("TrackDeduplication")
TrackDeduper.OutputLevel = INFO
TrackDeduper.ProcessorType = "ACTSDuplicateRemoval"
TrackDeduper.Parameters = {
    "InputTrackCollectionName": ["AllTracks"],
    "OutputTrackCollectionName": ["SiTracks"]
}

# Refit = MarlinProcessorWrapper("Refit")
# Refit.OutputLevel = WARNING
# Refit.ProcessorType = "RefitFinal"
# Refit.Parameters = {
#     "DoCutsOnRedChi2Nhits": ["true"],
#     "EnergyLossOn": ["true"],
#     "InputRelationCollectionName": ["SiTrackRelations"],
#     "InputTrackCollectionName": ["SiTracks"],
#     "Max_Chi2_Incr": ["1.79769e+30"],
#     "MinClustersOnTrackAfterFit": ["3"],
#     "MultipleScatteringOn": ["true"],
#     "NHitsCuts": ["1,2", "1", "3,4", "1", "5,6", "0"],
#     "OutputRelationCollectionName": ["SiTracks_Refitted_Relation"],
#     "OutputTrackCollectionName": ["SiTracks_Refitted"],
#     "ReducedChi2Cut": ["10."],
#     "ReferencePoint": ["-1"],
#     "SmoothOn": ["false"],
#     "extrapolateForward": ["true"]
# }

MyTrackTruth = MarlinProcessorWrapper("FirstTrackTruth")
MyTrackTruth.OutputLevel = INFO
MyTrackTruth.ProcessorType = "TrackTruthProc"
MyTrackTruth.Parameters = {
    "MCParticleCollection": ["MCParticle"],
    "Particle2TrackRelationName": ["MCParticle_SiTracks"],
    "TrackCollection": ["SiTracks"],
    "TrackerHit2SimTrackerHitRelationName": ["VBTrackerHitsRelationsConed", "IBTrackerHitsRelationsConed", "OBTrackerHitsRelationsConed", "VETrackerHitsRelationsConed", "IETrackerHitsRelationsConed", "OETrackerHitsRelationsConed"] #CONED
}

OverlayMIX = MarlinProcessorWrapper("OverlayMIX")
OverlayMIX.OutputLevel = DEBUG
OverlayMIX.ProcessorType = "OverlayTimingRandomMix"
OverlayMIX.Parameters = {
    "PathToMuPlus": ["/ospool/uc-shared/public/futurecolliders/v5/simBIB/mp_pruned"],
    "PathToMuMinus": ["/ospool/uc-shared/public/futurecolliders/v5/simBIB/mm_pruned"],
    "Collection_IntegrationTimes": [
        "VertexBarrelCollection", "-0.09", "0.32",
        "VertexEndcapCollection", "-0.09", "0.32",
        "InnerTrackerBarrelCollection", "-0.18", "1.30",
        "InnerTrackerEndcapCollection", "-0.18", "1.30",
        "OuterTrackerBarrelCollection", "-0.18", "4.00",
        "OuterTrackerEndcapCollection", "-0.18", "4.00"
    ],
    "IntegrationTimeMin": ["-0.5"],
    "MCParticleCollectionName": ["MCParticle"],
    "MergeMCParticles": ["false"],
    "NumberBackground": [the_args.OverlayFullNumberBackground]
}

algList.append(MyAIDAProcessor)
algList.append(EventNumber)
algList.append(InitDD4hep)
algList.append(OverlayMIX)
algList.append(VXDBarrelDigitiser)
algList.append(VXDEndcapDigitiser)
algList.append(InnerPlanarDigiProcessor)
algList.append(InnerEndcapPlanarDigiProcessor)
algList.append(OuterPlanarDigiProcessor)
algList.append(OuterEndcapPlanarDigiProcessor)
algList.append(VXDBarrelConer)
algList.append(VXDEndcapConer)
algList.append(InnerPlanarConer)
algList.append(InnerEndcapConer)
algList.append(OuterPlanarConer)
algList.append(OuterEndcapConer)
algList.append(CKFTracking)
algList.append(TrackDeduper)
algList.append(MyTrackTruth)
algList.append(Output_REC)

ApplicationMgr(TopAlg=algList,
               EvtSel='NONE',
               EvtMax=-1,
               ExtSvc=[evtsvc],
               OutputLevel=INFO
               )