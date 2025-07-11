#Tue Jun 10 12:36:05 2025"""Automatically generated. DO NOT EDIT please"""
from GaudiKernel.Proxy.Configurable import *

class TrackPerfHistAlg( ConfigurableAlgorithm ) :
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
    'InputMCParticleCollectionName' : [ 'MCParticle' ],
    'InputTrackCollectionName' : [ 'Tracks' ],
    'InputMCTrackRelationCollectionName' : [ 'MCTrackRelations' ],
    'MatchProb' : 0.500000,
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
    'InputMCParticleCollectionName' : """  [k4FWCore::details::Consumer<void (edm4hep::MCParticleCollection const&,edm4hep::TrackCollection const&,edm4hep::TrackMCParticleLinkCollection const&),Gaudi::Functional::Traits::use_<> >] """,
    'InputTrackCollectionName' : """  [k4FWCore::details::Consumer<void (edm4hep::MCParticleCollection const&,edm4hep::TrackCollection const&,edm4hep::TrackMCParticleLinkCollection const&),Gaudi::Functional::Traits::use_<> >] """,
    'InputMCTrackRelationCollectionName' : """  [k4FWCore::details::Consumer<void (edm4hep::MCParticleCollection const&,edm4hep::TrackCollection const&,edm4hep::TrackMCParticleLinkCollection const&),Gaudi::Functional::Traits::use_<> >] """,
    'MatchProb' : """ Minimum matching probability to be considered a good track-MC match. [TrackPerfHistAlg] """,
  }
  __declaration_location__ = 'TrackPerfHistAlg.cxx:21'
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TrackPerfHistAlg, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'TrackPerfPlugins'
  def getType( self ):
      return 'TrackPerfHistAlg'
  pass # class TrackPerfHistAlg
