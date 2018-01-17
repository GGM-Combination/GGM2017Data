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

