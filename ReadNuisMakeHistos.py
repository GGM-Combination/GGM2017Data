from ROOT import *

fdipho=open("DiPhoton/diphoton_T5Wg_datacard.txt", 'r')

fleppho=open("LeptonPhoton/datacard_LeptonPhoton.txt", 'r')
fSTbin=open("STbinnedPho/datacard_T5Wg_1400_1150.txt", 'r')
fHTbin=open("HTgammaPho/Wg_1350_1000.txt", 'r')

#Exclusive diphoton nuisances diEMPtWUnc ffshape ffstats ZggMCstat ZggXsecUnc Electron  Stat
ffShapeUnc=[]
diEMPtWUnc=[]
ffstatsLower=[]
ffstatsUpper=[]
ZggMCstat=[] # this is missing in the card
ZggXsecUnc=[]
EleFakePho_DiphoStat=[]
FakeRateUncDipho=[]#THis is correlated across all search bins
#bin 1-6
for line in fdipho:
	if "qcdShape" in line:
		line=line.replace(" ",'')		
		parse=line.split("-")
		print parse
		for p in parse:
			if "lnN" not in p and '\n' not in p and  p is not '':
				ffShapeUnc.append(p);
	if "diempt" in line:
		line=line.replace(" ",'')		
		parse=line.split("-")
		print parse
		for p in parse:
			if "lnN" not in p and '\n' not in p and  p is not '':
				diEMPtWUnc.append(p);
	if "zggErr" in line:
		line=line.replace(" ",'')		
		parse=line.split("-")
		print parse
		for p in parse:
			if "lnN" not in p and '\n' not in p and  p is not '':
				ZggXsecUnc.append(p);
	if "ewkStats" in line:
		line=line.replace(" ",'')		
		parse=line.split("-")
		print parse
		for p in parse:
			if "lnN" not in p and '\n' not in p and  p is not '':
				EleFakePho_DiphoStat.append(p);
	if "ewkFake" in line:
		line=line.replace(" ",'')		
		parse=line.split("-")
		print parse
		for p in parse:
			if "lnN" not in p and '\n' not in p and  p is not '':
				FakeRateUncDipho.append(p);
		
	if "qcdStats" in line:
                line=line.replace(" ",'')
                parse=line.split("-")
                print parse
                for p in parse:
                        if "lnN" not in p and '\n' not in p and  p is not '':
				Unc=p.split("/")
				print Unc
                                ffstatsLower.append(Unc[0]);
                                ffstatsUpper.append(Unc[1]);
FakeLeptonStatUnc=[]
FakeLeptonShapeUnc=[]
EleFakeRateUncleppho=[]
EleFakePhoStatUnc=[]
VgammaStatSingleLep=[]
RareSinglePhoBkgStat=[]
JetProxyStatUnc=[]# This is currently assigned as a gmN function

FakeRateUncLeppho=[]#THis is correlated across all search bins

#correlated with other Single Photon processes
VgammaShapeUnc=[] 
RareSinglePhoBkgXsecUnc=[]
JetPhotonFakeSystLeppho=[]
#bin 7-42
for line in fleppho:
	if "j_to_lep" in line:
		line=line.replace(" ",'')		
		parse=line.split("-")
		print parse
		for p in parse:
			if "lnN" not in p and '\n' not in p and  p is not '':
				FakeLeptonStatUnc.append(p);
	if "fakelep_shape" in line:
		line=line.replace(" ",'')		
		parse=line.split("-")
		print parse
		for p in parse:
			if "lnN" not in p and '\n' not in p and  p is not '':
				FakeLeptonShapeUnc.append(p);
	if "e_to_pho_syst" in line:
		line=line.replace(" ",'')		
		parse=line.split("-")
		print parse
		for p in parse:
			if "lnN" not in p and '\n' not in p and  p is not '':
				EleFakeRateUncleppho.append(p);
	if "e_to_pho_stat" in line:
		line=line.replace(" ",'')		
		parse=line.split("-")
		print parse
		for p in parse:
			if "lnN" not in p and '\n' not in p and  p is not '':
				EleFakePhoStatUnc.append(p);
	if "VGamma_stat" in line:
		line=line.replace(" ",'')		
		parse=line.split("-")
		print parse
		for p in parse:
			if "lnN" not in p and '\n' not in p and  p is not '':
				VgammaStatSingleLep.append(p);
	if "scale" in line:
		line=line.replace(" ",'')		
		parse=line.split("-")
		print parse
		for p in parse:
			if "lnN" not in p and '\n' not in p and  p is not '':
				VgammaShapeUnc.append(p);
	if "xs" in line:
		line=line.replace(" ",'')		
		parse=line.split("-")
		print parse
		for p in parse:
			if "lnN" not in p and '\n' not in p and  p is not '':
				RareSinglePhoBkgXsecUnc.append(p);
	
	if "rare_stat" in line:
		line=line.replace(" ",'')		
		parse=line.split("-")
		print parse
		for p in parse:
			if "lnN" not in p and '\n' not in p and  p is not '':
				RareSinglePhoBkgStat.append(p);
	if "j_to_pho_syst" in line:
		line=line.replace(" ",'')		
		parse=line.split("-")
		print parse
		for p in parse:
			if "lnN" not in p and '\n' not in p and  p is not '':
				JetPhotonFakeSystLeppho.append(p);
