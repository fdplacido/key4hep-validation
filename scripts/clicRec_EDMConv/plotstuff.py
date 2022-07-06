import ROOT
from pathlib import Path

import os


def listdir_fullpath(d):
  return [os.path.join(d, f) for f in os.listdir(d)]


def read_chains(lcio_path, e4h_path, branch='events'):
  chain_lcio = ROOT.TChain(branch)
  chain_lcio.Add(lcio_path)


  chain_e4h = ROOT.TChain(branch)
  all_files_list = listdir_fullpath(e4h_path)
  for f in all_files_list:
    chain_e4h.Add(f)

  # infilename1 = "converted_slcio_rec_output.root"
  # infile1 = ROOT.TFile(infilename1, "READ")
  # tree1 = infile1.Get("events")
  # 
  # infilename2 = "clicRec_output_edm4hep.root"
  # infile2 = ROOT.TFile(infilename2, "READ")
  # tree2 = infile2.Get("events")

  return chain_lcio, chain_e4h


def print_structure(tree):

  # Show number of entries
  num_entries = tree.GetEntries()
  print(str(num_entries) + " entries")

  for event in tree:
  
    # print(event.GetName())
    
    # Print contents
    # print(event.ls())
    # Print available functions
    # print(dir(event))

    for branch in event.GetListOfBranches():
      print("\t" + branch.GetName())
      for entry in branch.GetListOfBranches():
        print("\t\t" + entry.GetName())
    # printing once is enough
    break


def plot_compare_branch(
  br_name, chain_lcio, chain_e4h,
  axis_name="", min_range=0, max_range=-1, n_bins=100,
  folder='plots', cv_name='c'):
  
  canvas = ROOT.TCanvas(cv_name)
  canvas.SetGrid()
  # canvas.SetLogy(True)

  h1name = "h1_%s" % br_name.replace("#","")
  chain_lcio.Draw(br_name + f" >> {h1name} ({n_bins}, {min_range}, {max_range})")
  # tree1.Draw(br_name + f" >> {h1name}")
  h1 = ROOT.gROOT.FindObject(h1name)
  h1.SetLineColor(ROOT.kRed)
  h1.SetLineWidth(2)
  h1.SetTitle("LCIO conv")

  h2name = "h2_%s" % br_name.replace("#","")
  chain_e4h.Draw(br_name + f" >> {h2name} ({n_bins}, {min_range}, {max_range})", "1", "same", nentries=990)
  # tree2.Draw(br_name + f" >> {h2name}", "1", "same")
  # tree2.Draw(br_name + " >> h2_%s" % br_name, "1", "same")
  h2 = ROOT.gROOT.FindObject(h2name)
  if isinstance(h2, ROOT.TH1):
    h2.SetLineColor(ROOT.kBlue)
    h2.SetTitle("EDM4hep")
    h2.SetLineStyle(2)
  
  # legend = ROOT.TLegend(0.1,0.7,0.2,0.9)
  # legend.SetBorderSize(0)
  # legend.SetFillColor(0)
  # legend.AddEntry(tree1, "LCIO", "f")
  # legend.AddEntry(tree2, "EDM4hep", "f")
  # legend.Draw()

  canvas.BuildLegend()
  
  Path(folder+"/png").mkdir(parents=True, exist_ok=True)
  Path(folder+"/pdf").mkdir(parents=True, exist_ok=True)
  
  # canvas.SaveAs(folder+"/png/"+br_name+".png")
  canvas.SaveAs(folder+"/pdf/"+br_name+".pdf")



def plot_all_branches(tree, chain_lcio, chain_e4h):
  # assume same branches in both?
  for event in tree:
    for branch in event.GetListOfBranches():
      for entry in branch.GetListOfBranches():
        plot_compare_branch(entry.GetName(), chain_lcio, chain_e4h, "all_plots")
    break 



