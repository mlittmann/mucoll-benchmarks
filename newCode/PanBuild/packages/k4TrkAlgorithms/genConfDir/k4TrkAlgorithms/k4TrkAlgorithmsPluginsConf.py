#Tue Jun 10 12:36:03 2025"""Automatically generated. DO NOT EDIT please"""
from GaudiKernel.Proxy.Configurable import *

class DDPlanarDigiAlgorithm( ConfigurableAlgorithm ) :
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
    'SimTrackHitCollectionName' : [ 'VXDCollection' ],
    'TrackerHitCollectionName' : [ 'VTXTrackerHits' ],
    'SimTrkHitRelCollection' : [ 'VTXTrackerHitRelations' ],
    'ResolutionU' : [ 0.00400000 ],
    'ResolutionV' : [ 0.00400000 ],
    'ResolutionT' : [ -1.00000 ],
    'IsStrip' : False,
    'SubDetectorName' : 'VXD',
    'ForceHitsOntoSurface' : False,
    'MinimumEnergyPerHit' : 0.0000000,
    'CorrectTimesForPropagation' : False,
    'UseTimeWindow' : False,
    'TimeWindowMin' : [ -1.00000e+09 ],
    'TimeWindowMax' : [ 1.00000e+09 ],
    'EncodingStringParameterName' : 'GlobalTrackerReadoutID',
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
    'SimTrackHitCollectionName' : """  [k4FWCore::details::MultiTransformer<std::tuple<edm4hep::TrackerHitPlaneCollection,edm4hep::TrackerHitSimTrackerHitLinkCollection> (edm4hep::SimTrackerHitCollection const&),Gaudi::Functional::Traits::use_<> >] """,
    'TrackerHitCollectionName' : """  [k4FWCore::details::MultiTransformer<std::tuple<edm4hep::TrackerHitPlaneCollection,edm4hep::TrackerHitSimTrackerHitLinkCollection> (edm4hep::SimTrackerHitCollection const&),Gaudi::Functional::Traits::use_<> >] """,
    'SimTrkHitRelCollection' : """  [k4FWCore::details::MultiTransformer<std::tuple<edm4hep::TrackerHitPlaneCollection,edm4hep::TrackerHitSimTrackerHitLinkCollection> (edm4hep::SimTrackerHitCollection const&),Gaudi::Functional::Traits::use_<> >] """,
    'ResolutionU' : """ Resolution in direction of u - either one per layer or one for all layers. [DDPlanarDigiAlgorithm] """,
    'ResolutionV' : """ Resolution in direction of u - either one per layer or one for all layers. [DDPlanarDigiAlgorithm] """,
    'ResolutionT' : """ Resolution of time - either one per layer or one for all layers. If the single entry is negative, disable time smearing. [DDPlanarDigiAlgorithm] """,
    'IsStrip' : """ Whether hits are 1D strip hits. [DDPlanarDigiAlgorithm] """,
    'SubDetectorName' : """ Name of sub detector. [DDPlanarDigiAlgorithm] """,
    'ForceHitsOntoSurface' : """ Project hits onto the surface in case they are not yet on the surface (default: false). [DDPlanarDigiAlgorithm] """,
    'MinimumEnergyPerHit' : """ Minimum Energy (in GeV!) to accept hits, other hits are ignored. [DDPlanarDigiAlgorithm] """,
    'CorrectTimesForPropagation' : """ Correct hit time for the propagation: radial distance/c (default: false). [DDPlanarDigiAlgorithm] """,
    'UseTimeWindow' : """ Only accept hits with time (after smearing) within the specified time window (default: false). [DDPlanarDigiAlgorithm] """,
    'TimeWindowMin' : """ Minimum time a hit must have after smearing to be accepted [ns] - either one per layer or one for all layers. [DDPlanarDigiAlgorithm] """,
    'TimeWindowMax' : """ Maximum time a hit must have after smearing to be accepted [ns] - either one per layer or one for all layers. [DDPlanarDigiAlgorithm] """,
    'EncodingStringParameterName' : """ The name of the DD4hep constant that contains the Encoding string for the detector [DDPlanarDigiAlgorithm] """,
  }
  __declaration_location__ = 'DDPlanarDigiAlgorithm.cc:29'
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(DDPlanarDigiAlgorithm, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'k4TrkAlgorithmsPlugins'
  def getType( self ):
      return 'DDPlanarDigiAlgorithm'
  pass # class DDPlanarDigiAlgorithm