VgammaStatST=[]
tgStat=[] #This should be comined with diboson stat
VgammaShapeST=[]
JetPhotonFakeSystST=[]
EleFakeRateUncST=[]
EleFakePhoStatUncST=[]
JetFakeStatUncST=[]
#bin 43-46
for line in fSTbin:
	if "Vg_systematics" in line:
		line=line.replace(" ",'')		
		parse=line.split("-")
		print parse
		for p in parse:
			if "lnN" not in p and '\n' not in p and  p is not '':
				VgammaShapeST.append(p);
	if "GJ_systematics" in line:
		line=line.replace(" ",'')		
		parse=line.split("-")
		print parse
		for p in parse:
			if "lnN" not in p and '\n' not in p and  p is not '':
				JetPhotonFakeSystST.append(p);
	if "syst_efake" in line:
		line=line.replace(" ",'')
		line=line.replace("\n",'-')		
		parse=line.split("-")
		print parse
		for p in parse:
			if "lnN" not in p and '\n' not in p and  p is not '':
				EleFakeRateUncST.append(p);
	if "Vg" in line and "stat" in line:
                line=line.replace(" ",'')
                parse=line.split("-")
                print parse
                for p in parse:
                        if "lnN" not in p and '\n' not in p and  p is not '':
                                VgammaStatST.append(p);
	if "TTcomb" in line and "stat" in line:
                line=line.replace(" ",'')
                parse=line.split("-")
                print parse
                for p in parse:
                        if "lnN" not in p and '\n' not in p and  p is not '':
                                tgStat.append(p);
	if "efake" in line and "stat" in line:
                line=line.replace(" ",'')
		line=line.replace("\n",'-')
                parse=line.split("-")
                print parse
                for p in parse:
                        if "lnN" not in p and '\n' not in p and  p is not '':
                                EleFakePhoStatUncST.append(p);
	if "GJ" in line and "stat" in line:
                line=line.replace(" ",'')
                parse=line.split("-")
                print parse
                for p in parse:
                        if "lnN" not in p and '\n' not in p and  p is not '':
                                JetFakeStatUncST.append(p);
VgammaStatHT=[]#this should be combined from Wg and Zg
tgStatHT=[] #This should be comined with diboson stat
VgammaShapeHT=[]
JetPhotonFakeSystHT=[]
EleFakeRateUncHT=[]
EleFakePhoStatUncHT=[]
JetFakeStatUncHT=[]
#bin 47-52
for line in fHTbin:
	if "eleStat" in line:
		line=line.replace(" ",'')		
		parse=line.split("-")
		print parse
		for p in parse:
			if "lnN" not in p and '\n' not in p and  p is not '':
				EleFakePhoStatUncHT.append(p);
		
	if "syst_efake" in line:
		line=line.replace(" ",'')		
		parse=line.split("-")
		print parse
		for p in parse:
			if "lnN" not in p and '\n' not in p and  p is not '':
				EleFakeRateUncHT.append(p);
	if "wgStat" in line:
                line=line.replace(" ",'')
                parse=line.split("-")
                print parse
                for p in parse:
                        if "lnN" not in p and '\n' not in p and  p is not '':
                                VgammaStatHT.append(p);
	if "tgStat" in line and "stat" in line:
                line=line.replace(" ",'')
                parse=line.split("-")
                print parse
                for p in parse:
                        if "lnN" not in p and '\n' not in p and  p is not '':
                                tgStatHT.append(p);
	if "efake" in line and "stat" in line:
                line=line.replace(" ",'')
                parse=line.split("-")
                print parse
                for p in parse:
                        if "lnN" not in p and '\n' not in p and  p is not '':
                                EleFakePhoStatUncHT.append(p);
	if "gqcdStat" in line:
                line=line.replace(" ",'')
                parse=line.split("-")
                print parse
                for p in parse:
                        if "lnN" not in p and '\n' not in p and  p is not '':
                                JetFakeStatUncHT.append(p);
