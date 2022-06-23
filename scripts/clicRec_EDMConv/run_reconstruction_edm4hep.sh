# source /cvmfs/sw-nightlies.hsf.org/key4hep/setup.sh

cp clicRec_e4h_input.py CLICPerformance/clicConfig/

cd CLICPerformance/clicConfig/

k4run ../../clicRec_e4h_input.py

rm clicRec_e4h_input.py
