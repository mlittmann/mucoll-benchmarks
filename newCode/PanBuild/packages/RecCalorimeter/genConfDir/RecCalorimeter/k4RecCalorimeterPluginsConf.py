#Tue Jun 10 12:36:17 2025"""Automatically generated. DO NOT EDIT please"""
from GaudiKernel.Proxy.Configurable import *

class CreateCaloJet( ConfigurableAlgorithm ) :
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
    'InputClusterCollection' : [ 'CorrectedCaloClusters' ],
    'OutputJetCollection' : [ 'Jets' ],
    'JetAlg' : 'antikt',
    'JetRadius' : 0.40000000,
    'MinPt' : 10.000000,
    'IsExclusiveClustering' : 0,
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
    'InputClusterCollection' : """  [k4FWCore::details::Transformer<edm4hep::ReconstructedParticleCollection (edm4hep::ClusterCollection const&),Gaudi::Functional::Traits::use_<> >] """,
    'OutputJetCollection' : """  [k4FWCore::details::Transformer<edm4hep::ReconstructedParticleCollection (edm4hep::ClusterCollection const&),Gaudi::Functional::Traits::use_<> >] """,
    'JetAlg' : """ Name of jet clustering algorithm [CreateCaloJet] """,
    'JetRadius' : """ Jet clustering radius [CreateCaloJet] """,
    'MinPt' : """ Minimum pT for saved jets [CreateCaloJet] """,
    'IsExclusiveClustering' : """ 1 if exclusive, 0 if inclusive [CreateCaloJet] """,
  }
  __declaration_location__ = 'CreateCaloJet.cpp:114'
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(CreateCaloJet, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'k4RecCalorimeterPlugins'
  def getType( self ):
      return 'CreateCaloJet'
  pass # class CreateCaloJet

class CreateTruthJet( ConfigurableAlgorithm ) :
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
    'InputMCParticleCollection' : [ 'MCParticles' ],
    'OutputJetCollection' : [ 'TruthJets' ],
    'OutputAssociationsCollection' : [ 'TruthJetParticleAssociations' ],
    'JetAlg' : 'antikt',
    'JetRadius' : 0.40000000,
    'MinPt' : 1.0000000,
    'isExclusiveClustering' : False,
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
    'InputMCParticleCollection' : """  [k4FWCore::details::MultiTransformer<std::tuple<edm4hep::ReconstructedParticleCollection,edm4hep::RecoMCParticleLinkCollection> (edm4hep::MCParticleCollection const&),Gaudi::Functional::Traits::use_<> >] """,
    'OutputJetCollection' : """  [k4FWCore::details::MultiTransformer<std::tuple<edm4hep::ReconstructedParticleCollection,edm4hep::RecoMCParticleLinkCollection> (edm4hep::MCParticleCollection const&),Gaudi::Functional::Traits::use_<> >] """,
    'OutputAssociationsCollection' : """  [k4FWCore::details::MultiTransformer<std::tuple<edm4hep::ReconstructedParticleCollection,edm4hep::RecoMCParticleLinkCollection> (edm4hep::MCParticleCollection const&),Gaudi::Functional::Traits::use_<> >] """,
    'JetAlg' : """ Name of jet clustering algorithm [CreateTruthJet] """,
    'JetRadius' : """ Jet clustering radius [CreateTruthJet] """,
    'MinPt' : """ Minimum pT for saved jets [CreateTruthJet] """,
    'isExclusiveClustering' : """ true if exclusive, false if inclusive [CreateTruthJet] """,
  }
  __declaration_location__ = 'CreateTruthJet.cpp:112'
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(CreateTruthJet, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'k4RecCalorimeterPlugins'
  def getType( self ):
      return 'CreateTruthJet'
  pass # class CreateTruthJet
