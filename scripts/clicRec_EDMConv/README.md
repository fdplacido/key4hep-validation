# Producing validation plots

1. Run simulations (ddsim) to produce slcio and edm4hep outputs with same parameters
2. Run reconstruction on both: one using Marlin, the other using key4hep with the EDM converters
3. Convert LCIO output to EDM4hep using converters
4. Produce plots comparing the converted LCIO and the EDM4hep outputs

```sh
sh generate_output.sh
sh run_reconstruction_slcio.sh
sh run_reconstruction_edm4hep.sh
sh convert_slcio.sh
python plotstuff.py
```