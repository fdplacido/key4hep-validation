# Producing validation plots

1. Run simulations (ddsim) to produce slcio and edm4hep outputs with same parameters
2. Run reconstruction on both: one using Marlin, the other using key4hep with the EDM converters
3. Convert LCIO output to EDM4hep using converters
4. Produce plots comparing the converted LCIO and the EDM4hep outputs

```sh
# 1. simulation
sh generate_output.sh
# 2. reconstruction
sh run_reconstruction_slcio.sh
sh run_reconstruction_edm4hep.sh
# 3. convert LCIO to EDM4hep
sh convert_slcio.sh
# 4. plot
python plotstuff.py
```