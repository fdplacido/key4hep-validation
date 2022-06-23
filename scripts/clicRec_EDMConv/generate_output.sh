# source /cvmfs/sw-nightlies.hsf.org/key4hep/setup.sh
source /cvmfs/sw.hsf.org/key4hep/setup.sh

git clone https://github.com/iLCSoft/CLICPerformance
cd CLICPerformance/clicConfig/

ddsim --steeringFile clic_steer.py \
      --compactFile $LCGEO/CLIC/compact/CLIC_o3_v14/CLIC_o3_v14.xml \
      --enableGun --gun.distribution uniform \
      --gun.particle mu- --gun.energy 10*GeV \
      --random.seed 123 --outputFile mu_10GeV.slcio \
      --numberOfEvents 10

ddsim --steeringFile clic_steer.py \
      --compactFile $LCGEO/CLIC/compact/CLIC_o3_v14/CLIC_o3_v14.xml \
      --enableGun --gun.distribution uniform \
      --gun.particle mu- \
      --gun.energy 10*GeV \
      --random.seed 123 \
      --outputFile mu_10GeV_edm4hep.root \
      --numberOfEvents 10