ffShapehisto=TH1D("ffShapehisto", "", 52, 1,53)
DiEmPthisto=TH1D("DiEmPthisto", "", 52, 1,53)
ffStatLowhisto=TH1D("ffStatLowhisto", "", 52, 1,53)
ffStatHighhisto=TH1D("ffStatHighhisto", "", 52, 1,53)
ZggStathisto=TH1D("ZggStathisto", "", 52, 1,53)
ZggUnchisto=TH1D("ZggUnchisto", "", 52, 1,53)
EleFakeRatehisto=TH1D("EleFakeRatehisto", "", 51,1,53);
for i in range(len(ffShapeUnc)):
        ffShapehisto.SetBinContent(i+1, float(ffShapeUnc[i]));
        ffShapehisto.GetXaxis().SetBinLabel(i+1,"ffshape");#correlated across dipho bins
        DiEmPthisto.SetBinContent(i+1,float(diEMPtWUnc[i]));
        DiEmPthisto.GetXaxis().SetBinLabel(i+1,"diEmPtWeight");#correlated across dipho bins
        ffStatLowhisto.SetBinContent(i+1,float(ffstatsLower[i]))
        ffStatLowhisto.GetXaxis().SetBinLabel(i+1,"ffstatUnc"+str(i));#uncorrelated across dipho bins
        ffStatHighhisto.SetBinContent(i+1,float(ffstatsUpper[i]));
        ffStatHighhisto.GetXaxis().SetBinLabel(i+1,"ffstatUnc"+str(i));#uncorrelated across dipho bins
        ZggUnchisto.SetBinContent(i+1, 1.5)
        ZggUnchisto.GetXaxis().SetBinLabel(i+1,"ZggxsecUnc");#correlated across dipho bins
        EleFakeRatehisto.SetBinContent(i+1, float(FakeRateUncDipho[i]))
        EleFakeRatehisto.GetXaxis().SetBinLabel(i+1,"EleFakeRateUnc");#correlated across all search bins

FakeLeptonShapehisto=TH1D("FakeLeptonShapehisto", "", 52, 1,53)
FakeLeptonStathisto=TH1D("FakeLeptonStathisto", "", 52, 1,53)
EleFakeStathisto=TH1D("EleFakeStathisto", "", 52, 1,53)
VgammaStathisto=TH1D("VgammaStathisto", "", 52, 1,53)
VgammaShapehisto=TH1D("VgammaShapehisto", "", 52, 1,53)
RareXsecUnchist=TH1D("RareXsecUnchist", "", 52, 1,53)
RareStatUnchist=TH1D("RareStatUnchist", "", 52, 1,53)
JetFakePhohisto=TH1D("JetFakePhohisto", "", 51,1,53);
print VgammaShapeUnc
for i in range(len(FakeLeptonShapeUnc)):
        EleFakeRatehisto.SetBinContent(i+7, float(EleFakeRateUncleppho[i]))
        EleFakeRatehisto.GetXaxis().SetBinLabel(i+7,"EleFakeRateUnc");#correlated across all search bins
        #EleFakeStathisto.SetBinContent(i+7, float( EleFakePhoStatUnc[i]));
        #EleFakeStathisto.GetXaxis().SetBinLabel(i+7,"EleFakeStat"+str(i+6));
        #FakeLeptonStathisto.SetBinContent(i+7,float(FakeLeptonStatUnc[i]));
        #FakeLeptonStathisto.GetXaxis().SetBinLabel(i+7,"FakeLeptonStat"+str(i+6));#uncorrelated across all search bins
        FakeLeptonShapehisto.SetBinContent(i+7, float(FakeLeptonShapeUnc[i]))
        FakeLeptonShapehisto.GetXaxis().SetBinLabel(i+7,"FakeLeptonShape");
        VgammaStathisto.SetBinContent(i+7, float(VgammaStatSingleLep[i]))
        VgammaStathisto.GetXaxis().SetBinLabel(i+7, "VGammaStat"+str(i+6));
        #VgammaShapehisto.SetBinContent(i+7, float(VgammaShapeUnc[i]))
        #VgammaShapehisto.GetXaxis().SetBinLabel(i+7,"VgammaShape")
        RareXsecUnchist.SetBinContent(i+7, float(RareSinglePhoBkgXsecUnc[i]));
        RareXsecUnchist.GetXaxis().SetBinLabel(i+7, "RareSinglePhoBkgXsec");
        RareStatUnchist.SetBinContent(i+7, float(RareSinglePhoBkgStat[i]));
        RareStatUnchist.GetXaxis().SetBinLabel(i+7, "RareSinglePhoBkgStat"+str(i+6));
        JetFakePhohisto.SetBinContent(i+7, float(JetPhotonFakeSystLeppho[i]));
        JetFakePhohisto.GetXaxis().SetBinLabel(i+7, "JetFakePhoSyst_SingleLep");
