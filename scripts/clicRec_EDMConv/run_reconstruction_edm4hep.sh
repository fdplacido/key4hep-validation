# source /cvmfs/sw-nightlies.hsf.org/key4hep/setup.sh

if [ ! -d "output/edm4hep" ]; then
  mkdir output/edm4hep
fi

ln -s clicRec_e4h_input.py CLICPerformance/clicConfig/clicRec_e4h_input.py
cd CLICPerformance/clicConfig/

k4run ../../clicRec_e4h_input.py

cd ../../
