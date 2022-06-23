source /cvmfs/sw-nightlies.hsf.org/key4hep/setup.sh
# source /cvmfs/sw.hsf.org/key4hep/setup.sh

CLICPERF="CLICPerformance/clicConfig/"
if [ ! -d "$CLICPERF" ]; then
  git clone https://github.com/iLCSoft/CLICPerformance
fi

cd CLICPerformance/clicConfig/

STEERFILE="clic_steer.py"
COMPACTFILE="${LCGEO}/CLIC/compact/CLIC_o3_v14/CLIC_o3_v14.xml"
GUNDISTRIBUTION="uniform"
GUNPARTICLE="mu-"
GUNENERGY="10*GeV"
RANDOMSEED=123
NUMEVENTS=10

ddsim --steeringFile $STEERFILE \
      --compactFile $COMPACTFILE \
      --enableGun --gun.distribution $GUNDISTRIBUTION \
      --gun.particle $GUNPARTICLE --gun.energy $GUNENERGY \
      --random.seed $RANDOMSEED --outputFile mu_10GeV.slcio \
      --numberOfEvents $NUMEVENTS

ddsim --steeringFile $STEERFILE \
      --compactFile $COMPACTFILE \
      --enableGun --gun.distribution $GUNDISTRIBUTION \
      --gun.particle $GUNPARTICLE --gun.energy $GUNENERGY \
      --random.seed $RANDOMSEED --outputFile mu_10GeV_edm4hep.root \
      --numberOfEvents $NUMEVENTS


cd ../../

OUTPUTDIR="output"
if [ ! -d "$OUTPUTDIR" ]; then
  mkdir output
fi


mv CLICPerformance/clicConfig/mu_10GeV.slcio ./output/
mv CLICPerformance/clicConfig/mu_10GeV_edm4hep.root ./output/