def main():
  lcio_conv_file = "output/edm4hep/converted_slcio_rec_output.root"
  e4h_folder = "output/edm4hep/"
  chain_lcio, chain_e4h = read_chains(lcio_conv_file, e4h_folder)

  # print_structure(chain_lcio)

  # plot_all_branches(chain_lcio, chain_lcio, chain_e4h)

  # plot selected things
  plot_compare_branch("VXDTrackerHits.eDep", chain_lcio, chain_e4h, "X", 0, 0.0003)
  plot_compare_branch("VXDTrackerHits.time", chain_lcio, chain_e4h, "X", 0, 1.4)
  plot_compare_branch("VXDTrackerHits.type", chain_lcio, chain_e4h)
  plot_compare_branch("VXDTrackerHits.position.x", chain_lcio, chain_e4h)
  plot_compare_branch("VXDTrackerHits.position.y", chain_lcio, chain_e4h)
  plot_compare_branch("VXDTrackerHits.position.z", chain_lcio, chain_e4h)
  plot_compare_branch("VXDTrackerHits.type", chain_lcio, chain_e4h)

  plot_compare_branch("VertexJets.type", chain_lcio, chain_e4h)
  plot_compare_branch("VertexJets.mass", chain_lcio, chain_e4h)
  plot_compare_branch("VertexJets.energy", chain_lcio, chain_e4h)
  plot_compare_branch("VertexJets.momentum.x", chain_lcio, chain_e4h)
  plot_compare_branch("VertexJets.momentum.y", chain_lcio, chain_e4h)
  plot_compare_branch("VertexJets.momentum.z", chain_lcio, chain_e4h)

  plot_compare_branch("RefinedVertices.probability", chain_lcio, chain_e4h)
  plot_compare_branch("RefinedVertices.chi2", chain_lcio, chain_e4h)
  plot_compare_branch("RefinedVertices.position.x", chain_lcio, chain_e4h)
  plot_compare_branch("RefinedVertices.position.y", chain_lcio, chain_e4h)
  plot_compare_branch("RefinedVertices.position.z", chain_lcio, chain_e4h)

  plot_compare_branch("MUON.type", chain_lcio, chain_e4h)
  plot_compare_branch("MUON.time", chain_lcio, chain_e4h, "X", -0.02, 0.02)
  plot_compare_branch("MUON.position.x", chain_lcio, chain_e4h)
  plot_compare_branch("MUON.position.y", chain_lcio, chain_e4h)
  plot_compare_branch("MUON.position.z", chain_lcio, chain_e4h)
  plot_compare_branch("MUON.energy", chain_lcio, chain_e4h, "X", 0, 0.002)

  plot_compare_branch("InnerTrackerBarrelCollection.time", chain_lcio, chain_e4h)
  plot_compare_branch("InnerTrackerBarrelCollection.position.x", chain_lcio, chain_e4h)
  plot_compare_branch("InnerTrackerBarrelCollection.position.y", chain_lcio, chain_e4h)
  plot_compare_branch("InnerTrackerBarrelCollection.position.z", chain_lcio, chain_e4h)
  plot_compare_branch("InnerTrackerBarrelCollection.momentum.x", chain_lcio, chain_e4h, "X", -50, 50)
  plot_compare_branch("InnerTrackerBarrelCollection.momentum.y", chain_lcio, chain_e4h, "X", -50, 50)
  plot_compare_branch("InnerTrackerBarrelCollection.momentum.z", chain_lcio, chain_e4h, "X", -50, 50)  
  plot_compare_branch("InnerTrackerBarrelCollection.EDep", chain_lcio, chain_e4h, "X", 0, 0.002)

  plot_compare_branch("PandoraPFOs.type", chain_lcio, chain_e4h)
  plot_compare_branch("PandoraPFOs.energy", chain_lcio, chain_e4h, "X", 0, 50)
  plot_compare_branch("PandoraPFOs.momentum.x", chain_lcio, chain_e4h, "X", -50, 50)
  plot_compare_branch("PandoraPFOs.momentum.y", chain_lcio, chain_e4h, "X", -75, 75)
  plot_compare_branch("PandoraPFOs.momentum.z", chain_lcio, chain_e4h, "X", -80, 80)

  plot_compare_branch("ECALBarrel.type", chain_lcio, chain_e4h)
  plot_compare_branch("ECALBarrel.energy", chain_lcio, chain_e4h, "X", 0, 0.6)
  plot_compare_branch("ECALBarrel.time", chain_lcio, chain_e4h, "X", 0, 1.5)
  plot_compare_branch("ECALBarrel.position.x", chain_lcio, chain_e4h)
  plot_compare_branch("ECALBarrel.position.y", chain_lcio, chain_e4h)
  plot_compare_branch("ECALBarrel.position.z", chain_lcio, chain_e4h)

  plot_compare_branch("ECALEndcap.type", chain_lcio, chain_e4h)
  plot_compare_branch("ECALEndcap.energy", chain_lcio, chain_e4h, "X", 0, 0.4)
  plot_compare_branch("ECALEndcap.time", chain_lcio, chain_e4h, "X", 0, 2)
  plot_compare_branch("ECALEndcap.position.x", chain_lcio, chain_e4h)
  plot_compare_branch("ECALEndcap.position.y", chain_lcio, chain_e4h)
  plot_compare_branch("ECALEndcap.position.z", chain_lcio, chain_e4h)



if __name__ == "__main__":
    main()
