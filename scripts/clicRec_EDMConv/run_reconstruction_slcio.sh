# source /cvmfs/sw-nightlies.hsf.org/key4hep/setup.sh

cd CLICPerformance/clicConfig/

convertMarlinSteeringToGaudi.py clicReconstruction.xml clicReconstruction.py

sed -i 's;read.Files = \[".*"\];read.Files = \["../../output/mu_10GeV.slcio"\];' clicReconstruction.py
# sed -i 's;EvtMax   = 10,;EvtMax   = 3,;' clicReconstruction.py
# sed -i 's;"MaxRecordNumber": ["10"],;"MaxRecordNumber": ["3"],;' clicReconstruction.py
sed -i 's;# algList.append(OverlayFalse);algList.append(OverlayFalse);' clicReconstruction.py
sed -i 's;# algList.append(MyConformalTracking);algList.append(MyConformalTracking);' clicReconstruction.py
sed -i 's;# algList.append(ClonesAndSplitTracksFinder);algList.append(ClonesAndSplitTracksFinder);' clicReconstruction.py
sed -i 's;# algList.append(RenameCollection);algList.append(RenameCollection);' clicReconstruction.py
sed -i 's;"DD4hepXMLFile": \[".*"\],; "DD4hepXMLFile": \[os.environ["LCGEO"]+"/CLIC/compact/CLIC_o3_v14/CLIC_o3_v14.xml"\],;' clicReconstruction.py

k4run clicReconstruction.py

cd ../../

mkdir output/slcio

mv CLICPerformance/clicConfig/Output_DST.slcio output/slcio/
mv CLICPerformance/clicConfig/Output_REC.slcio output/slcio/
