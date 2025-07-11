#Tue Jun 10 12:36:49 2025"""Automatically generated. DO NOT EDIT please"""
from GaudiKernel.Proxy.Configurable import *

class ACTSDuplicateRemoval( ConfigurableAlgorithm ) :
  __slots__ = { 
    'ExtraInputs' : set(),
    'ExtraOutputs' : set(),
    'OutputLevel' : 0,
    'Enable' : True,
    'ErrorMax' : 1,
    'AuditAlgorithms' : False,
    'AuditInitialize' : False,
    'AuditReinitialize' : False,
    'AuditRestart' : False,
    'AuditExecute' : False,
    'AuditFinalize' : False,
    'AuditStart' : False,
    'AuditStop' : False,
    'Timeline' : True,
    'MonitorService' : 'MonitorSvc',
    'RegisterForContextService' : False,
    'Cardinality' : 0,
    'NeededResources' : [  ],
    'Asynchronous' : False,
    'FilterCircularDependencies' : True,
    'InputTrackCollectionName' : [ 'TruthTracks' ],
    'OutputTrackCollectionName' : [ 'DedupedTruthTracks' ],
  }
  _propertyDocDct = { 
    'ExtraInputs' : """  [DataHandleHolderBase<PropertyHolder<CommonMessaging<implements<IAlgorithm,IDataHandleHolder,IProperty,IStateful> > > >] """,
    'ExtraOutputs' : """  [DataHandleHolderBase<PropertyHolder<CommonMessaging<implements<IAlgorithm,IDataHandleHolder,IProperty,IStateful> > > >] """,
    'OutputLevel' : """ output level [Gaudi::Algorithm] """,
    'Enable' : """ should the algorithm be executed or not [Gaudi::Algorithm] """,
    'ErrorMax' : """ [[deprecated]] max number of errors [Gaudi::Algorithm] """,
    'AuditAlgorithms' : """ [[deprecated]] unused [Gaudi::Algorithm] """,
    'AuditInitialize' : """ trigger auditor on initialize() [Gaudi::Algorithm] """,
    'AuditReinitialize' : """ trigger auditor on reinitialize() [Gaudi::Algorithm] """,
    'AuditRestart' : """ trigger auditor on restart() [Gaudi::Algorithm] """,
    'AuditExecute' : """ trigger auditor on execute() [Gaudi::Algorithm] """,
    'AuditFinalize' : """ trigger auditor on finalize() [Gaudi::Algorithm] """,
    'AuditStart' : """ trigger auditor on start() [Gaudi::Algorithm] """,
    'AuditStop' : """ trigger auditor on stop() [Gaudi::Algorithm] """,
    'Timeline' : """ send events to TimelineSvc [Gaudi::Algorithm] """,
    'MonitorService' : """ name to use for Monitor Service [Gaudi::Algorithm] """,
    'RegisterForContextService' : """ flag to enforce the registration for Algorithm Context Service [Gaudi::Algorithm] """,
    'Cardinality' : """ how many clones to create - 0 means algo is reentrant [Gaudi::Algorithm] """,
    'NeededResources' : """ named resources needed during event looping [Gaudi::Algorithm] """,
    'Asynchronous' : """ whether algorithm is asynchronous and uses Boost Fiber to suspend while offloaded code is running. [Gaudi::Algorithm] """,
    'FilterCircularDependencies' : """ filter out circular data dependencies [Gaudi::Algorithm] """,
    'InputTrackCollectionName' : """  [k4FWCore::details::Transformer<edm4hep::TrackCollection (edm4hep::TrackCollection const&),Gaudi::Functional::Traits::use_<> >] """,
    'OutputTrackCollectionName' : """  [k4FWCore::details::Transformer<edm4hep::TrackCollection (edm4hep::TrackCollection const&),Gaudi::Functional::Traits::use_<> >] """,
  }
  __declaration_location__ = 'ACTSDuplicateRemoval.cxx:82'
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(ACTSDuplicateRemoval, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'ACTSTrackingPlugins'
  def getType( self ):
      return 'ACTSDuplicateRemoval'
  pass # class ACTSDuplicateRemoval

class ACTSSeededCKFTrackingAlg( ConfigurableAlgorithm ) :
  __slots__ = { 
    'ExtraInputs' : set(),
    'ExtraOutputs' : set(),
    'OutputLevel' : 0,
    'Enable' : True,
    'ErrorMax' : 1,
    'AuditAlgorithms' : False,
    'AuditInitialize' : False,
    'AuditReinitialize' : False,
    'AuditRestart' : False,
    'AuditExecute' : False,
    'AuditFinalize' : False,
    'AuditStart' : False,
    'AuditStop' : False,
    'Timeline' : True,
    'MonitorService' : 'MonitorSvc',
    'RegisterForContextService' : False,
    'Cardinality' : 0,
    'NeededResources' : [  ],
    'Asynchronous' : False,
    'FilterCircularDependencies' : True,
    'InputTrackerHitCollectionName' : [ 'TrackerHits' ],
    'OutputSeedCollectionName' : [ 'SeedTracks' ],
    'OutputTrackCollectionName' : [ 'Tracks' ],
    'MatFile' : '',
    'TGeoFile' : '',
    'EncodingStringParameterName' : 'GlobalTrackerReadoutID',
    'RunCKF' : True,
    'PropagateBackward' : False,
    'SeedFinding_RMax' : 150.000,
    'SeedFinding_DeltaRMin' : 5.00000,
    'SeedFinding_DeltaRMax' : 80.0000,
    'SeedFinding_DeltaRMinTop' : 0.00000,
    'SeedFinding_DeltaRMaxTop' : 0.00000,
    'SeedFinding_DeltaRMinBottom' : 0.00000,
    'SeedFinding_DeltaRMaxBottom' : 0.00000,
    'SeedFinding_CollisionRegion' : 75.0000,
    'SeedFinding_ZMax' : 600.000,
    'SeedFinding_SigmaScattering' : 50.0000,
    'SeedFinding_RadLengthPerSeed' : 0.100000,
    'SeedFinding_MinPt' : 500.000,
    'SeedFinding_ImpactMax' : 3.00000,
    'SeedFinding_zBinEdges' : [  ],
    'SeedFinding_zTopBinLen' : 1,
    'SeedFinding_zBottomBinLen' : 1,
    'SeedFinding_phiTopBinLen' : 1,
    'SeedFinding_phiBottomBinLen' : 1,
    'InitialTrackError_Pos' : 0.010000000,
    'InitialTrackError_Phi' : 0.017453293,
    'InitialTrackError_RelP' : 0.25000000,
    'InitialTrackError_Lambda' : 0.017453293,
    'InitialTrackError_Time' : 29979.246,
    'CKF_Chi2CutOff' : 15.000000,
    'CKF_NumMeasurementsCutOff' : 10,
    'SeedingLayers' : [  ],
  }
  _propertyDocDct = { 
    'ExtraInputs' : """  [DataHandleHolderBase<PropertyHolder<CommonMessaging<implements<IAlgorithm,IDataHandleHolder,IProperty,IStateful> > > >] """,
    'ExtraOutputs' : """  [DataHandleHolderBase<PropertyHolder<CommonMessaging<implements<IAlgorithm,IDataHandleHolder,IProperty,IStateful> > > >] """,
    'OutputLevel' : """ output level [Gaudi::Algorithm] """,
    'Enable' : """ should the algorithm be executed or not [Gaudi::Algorithm] """,
    'ErrorMax' : """ [[deprecated]] max number of errors [Gaudi::Algorithm] """,
    'AuditAlgorithms' : """ [[deprecated]] unused [Gaudi::Algorithm] """,
    'AuditInitialize' : """ trigger auditor on initialize() [Gaudi::Algorithm] """,
    'AuditReinitialize' : """ trigger auditor on reinitialize() [Gaudi::Algorithm] """,
    'AuditRestart' : """ trigger auditor on restart() [Gaudi::Algorithm] """,
    'AuditExecute' : """ trigger auditor on execute() [Gaudi::Algorithm] """,
    'AuditFinalize' : """ trigger auditor on finalize() [Gaudi::Algorithm] """,
    'AuditStart' : """ trigger auditor on start() [Gaudi::Algorithm] """,
    'AuditStop' : """ trigger auditor on stop() [Gaudi::Algorithm] """,
    'Timeline' : """ send events to TimelineSvc [Gaudi::Algorithm] """,
    'MonitorService' : """ name to use for Monitor Service [Gaudi::Algorithm] """,
    'RegisterForContextService' : """ flag to enforce the registration for Algorithm Context Service [Gaudi::Algorithm] """,
    'Cardinality' : """ how many clones to create - 0 means algo is reentrant [Gaudi::Algorithm] """,
    'NeededResources' : """ named resources needed during event looping [Gaudi::Algorithm] """,
    'Asynchronous' : """ whether algorithm is asynchronous and uses Boost Fiber to suspend while offloaded code is running. [Gaudi::Algorithm] """,
    'FilterCircularDependencies' : """ filter out circular data dependencies [Gaudi::Algorithm] """,
    'InputTrackerHitCollectionName' : """  [k4FWCore::details::MultiTransformer<std::tuple<edm4hep::TrackCollection,edm4hep::TrackCollection> (edm4hep::TrackerHitPlaneCollection const&),Gaudi::Functional::Traits::use_<> >] """,
    'OutputSeedCollectionName' : """  [k4FWCore::details::MultiTransformer<std::tuple<edm4hep::TrackCollection,edm4hep::TrackCollection> (edm4hep::TrackerHitPlaneCollection const&),Gaudi::Functional::Traits::use_<> >] """,
    'OutputTrackCollectionName' : """  [k4FWCore::details::MultiTransformer<std::tuple<edm4hep::TrackCollection,edm4hep::TrackCollection> (edm4hep::TrackerHitPlaneCollection const&),Gaudi::Functional::Traits::use_<> >] """,
    'MatFile' : """ Path to the material description JSON file. Can be empty. [ACTSAlgBase] """,
    'TGeoFile' : """ Path to the tracker geometry file. [ACTSAlgBase] """,
    'EncodingStringParameterName' : """ The name of the DD4hep constant that contains the Encoding string for the detector [ACTSAlgBase] """,
    'RunCKF' : """ Run tracking using CKF. False means stop at the seeding stage. [ACTSSeededCKFTrackingAlg] """,
    'PropagateBackward' : """ Extrapolates tracks towards beamline. [ACTSSeededCKFTrackingAlg] """,
    'SeedFinding_RMax' : """ Maximum radius of hits to consider. [ACTSSeededCKFTrackingAlg] """,
    'SeedFinding_DeltaRMin' : """ Minimum dR between hits in a seed. [ACTSSeededCKFTrackingAlg] """,
    'SeedFinding_DeltaRMax' : """ Maximum dR between hits in a seed. [ACTSSeededCKFTrackingAlg] """,
    'SeedFinding_DeltaRMinTop' : """ Minimum dR between the reference hit and outer ones in a seed. [ACTSSeededCKFTrackingAlg] """,
    'SeedFinding_DeltaRMaxTop' : """ Maximum dR between the reference hit and outer ones in a seed. [ACTSSeededCKFTrackingAlg] """,
    'SeedFinding_DeltaRMinBottom' : """ Minimum dR between the reference hit and inner ones in a seed. [ACTSSeededCKFTrackingAlg] """,
    'SeedFinding_DeltaRMaxBottom' : """ Maximum dR between the reference hit and inner ones in a seed. [ACTSSeededCKFTrackingAlg] """,
    'SeedFinding_CollisionRegion' : """ Size of the collision region in one direction (assumed symmetric). [ACTSSeededCKFTrackingAlg] """,
    'SeedFinding_ZMax' : """ Maximum z of hits to consider. [ACTSSeededCKFTrackingAlg] """,
    'SeedFinding_SigmaScattering' : """ Number of sigmas to allow in scattering angle. [ACTSSeededCKFTrackingAlg] """,
    'SeedFinding_RadLengthPerSeed' : """ Average radiation length per seed. [ACTSSeededCKFTrackingAlg] """,
    'SeedFinding_MinPt' : """ Minimum pT of tracks to seed. [ACTSSeededCKFTrackingAlg] """,
    'SeedFinding_ImpactMax' : """ Maximum d0 of tracks to seed. [ACTSSeededCKFTrackingAlg] """,
    'SeedFinding_zBinEdges' : """ Bins placement along Z for seeding. [ACTSSeededCKFTrackingAlg] """,
    'SeedFinding_zTopBinLen' : """ Number of top bins along Z for seeding. [ACTSSeededCKFTrackingAlg] """,
    'SeedFinding_zBottomBinLen' : """ Number of bottom bins along Z for seeding. [ACTSSeededCKFTrackingAlg] """,
    'SeedFinding_phiTopBinLen' : """ Number of top bins along phi for seeding. [ACTSSeededCKFTrackingAlg] """,
    'SeedFinding_phiBottomBinLen' : """ Number of bottom bins along phi for seeding. [ACTSSeededCKFTrackingAlg] """,
    'InitialTrackError_Pos' : """ Track error estimate, local position (mm). [ACTSSeededCKFTrackingAlg] """,
    'InitialTrackError_Phi' : """ Track error estimate, phi (radians). [ACTSSeededCKFTrackingAlg] """,
    'InitialTrackError_RelP' : """ Track error estimate, momentum component (relative). [ACTSSeededCKFTrackingAlg] """,
    'InitialTrackError_Lambda' : """ Track error estimate, lambda (radians). [ACTSSeededCKFTrackingAlg] """,
    'InitialTrackError_Time' : """ Track error estimate, time (sec). [ACTSSeededCKFTrackingAlg] """,
    'CKF_Chi2CutOff' : """ Maximum local chi2 contribution. [ACTSSeededCKFTrackingAlg] """,
    'CKF_NumMeasurementsCutOff' : """ Maximum number of associated measurements on a single surface. [ACTSSeededCKFTrackingAlg] """,
    'SeedingLayers' : """ Layers to use for seeding in vector. [ACTSSeededCKFTrackingAlg] """,
  }
  __declaration_location__ = 'ACTSSeededCKFTrackingAlg.cxx:45'
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(ACTSSeededCKFTrackingAlg, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'ACTSTrackingPlugins'
  def getType( self ):
      return 'ACTSSeededCKFTrackingAlg'
  pass # class ACTSSeededCKFTrackingAlg

class FilterTracksAlg( ConfigurableAlgorithm ) :
  __slots__ = { 
    'ExtraInputs' : set(),
    'ExtraOutputs' : set(),
    'OutputLevel' : 0,
    'Enable' : True,
    'ErrorMax' : 1,
    'AuditAlgorithms' : False,
    'AuditInitialize' : False,
    'AuditReinitialize' : False,
    'AuditRestart' : False,
    'AuditExecute' : False,
    'AuditFinalize' : False,
    'AuditStart' : False,
    'AuditStop' : False,
    'Timeline' : True,
    'MonitorService' : 'MonitorSvc',
    'RegisterForContextService' : False,
    'Cardinality' : 0,
    'NeededResources' : [  ],
    'Asynchronous' : False,
    'FilterCircularDependencies' : True,
    'InputTrackCollectionName' : [ 'Tracks' ],
    'OutputTrackCollectionName' : [ 'FilteredTracks' ],
    'NHitsTotal' : 7,
    'NHitsVertex' : 3,
    'NHitsInner' : 2,
    'NHitsOuter' : 1,
    'MaxD0' : 5.00000,
    'MaxZ0' : 5.00000,
    'MinPt' : 1.00000,
  }
  _propertyDocDct = { 
    'ExtraInputs' : """  [DataHandleHolderBase<PropertyHolder<CommonMessaging<implements<IAlgorithm,IDataHandleHolder,IProperty,IStateful> > > >] """,
    'ExtraOutputs' : """  [DataHandleHolderBase<PropertyHolder<CommonMessaging<implements<IAlgorithm,IDataHandleHolder,IProperty,IStateful> > > >] """,
    'OutputLevel' : """ output level [Gaudi::Algorithm] """,
    'Enable' : """ should the algorithm be executed or not [Gaudi::Algorithm] """,
    'ErrorMax' : """ [[deprecated]] max number of errors [Gaudi::Algorithm] """,
    'AuditAlgorithms' : """ [[deprecated]] unused [Gaudi::Algorithm] """,
    'AuditInitialize' : """ trigger auditor on initialize() [Gaudi::Algorithm] """,
    'AuditReinitialize' : """ trigger auditor on reinitialize() [Gaudi::Algorithm] """,
    'AuditRestart' : """ trigger auditor on restart() [Gaudi::Algorithm] """,
    'AuditExecute' : """ trigger auditor on execute() [Gaudi::Algorithm] """,
    'AuditFinalize' : """ trigger auditor on finalize() [Gaudi::Algorithm] """,
    'AuditStart' : """ trigger auditor on start() [Gaudi::Algorithm] """,
    'AuditStop' : """ trigger auditor on stop() [Gaudi::Algorithm] """,
    'Timeline' : """ send events to TimelineSvc [Gaudi::Algorithm] """,
    'MonitorService' : """ name to use for Monitor Service [Gaudi::Algorithm] """,
    'RegisterForContextService' : """ flag to enforce the registration for Algorithm Context Service [Gaudi::Algorithm] """,
    'Cardinality' : """ how many clones to create - 0 means algo is reentrant [Gaudi::Algorithm] """,
    'NeededResources' : """ named resources needed during event looping [Gaudi::Algorithm] """,
    'Asynchronous' : """ whether algorithm is asynchronous and uses Boost Fiber to suspend while offloaded code is running. [Gaudi::Algorithm] """,
    'FilterCircularDependencies' : """ filter out circular data dependencies [Gaudi::Algorithm] """,
    'InputTrackCollectionName' : """  [k4FWCore::details::Transformer<edm4hep::TrackCollection (edm4hep::TrackCollection const&),Gaudi::Functional::Traits::use_<> >] """,
    'OutputTrackCollectionName' : """  [k4FWCore::details::Transformer<edm4hep::TrackCollection (edm4hep::TrackCollection const&),Gaudi::Functional::Traits::use_<> >] """,
    'NHitsTotal' : """ Minimum number of hits on track [FilterTracksAlg] """,
    'NHitsVertex' : """ Minimum number of hits on vertex detector [FilterTracksAlg] """,
    'NHitsInner' : """ Minimum number of hits on inner tracker [FilterTracksAlg] """,
    'NHitsOuter' : """ Minimum number of hits on outer tracker [FilterTracksAlg] """,
    'MaxD0' : """ Maximum D0 value for a track [FilterTracksAlg] """,
    'MaxZ0' : """ Maximum Z0 value for a track [FilterTracksAlg] """,
    'MinPt' : """ Minimum transverse momentum [FilterTracksAlg] """,
  }
  __declaration_location__ = 'FilterTracksAlg.cxx:16'
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(FilterTracksAlg, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'ACTSTrackingPlugins'
  def getType( self ):
      return 'FilterTracksAlg'
  pass # class FilterTracksAlg

class TrackTruthAlg( ConfigurableAlgorithm ) :
  __slots__ = { 
    'ExtraInputs' : set(),
    'ExtraOutputs' : set(),
    'OutputLevel' : 0,
    'Enable' : True,
    'ErrorMax' : 1,
    'AuditAlgorithms' : False,
    'AuditInitialize' : False,
    'AuditReinitialize' : False,
    'AuditRestart' : False,
    'AuditExecute' : False,
    'AuditFinalize' : False,
    'AuditStart' : False,
    'AuditStop' : False,
    'Timeline' : True,
    'MonitorService' : 'MonitorSvc',
    'RegisterForContextService' : False,
    'Cardinality' : 0,
    'NeededResources' : [  ],
    'Asynchronous' : False,
    'FilterCircularDependencies' : True,
    'InputTrackCollectionName' : [ 'Tracks' ],
    'InputTrackerHit2SimTrackerHitRelationName' : [ 'TrackMCRelation' ],
    'OutputParticle2TrackRelationName' : [ 'Particle2TrackRelationName' ],
  }
  _propertyDocDct = { 
    'ExtraInputs' : """  [DataHandleHolderBase<PropertyHolder<CommonMessaging<implements<IAlgorithm,IDataHandleHolder,IProperty,IStateful> > > >] """,
    'ExtraOutputs' : """  [DataHandleHolderBase<PropertyHolder<CommonMessaging<implements<IAlgorithm,IDataHandleHolder,IProperty,IStateful> > > >] """,
    'OutputLevel' : """ output level [Gaudi::Algorithm] """,
    'Enable' : """ should the algorithm be executed or not [Gaudi::Algorithm] """,
    'ErrorMax' : """ [[deprecated]] max number of errors [Gaudi::Algorithm] """,
    'AuditAlgorithms' : """ [[deprecated]] unused [Gaudi::Algorithm] """,
    'AuditInitialize' : """ trigger auditor on initialize() [Gaudi::Algorithm] """,
    'AuditReinitialize' : """ trigger auditor on reinitialize() [Gaudi::Algorithm] """,
    'AuditRestart' : """ trigger auditor on restart() [Gaudi::Algorithm] """,
    'AuditExecute' : """ trigger auditor on execute() [Gaudi::Algorithm] """,
    'AuditFinalize' : """ trigger auditor on finalize() [Gaudi::Algorithm] """,
    'AuditStart' : """ trigger auditor on start() [Gaudi::Algorithm] """,
    'AuditStop' : """ trigger auditor on stop() [Gaudi::Algorithm] """,
    'Timeline' : """ send events to TimelineSvc [Gaudi::Algorithm] """,
    'MonitorService' : """ name to use for Monitor Service [Gaudi::Algorithm] """,
    'RegisterForContextService' : """ flag to enforce the registration for Algorithm Context Service [Gaudi::Algorithm] """,
    'Cardinality' : """ how many clones to create - 0 means algo is reentrant [Gaudi::Algorithm] """,
    'NeededResources' : """ named resources needed during event looping [Gaudi::Algorithm] """,
    'Asynchronous' : """ whether algorithm is asynchronous and uses Boost Fiber to suspend while offloaded code is running. [Gaudi::Algorithm] """,
    'FilterCircularDependencies' : """ filter out circular data dependencies [Gaudi::Algorithm] """,
    'InputTrackCollectionName' : """  [k4FWCore::details::MultiTransformer<std::tuple<edm4hep::TrackMCParticleLinkCollection> (edm4hep::TrackCollection const&,edm4hep::TrackerHitSimTrackerHitLinkCollection const&),Gaudi::Functional::Traits::use_<> >] """,
    'InputTrackerHit2SimTrackerHitRelationName' : """  [k4FWCore::details::MultiTransformer<std::tuple<edm4hep::TrackMCParticleLinkCollection> (edm4hep::TrackCollection const&,edm4hep::TrackerHitSimTrackerHitLinkCollection const&),Gaudi::Functional::Traits::use_<> >] """,
    'OutputParticle2TrackRelationName' : """  [k4FWCore::details::MultiTransformer<std::tuple<edm4hep::TrackMCParticleLinkCollection> (edm4hep::TrackCollection const&,edm4hep::TrackerHitSimTrackerHitLinkCollection const&),Gaudi::Functional::Traits::use_<> >] """,
  }
  __declaration_location__ = 'TrackTruthAlg.cxx:15'
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TrackTruthAlg, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'ACTSTrackingPlugins'
  def getType( self ):
      return 'TrackTruthAlg'
  pass # class TrackTruthAlg
