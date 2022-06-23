from Gaudi.Configuration import *

from Configurables import k4DataSvc, MarlinProcessorWrapper
from Configurables import ToolSvc, Lcio2EDM4hepTool
from Configurables import LcioEvent

evtsvc = k4DataSvc('EventDataSvc')
algList = []

read = LcioEvent()
read.OutputLevel = WARNING
read.Files = ["output/slcio/Output_REC.slcio"]



MyAIDAProcessor = MarlinProcessorWrapper("MyAIDAProcessor")
MyAIDAProcessor.OutputLevel = WARNING
MyAIDAProcessor.ProcessorType = "AIDAProcessor"
MyAIDAProcessor.Parameters = {
                              "Compress": ["1"],
                              "FileName": ["output/histograms"],
                              "FileType": ["root"]
                              }


AllOutputConv = Lcio2EDM4hepTool("AllOutputConv")
AllOutputConv.Parameters = [
  "BuildUpVertices", "BuildUpVertices",
  "BuildUpVertices_RP", "BuildUpVertices_RP",
  "BuildUpVertices_V0", "BuildUpVertices_V0",
  "BuildUpVertices_V0_RP", "BuildUpVertices_V0_RP",
  "CalohitMCTruthLink", "CalohitMCTruthLink",
  "ClusterMCTruthLink", "ClusterMCTruthLink",
  "DebugHits", "DebugHits",
  "ECALBarrel", "ECALBarrel",
  "ECALEndcap", "ECALEndcap",
  "ECALOther", "ECALOther",
  "ECalBarrelCollection", "ECalBarrelCollection",
  "ECalEndcapCollection", "ECalEndcapCollection",
  "ECalPlugCollection", "ECalPlugCollection",
  "HCALBarrel", "HCALBarrel",
  "HCALEndcap", "HCALEndcap",
  "HCALOther", "HCALOther",
  "HCalBarrelCollection", "HCalBarrelCollection",
  "HCalEndcapCollection", "HCalEndcapCollection",
  "HCalRingCollection", "HCalRingCollection",
  "ITrackerEndcapHits", "ITrackerEndcapHits",
  "ITrackerHits", "ITrackerHits",
  "InnerTrackerBarrelCollection", "InnerTrackerBarrelCollection",
  "InnerTrackerBarrelHitsRelations", "InnerTrackerBarrelHitsRelations",
  "InnerTrackerEndcapCollection", "InnerTrackerEndcapCollection",
  "InnerTrackerEndcapHitsRelations", "InnerTrackerEndcapHitsRelations",
  "LE_LooseSelectedPandoraPFOs", "LE_LooseSelectedPandoraPFOs",
  "LE_SelectedPandoraPFOs", "LE_SelectedPandoraPFOs",
  "LE_TightSelectedPandoraPFOs", "LE_TightSelectedPandoraPFOs",
  "LooseSelectedPandoraPFOs", "LooseSelectedPandoraPFOs",
  "LumiCalClusters", "LumiCalClusters",
  "LumiCalCollection", "LumiCalCollection",
  "LumiCalRecoParticles", "LumiCalRecoParticles",
  "LumiCal_Hits", "LumiCal_Hits",
  "MCParticles", "MCParticles",
  "MCParticlesSkimmed", "MCParticlesSkimmed",
  "MCPhysicsParticles", "MCPhysicsParticles",
  "MUON", "MUON",
  "MergedClusters", "MergedClusters",
  "MergedRecoParticles", "MergedRecoParticles",
  "OTrackerEndcapHits", "OTrackerEndcapHits",
  "OTrackerHits", "OTrackerHits",
  "OuterTrackerBarrelCollection", "OuterTrackerBarrelCollection",
  "OuterTrackerBarrelHitsRelations", "OuterTrackerBarrelHitsRelations",
  "OuterTrackerEndcapCollection", "OuterTrackerEndcapCollection",
  "OuterTrackerEndcapHitsRelations", "OuterTrackerEndcapHitsRelations",
  "PFOsFromJets", "PFOsFromJets",
  "PandoraClusters", "PandoraClusters",
  "PandoraPFOs", "PandoraPFOs",
  "PandoraStartVertices", "PandoraStartVertices",
  "PrimaryVertices", "PrimaryVertices",
  "PrimaryVertices_RP", "PrimaryVertices_RP",
  "RecoMCTruthLink", "RecoMCTruthLink",
  "RefinedVertexJets", "RefinedVertexJets",
  "RefinedVertexJets_rel", "RefinedVertexJets_rel",
  "RefinedVertexJets_vtx", "RefinedVertexJets_vtx",
  "RefinedVertexJets_vtx_RP", "RefinedVertexJets_vtx_RP",
  "RefinedVertices", "RefinedVertices",
  "RefinedVertices_RP", "RefinedVertices_RP",
  "RelationCaloHit", "RelationCaloHit",
  "RelationMuonHit", "RelationMuonHit",
  "SelectedPandoraPFOs", "SelectedPandoraPFOs",
  "SiTracks", "SiTracks",
  "SiTracksCT", "SiTracksCT",
  "SiTracksMCTruthLink", "SiTracksMCTruthLink",
  "SiTracks_Refitted", "SiTracks_Refitted",
  "TightSelectedPandoraPFOs", "TightSelectedPandoraPFOs",
  "VXDEndcapTrackerHitRelations", "VXDEndcapTrackerHitRelations",
  "VXDEndcapTrackerHits", "VXDEndcapTrackerHits",
  "VXDTrackerHitRelations", "VXDTrackerHitRelations",
  "VXDTrackerHits", "VXDTrackerHits",
  "VertexBarrelCollection", "VertexBarrelCollection",
  "VertexEndcapCollection", "VertexEndcapCollection",
  "VertexJets", "VertexJets",
  "YokeBarrelCollection", "YokeBarrelCollection",
  "YokeEndcapCollection", "YokeEndcapCollection",
]
AllOutputConv.OutputLevel = DEBUG

MyAIDAProcessor.Lcio2EDM4hepTool = AllOutputConv



from Configurables import PodioOutput
out = PodioOutput("PodioOutput", filename = "output/edm4hep/converted_slcio_rec_output.root")
out.outputCommands = ["keep *"]


algList.append(read)
algList.append(MyAIDAProcessor)
algList.append(out)

from Configurables import ApplicationMgr
ApplicationMgr( TopAlg = algList,
                EvtSel = 'NONE',
                EvtMax = 10,
                ExtSvc = [evtsvc],
                OutputLevel=WARNING)