print EleFakePhoStatUncST
for i in range(len(VgammaShapeST)):
        EleFakeRatehisto.SetBinContent(i+43, 1.5)# float(EleFakeRateUncST[i]))
        EleFakeRatehisto.GetXaxis().SetBinLabel(i+43,"EleFakeRateUnc");#correlated across all search bins
        EleFakeStathisto.SetBinContent(i+43, float( EleFakePhoStatUncST[i]));
        EleFakeStathisto.GetXaxis().SetBinLabel(i+43,"EleFakeStat"+str(i+42));
        RareXsecUnchist.SetBinContent(i+43, 1.30);
        RareXsecUnchist.GetXaxis().SetBinLabel(i+43, "RareSinglePhoBkgXsec");
        RareStatUnchist.SetBinContent(i+43, float(tgStat[i]));
        RareStatUnchist.GetXaxis().SetBinLabel(i+43, "RareSinglePhoBkgStat"+str(i+42));
        VgammaStathisto.SetBinContent(i+43, float(VgammaStatST[i]))
        VgammaStathisto.GetXaxis().SetBinLabel(i+43, "VGammaStat"+str(i+42));
        VgammaShapehisto.SetBinContent(i+43, float(VgammaShapeST[i]))
        VgammaShapehisto.GetXaxis().SetBinLabel(i+43,"VgammaShape")
        JetFakePhohisto.SetBinContent(i+43, float(JetPhotonFakeSystST[i]));
        JetFakePhohisto.GetXaxis().SetBinLabel(i+43, "JetFakePhoSyst_ST");

for i in range(len(EleFakeRateUncHT)):
        EleFakeRatehisto.SetBinContent(i+47, float(EleFakeRateUncHT[i]))
        EleFakeRatehisto.GetXaxis().SetBinLabel(i+47,"EleFakeRateUnc");#correlated across all search bins
        EleFakeStathisto.SetBinContent(i+47, float( EleFakePhoStatUncHT[i]));
        EleFakeStathisto.GetXaxis().SetBinLabel(i+47,"EleFakeStat"+str(i+46));
        RareXsecUnchist.SetBinContent(i+47, 1.30);
        RareXsecUnchist.GetXaxis().SetBinLabel(i+47, "RareSinglePhoBkgXsec");
        RareStatUnchist.SetBinContent(i+47, float(tgStat[i]));
        RareStatUnchist.GetXaxis().SetBinLabel(i+47, "RareSinglePhoBkgStat"+str(i+46));
        VgammaStathisto.SetBinContent(i+47, float(VgammaStatHT[i]))
        VgammaStathisto.GetXaxis().SetBinLabel(i+47, "VGammaStat"+str(i+46));
        #VgammaShapehisto.SetBinContent(i+47, float(VgammaShapeHT[i]))
        #VgammaShapehisto.GetXaxis().SetBinLabel(i+47,"VgammaShape")
        JetFakePhohisto.SetBinContent(i+47, float(JetPhotonFakeSystHT[i]));
        JetFakePhohisto.GetXaxis().SetBinLabel(i+47, "JetFakePhoSyst_HT");
fout=TFile("NuisanceGGMCombination.root","RECREATE")
ffShapehisto.Write("ffShapehisto");
DiEmPthisto.Write("DiEmPthisto");
ffStatLowhisto.Write("ffStatLowhisto");
ffStatHighhisto.Write("ffStatHighhisto")
ZggStathisto.Write("ZggStathisto");
EleFakeRatehisto.Write("EleFakeRatehisto");
FakeLeptonShapehisto.Write("FakeLeptonShapehisto");
FakeLeptonStathisto.Write("FakeLeptonStathisto");
EleFakeStathisto.Write("EleFakeStathisto");
VgammaStathisto.Write("VgammaStathisto");
VgammaShapehisto.Write("VgammaShapehisto");
RareXsecUnchist.Write("RareXsecUnchist");
RareStatUnchist.Write("RareStatUnchist");
JetFakePhohisto.Write("JetFakePhohisto");
