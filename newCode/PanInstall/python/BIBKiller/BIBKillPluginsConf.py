#Tue Jun 10 12:36:08 2025"""Automatically generated. DO NOT EDIT please"""
from GaudiKernel.Proxy.Configurable import *

class BIBKiller( ConfigurableAlgorithm ) :
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
    'OutputTrackCollectionName' : [ 'BIBKilledTracks' ],
    'SideLength' : 0.900000,
    'PhiMax' : 3.14159,
    'LambdaMax' : 1.40000,
    'KeepOverflow' : True,
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
    'SideLength' : """ Side length of SoftKiller grid. [BIBKiller] """,
    'PhiMax' : """ Maximum allowed value of phi (absolute value). [BIBKiller] """,
    'LambdaMax' : """ Maximum allowed value of Lambda (absolute value). [BIBKiller] """,
    'KeepOverflow' : """ Should the algorithm keep or remove all overflow. [BIBKiller] """,
  }
  __declaration_location__ = 'BIBKiller.cxx:12'
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(BIBKiller, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'BIBKillPlugins'
  def getType( self ):
      return 'BIBKiller'
  pass # class BIBKiller

class BIBKillerCalo( ConfigurableAlgorithm ) :
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
    'InputBarrelCollections' : [ 'Barrel' ],
    'InputEndcapCollections' : [ 'Endcap' ],
    'OutputBarrelCollections' : [ 'BIBKilledBarrel' ],
    'OutputEndcapCollections' : [ 'BIBKilledEndcap' ],
    'SideLength' : 0.900000,
    'PhiMax' : 3.14159,
    'ThetaMax' : 1.57080,
    'ThetaMin' : 0.00000,
    'ThetaCenter' : 1.57080,
    'KeepOverflow' : True,
    'UsePt' : True,
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
    'InputBarrelCollections' : """  [k4FWCore::details::MultiTransformer<std::tuple<edm4hep::CalorimeterHitCollection,edm4hep::CalorimeterHitCollection> (std::vector<edm4hep::CalorimeterHitCollection const*,std::allocator<edm4hep::CalorimeterHitCollection const*> > const&,std::vector<edm4hep::CalorimeterHitCollection const*,std::allocator<edm4hep::CalorimeterHitCollection const*> > const&),Gaudi::Functional::Traits::use_<> >] """,
    'InputEndcapCollections' : """  [k4FWCore::details::MultiTransformer<std::tuple<edm4hep::CalorimeterHitCollection,edm4hep::CalorimeterHitCollection> (std::vector<edm4hep::CalorimeterHitCollection const*,std::allocator<edm4hep::CalorimeterHitCollection const*> > const&,std::vector<edm4hep::CalorimeterHitCollection const*,std::allocator<edm4hep::CalorimeterHitCollection const*> > const&),Gaudi::Functional::Traits::use_<> >] """,
    'OutputBarrelCollections' : """  [k4FWCore::details::MultiTransformer<std::tuple<edm4hep::CalorimeterHitCollection,edm4hep::CalorimeterHitCollection> (std::vector<edm4hep::CalorimeterHitCollection const*,std::allocator<edm4hep::CalorimeterHitCollection const*> > const&,std::vector<edm4hep::CalorimeterHitCollection const*,std::allocator<edm4hep::CalorimeterHitCollection const*> > const&),Gaudi::Functional::Traits::use_<> >] """,
    'OutputEndcapCollections' : """  [k4FWCore::details::MultiTransformer<std::tuple<edm4hep::CalorimeterHitCollection,edm4hep::CalorimeterHitCollection> (std::vector<edm4hep::CalorimeterHitCollection const*,std::allocator<edm4hep::CalorimeterHitCollection const*> > const&,std::vector<edm4hep::CalorimeterHitCollection const*,std::allocator<edm4hep::CalorimeterHitCollection const*> > const&),Gaudi::Functional::Traits::use_<> >] """,
    'SideLength' : """ Side length of SoftKiller grid. [BIBKillerCalo] """,
    'PhiMax' : """ Maximum allowed value of phi (absolute value). [BIBKillerCalo] """,
    'ThetaMax' : """ Maximum allowed value of Theta. (Up to Pi/2, will be mirrored) [BIBKillerCalo] """,
    'ThetaMin' : """ Minimum allowed value of Theta. [BIBKillerCalo] """,
    'ThetaCenter' : """ Value Theta is mirrored over (endcaps). [BIBKillerCalo] """,
    'KeepOverflow' : """ Should the algorithm keep or remove all overflow. [BIBKillerCalo] """,
    'UsePt' : """ Should the algorithm use pT or E as the variable. [BIBKillerCalo] """,
  }
  __declaration_location__ = 'BIBKillerCalo.cxx:9'
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(BIBKillerCalo, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'BIBKillPlugins'
  def getType( self ):
      return 'BIBKillerCalo'
  pass # class BIBKillerCalo

class BIBKillerCluster( ConfigurableAlgorithm ) :
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
    'InputClusterCollections' : [ 'Clusters' ],
    'OutputClusterCollections' : [ 'BIBKilledClusters' ],
    'SideLength' : 0.900000,
    'PhiMax' : 3.14159,
    'ThetaMax' : 3.14159,
    'KeepOverflow' : True,
    'UsePt' : True,
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
    'InputClusterCollections' : """  [k4FWCore::details::MultiTransformer<std::tuple<edm4hep::ClusterCollection> (edm4hep::ClusterCollection const&),Gaudi::Functional::Traits::use_<> >] """,
    'OutputClusterCollections' : """  [k4FWCore::details::MultiTransformer<std::tuple<edm4hep::ClusterCollection> (edm4hep::ClusterCollection const&),Gaudi::Functional::Traits::use_<> >] """,
    'SideLength' : """ Side length of SoftKiller grid. [BIBKillerCluster] """,
    'PhiMax' : """ Maximum allowed value of phi (absolute value). [BIBKillerCluster] """,
    'ThetaMax' : """ Maximum allowed value of Theta. [BIBKillerCluster] """,
    'KeepOverflow' : """ Should the algorithm keep or remove all overflow. [BIBKillerCluster] """,
    'UsePt' : """ Should the algorithm use pT or E as the variable. [BIBKillerCluster] """,
  }
  __declaration_location__ = 'BIBKillerCluster.cxx:9'
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(BIBKillerCluster, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'BIBKillPlugins'
  def getType( self ):
      return 'BIBKillerCluster'
  pass # class BIBKillerCluster

class BIBKillerTrackHit( ConfigurableAlgorithm ) :
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
    'InputBarrelCollections' : [ 'Barrel' ],
    'InputEndcapCollections' : [ 'Endcap' ],
    'OutputBarrelCollections' : [ 'BIBKilledBarrel' ],
    'OutputEndcapCollections' : [ 'BIBKilledEndcap' ],
    'SideLength' : 0.900000,
    'PhiMax' : 3.14159,
    'ThetaMax' : 3.14159,
    'KeepOverflow' : True,
    'UsePt' : True,
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
    'InputBarrelCollections' : """  [k4FWCore::details::MultiTransformer<std::tuple<edm4hep::TrackerHitPlaneCollection,edm4hep::TrackerHitPlaneCollection> (edm4hep::TrackerHitPlaneCollection const&,edm4hep::TrackerHitPlaneCollection const&),Gaudi::Functional::Traits::use_<> >] """,
    'InputEndcapCollections' : """  [k4FWCore::details::MultiTransformer<std::tuple<edm4hep::TrackerHitPlaneCollection,edm4hep::TrackerHitPlaneCollection> (edm4hep::TrackerHitPlaneCollection const&,edm4hep::TrackerHitPlaneCollection const&),Gaudi::Functional::Traits::use_<> >] """,
    'OutputBarrelCollections' : """  [k4FWCore::details::MultiTransformer<std::tuple<edm4hep::TrackerHitPlaneCollection,edm4hep::TrackerHitPlaneCollection> (edm4hep::TrackerHitPlaneCollection const&,edm4hep::TrackerHitPlaneCollection const&),Gaudi::Functional::Traits::use_<> >] """,
    'OutputEndcapCollections' : """  [k4FWCore::details::MultiTransformer<std::tuple<edm4hep::TrackerHitPlaneCollection,edm4hep::TrackerHitPlaneCollection> (edm4hep::TrackerHitPlaneCollection const&,edm4hep::TrackerHitPlaneCollection const&),Gaudi::Functional::Traits::use_<> >] """,
    'SideLength' : """ Side length of SoftKiller grid. [BIBKillerTrackHit] """,
    'PhiMax' : """ Maximum allowed value of phi (absolute value). [BIBKillerTrackHit] """,
    'ThetaMax' : """ Maximum allowed value of Theta. [BIBKillerTrackHit] """,
    'KeepOverflow' : """ Should the algorithm keep or remove all overflow. [BIBKillerTrackHit] """,
    'UsePt' : """ Should the algorithm use pT or E as the variable. [BIBKillerTrackHit] """,
  }
  __declaration_location__ = 'BIBKillerTrackHit.cxx:9'
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(BIBKillerTrackHit, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'BIBKillPlugins'
  def getType( self ):
      return 'BIBKillerTrackHit'
  pass # class BIBKillerTrackHit
