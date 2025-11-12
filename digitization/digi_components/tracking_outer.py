from GaudiKernel.Constants import INFO, WARNING
from Configurables import DDPlanarDigi

def new_OTBarrel(args):
    """
    Create a new outer barrel digitiser instance with the given parameters.
    """
    if args.doOverlayFull:
        inputHitCollections = ["OverlayOuterTrackerBarrelCollection"]
    else:
        inputHitCollections = ["OuterTrackerBarrelCollection"]
    return DDPlanarDigi(
        "OTBarrelDigitiser",
        CorrectTimesForPropagation = True,
        IsStrip = False,
        ResolutionT = [0.06],
        ResolutionU = [0.007],
        ResolutionV = [0.09],
        SubDetectorName = "OuterTrackers",
        TimeWindowMax = [10.00],
        TimeWindowMin = [-0.18],
        UseTimeWindow = True,
        SimTrackHitCollectionName = inputHitCollections,
        SimTrkHitRelCollection = ["OTBarrelHitsRelations"],
        TrackerHitCollectionName = ["OTBarrelHits"],
        OutputLevel = INFO
    )

def new_OTEndcap(args):
    """
    Create a new outer endcap digitiser instance with the given parameters.
    """
    if args.doOverlayFull:
        inputHitCollections = ["OverlayOuterTrackerEndcapCollection"]
    else:
        inputHitCollections = ["OuterTrackerEndcapCollection"]
    return DDPlanarDigi(
        "OTEndcapDigitiser",
        CorrectTimesForPropagation = True,
        IsStrip = True,
        ResolutionT = [0.06],
        ResolutionU = [0.007],
        ResolutionV = [0.09],
        SubDetectorName = "OuterTrackers",
        TimeWindowMax = [10.00],
        TimeWindowMin = [-0.18],
        UseTimeWindow = True,
        SimTrackHitCollectionName = inputHitCollections,
        SimTrkHitRelCollection = ["OTEndcapHitsRelations"],
        TrackerHitCollectionName = ["OTEndcapHits"],
        OutputLevel = INFO
    )
