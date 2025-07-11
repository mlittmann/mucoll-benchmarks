from GaudiKernel.Constants import INFO, WARNING
from Configurables import DDPlanarDigi

def new_VXDBarrel(args):
    """
    Create a new vertex barrel instance with the given parameters.
    """
    if args.doOverlayFull:
        inputHitCollections = ["OverlayVertexBarrelCollection"]
    else:
        inputHitCollections = ["VertexBarrelCollection"]
    return DDPlanarDigi(
        "VXDBarrelDigitiser",
        CorrectTimesForPropagation = True,
        IsStrip = False,
        ResolutionT = [0.03],
        ResolutionU = [0.005],
        ResolutionV = [0.005],
        SubDetectorName = "Vertex",
        TimeWindowMax = [0.15],
        TimeWindowMin = [-0.09],
        UseTimeWindow = True,
        SimTrackerHitCollectionName = inputHitCollections,
        SimTrkHitRelCollection = ["VXDBarrelHitsRelations"],
        TrackerHitCollectionName = ["VXDBarrelHits"],
        OutputLevel = INFO
    )

def new_VXDEndcap(args):
    """
    Create a new vertex endcap instance with the given parameters.
    """
    if args.doOverlayFull:
        inputHitCollections = ["OverlayVertexEndcapCollection"]
    else:
        inputHitCollections = ["VertexEndcapCollection"]
    return DDPlanarDigi(
        "VXDEndcapDigitiser",
        CorrectTimesForPropagation = True,
        IsStrip = False,
        ResolutionT = [0.03],
        ResolutionU = [0.005],
        ResolutionV = [0.005],
        SubDetectorName = "Vertex",
        TimeWindowMax = [0.15],
        TimeWindowMin = [-0.09],
        UseTimeWindow = True,
        SimTrackerHitCollectionName = inputHitCollections,
        SimTrkHitRelCollection = ["VXDEndcapHitsRelations"],
        TrackerHitCollectionName = ["VXDEndcapHits"],
        OutputLevel = INFO
    )