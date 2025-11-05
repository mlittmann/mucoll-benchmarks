from Gaudi.Configuration import *

def makeRecoAlgList(the_args):
    '''-------------------------------------------------------------'''
    '''   Add the Reconstruction Algorithms to the Algorithm List   '''
    '''-------------------------------------------------------------'''
    algList = []
    # Merging
    from reco_components.mergers import new_mergehits, new_mergehitsrelations
    algList.append(new_mergehits())
    algList.append(new_mergehitsrelations())

    # CKF Tracking
    from reco_components.CKF_tracking import new_CKFTracker, new_deduper, new_track_filter, new_track_truth, new_track_refitter
    algList.append(new_CKFTracker(
        the_args.MatFile,
        the_args.TGeoFile
        the_args.TGeoDescFile))
    algList.append(new_deduper())
    algList.append(new_track_filter())
    algList.append(new_track_truth())
    algList.append(new_track_refitter())

    # Track Performance Monitoring
    if the_args.doTrackPerf:
        from reco_components.track_performance import new_trackTruth, new_trackPerf
        algList.append(new_trackTruth())
        algList.append(new_trackPerf())

    # Pandora PFOs
    from reco_components.pandora import new_pandoraPFA #, new_fastJet
    algList.append(new_pandoraPFA())
    # algList.append(new_fastJet())

    return algList
