from ROOT import *
import mmap
import os
fsinglelepton=open("GGM2017Data/LeptonPhoton/datacard_LeptonPhoton.txt", "read")
fdiphoton=open("GGM2017Data/DiPhoton/diphoton_T5Wg_datacard.txt", "read")
fHTGamma=open("GGM2017Data/HTgammaPho/Wg_900_700.txt","read");
fSTBinned=open("GGM2017Data/STbinnedPho/datacard_T5Wg_1550_300.txt", "read")

#replace this with signal ntuple for GGM Scan
SingleLeptonSignal=TFile("GGM2017Data/LeptonPhoton/signalTree_T5WG.root", "READ")
observationsSTbinned=[]
BackgroundPredictionsST=[]
for line in fSTBinned:
        if "observation" in line:
		stripline=line.rstrip('\n').lstrip("observation");
                parse=stripline.split(" ");
		for p in parse:
                        if p is not '':
                                observationsSTbinned.append(int(p));
        if "rate" in line:
                stripline=line.rstrip('\n').lstrip("rate");
                parse=stripline.split(" ");
                for p in parse:
                        if p is not '' and p is not "rate" :
                                BackgroundPredictionsST.append(float(p));
				#skip signal for now
observationsHTgammabinned=[]
BackgroundPredictionsHTgamma=[]
for line in fHTGamma:
        if "observation" in line:
		stripline=line.rstrip('\n').lstrip("observation");
                parse=stripline.split(" ");
		for p in parse:
                        if p is not '':
                                observationsHTgammabinned.append(int(p));
        if "rate" in line:
                stripline=line.rstrip('\n').lstrip("rate");
                parse=stripline.split(" ");
                for p in parse:
                        if p is not '' and p.find("rate")==-1:
                                BackgroundPredictionsHTgamma.append(float(p));
				#skip signal for now

observationsSingleLepton=[]
BackgroundPredictionsSingleLepton=[]
for line in fsinglelepton:
	if "observation" in line:
		stripline=line.rstrip('\n').lstrip("observation");
		parse=stripline.split(" ");
		for p in parse:
			if p is not '':
				observationsSingleLepton.append(int(p));
	if "rate" in line:
		stripline=line.rstrip('\n').lstrip("rate");
                parse=stripline.split(" ");
		for p in parse:
			if p is not '' and "NSC" not in p:
				BackgroundPredictionsSingleLepton.append(float(p));

observationsDiphoton=[]
BackgroundPredictionsDiphoton=[]
for line in fdiphoton:
	if "observation" in line:
		stripline=line.rstrip('\n').lstrip("observation");
		parse=stripline.split(" ");
		for p in parse:
			if p is not '':
				observationsDiphoton.append(int(p))			
	if "rate" in line:
		stripline=line.rstrip('\n').lstrip("rate");
                parse=stripline.split(" ");
		for p in parse:
			if p is not '' and "T5GG" not in p:
				BackgroundPredictionsDiphoton.append(float(p));
searchbin=0;
listOfBkgs=['qcdfakefake','elefakepho','Zgammagamma','jetfakepho','qcdfakelep','Vgamma','rareSnglPho',]
dictBkgPredictions={}
for i in range(len(BackgroundPredictionsDiphoton)):
	if i%3==0:
	        #diphoton bkgs have no contribution from single photon bkgs
		bkgline="%g %g %g 0 0 0 0" %(BackgroundPredictionsDiphoton[i], BackgroundPredictionsDiphoton[i+1], BackgroundPredictionsDiphoton[i+2])
		dictBkgPredictions[searchbin]=bkgline;			
		searchbin=searchbin+1
for i in range(len(BackgroundPredictionsSingleLepton)):
	if i%5==0:
	        #diphoton bkgs have no contribution from single photon bkgs
		bkgline="0 %g 0 %g %g %g %g" %(BackgroundPredictionsSingleLepton[i], BackgroundPredictionsSingleLepton[i+1], BackgroundPredictionsSingleLepton[i+2], BackgroundPredictionsSingleLepton[i+3], BackgroundPredictionsSingleLepton[i+4])
		dictBkgPredictions[searchbin]=bkgline;			
		searchbin=searchbin+1
for i in range(len(BackgroundPredictionsST)):
		bkgline="0 %g 0 %g 0 %g %g " %(BackgroundPredictionsST[5], BackgroundPredictionsST[1],BackgroundPredictionsST[3], BackgroundPredictionsST[2]+BackgroundPredictionsST[4] )
		dictBkgPredictions[searchbin]=bkgline;			
		searchbin=searchbin+1
for i in range(len(BackgroundPredictionsHTgamma)):
		bkgline="0 %g 0 %g 0 %g %g " %(BackgroundPredictionsST[4], BackgroundPredictionsST[3],BackgroundPredictionsST[0]+BackgroundPredictionsST[2], BackgroundPredictionsST[5] )
		dictBkgPredictions[searchbin]=bkgline;			
		searchbin=searchbin+1

#replace with observations from the cards
#observationsSingleLepton=[309, 494, 85, 32, 64, 45,1,1,5,12,23,20,4,12,7,1,1,0, 153,277,67, 32,46,32,1,1,4,10,21,14,6,9,4,0,1,3]
#Legend: Fake-Fake bkg for diphoton, W->electron nu in W and WW events, (rare) Zgammagamma bkg,  Single photon fakes, Zgamma and Wgamma bkgs, WW(ZW)gamma +ttGamma bkgs 

# bin order diphoton, single photon, photon+lepton
binlabels=[]
for i in range(len(observationsDiphoton)):
	binlabels.append("diphotonMETbin%d" %i);
for i in range(len(observationsSingleLepton)/2):
	binlabels.append("MuGammaBin%d" %i);
for i in range(len(observationsSingleLepton)/2):
	binlabels.append("EleGammaBin%d" %i);
for i in range(len(observationsSTbinned)):
	binlabels.append("STBin%d" %i);
for i in range(len(observationsHTgammabinned)):
	binlabels.append("HTgammaBin%d" %i);
searchbincount=0;
for b in binlabels:
	print searchbincount
	fcardOut=open("GGMCombinationTemplateBin_%s.txt" %b, 'w');
	fcardOut.write("imax 1 number of channels \n" )
	fcardOut.write("jmax %d number of backgrounds\n" %(len(listOfBkgs)));
	fcardOut.write("kmax *\n");
	fcardOut.write("------------\n");
	fcardOut.write("bin ");
	fcardOut.write(" %s" %b)
	fcardOut.write("\n") 
	fcardOut.write("observation ");
	if searchbincount<len(observationsDiphoton):fcardOut.write(" %d " %observationsDiphoton[searchbincount]);
        if searchbincount>=len(observationsDiphoton) and searchbincount<42:fcardOut.write(" %d " %observationsSingleLepton[searchbincount-len(observationsDiphoton)]);
	if searchbincount>=42 and searchbincount<46:
		fcardOut.write(" %d " %observationsSTbinned[searchbincount-42])
	if searchbincount>=46:fcardOut.write(" %d " %observationsHTgammabinned[searchbincount-46])
	fcardOut.write('\n')
	fcardOut.write("bin ")
	processstring=""
	for i in range(len(listOfBkgs)+1):processstring=processstring+"%s " %b
	fcardOut.write(processstring);
	fcardOut.write('\n')
	fcardOut.write("process ")
	processstring="GGMModel "
	for i in range(len(listOfBkgs)):processstring=processstring+"%s " %listOfBkgs[i]
	fcardOut.write(processstring);
	fcardOut.write('\n')
	fcardOut.write("process ")
	processstring=""
	for i in range(len(listOfBkgs)+1):processstring=processstring+"%d " %i
	fcardOut.write(processstring);
	fcardOut.write('\n')
	fcardOut.write("rate GGMSig ")# will replace this by reading signal histos
	#print dictBkgPredictions[searchbincount]
        fcardOut.write(dictBkgPredictions[searchbincount]);
	fcardOut.close()
	searchbincount=searchbincount+1
	
#Fill Signal Model : 
testPath=os.getcwd()+"/T5WgTestCards"
if not os.path.isdir(testPath):os.mkdir(testPath);
##HERE YOU WOULD Fill the signal in the diphoton region

##HERE YOU FILL SIGNAL MODELS FOR the Photon+Lepton region
for i in range(len(observationsDiphoton)):
	T5WgSignalLeptonMap=SingleLeptonSignal.Get("h_chan%d_rate_nom" %(i+1));
	if not os.path.isdir(testPath):os.mkdir(testPath);
        for ix in range(1,T5WgSignalLeptonMap.GetNbinsX() + 1):
		for ij in range(1,T5WgSignalLeptonMap.GetNbinsY() + 1):
			M1=T5WgSignalLeptonMap.GetXaxis().GetBinCenter(ix);
			M2=T5WgSignalLeptonMap.GetYaxis().GetBinCenter(ij);
			if M1!=800 or M2!=600:continue
			DeltaM=M1-M2
			SignalYield=T5WgSignalLeptonMap.GetBinContent(ix,ij);
			if M1-M2<0 or SignalYield<0:continue
			SignalPath=os.getcwd()+"/T5WgTestCards/T5Wg_Mgo%d_MLSP%d" %(M1,M2)
			if not os.path.isdir(SignalPath):os.mkdir(SignalPath);
			M1=T5WgSignalLeptonMap.GetXaxis().GetBinCenter(ix);
			M2=T5WgSignalLeptonMap.GetYaxis().GetBinCenter(ij);
			fdiphoOut=open('%s/GGMCombination_M1_%d_M2_%d_diphotonBin%d.txt' %(SignalPath,M1,M2,i),'w')
			ftemplate=open("GGMCombinationTemplateBin_diphotonMETbin%d.txt" %i, 'r')
			for line in ftemplate:
				line=line.replace("GGMSig", "0.0" )
				fdiphoOut.write(line);
			fdiphoOut.close();
			ftemplate.close();
for i in range(len(observationsSingleLepton)):
	T5WgSignalLeptonMap=SingleLeptonSignal.Get("h_chan%d_rate_nom" %(i+1));
	if not os.path.isdir(testPath):os.mkdir(testPath);
        for ix in range(1,T5WgSignalLeptonMap.GetNbinsX() + 1):
		for ij in range(1,T5WgSignalLeptonMap.GetNbinsY() + 1):
			M1=T5WgSignalLeptonMap.GetXaxis().GetBinCenter(ix);
			M2=T5WgSignalLeptonMap.GetYaxis().GetBinCenter(ij);
			if M1!=800 or M2!=600:continue
			DeltaM=M1-M2
			SignalYield=T5WgSignalLeptonMap.GetBinContent(ix,ij);
			if i<18:
				feleOut=open('%s/GGMCombination_M1_%d_M2_%d_EleGammaBin%d.txt' %(SignalPath,M1,M2,i),'w')
				ftemplate=open("GGMCombinationTemplateBin_EleGammaBin%d.txt" %i, 'r')
				#print "GGMCombinationTemplateBin_EleGammaBin%d.txt" %i
				for line in ftemplate:
					line=line.replace("GGMSig", "%.4f" %SignalYield)
					feleOut.write(line);
				feleOut.close();
				ftemplate.close();
			else:
				fmuOut=open('%s/GGMCombination_M1_%d_M2_%d_MuGammaBin%d.txt' %(SignalPath,M1,M2,i-18),'w')
				ftemplate=open("GGMCombinationTemplateBin_MuGammaBin%d.txt" %(i-18), 'r')
				for line in ftemplate:
					line=line.replace("GGMSig", "%.4f" %SignalYield)
					fmuOut.write(line);
				fmuOut.close()
				ftemplate.close();
for i in range(len(observationsSTbinned)):
	T5WgSignalLeptonMap=SingleLeptonSignal.Get("h_chan%d_rate_nom" %(i+1));
	if not os.path.isdir(testPath):os.mkdir(testPath);
        for ix in range(1,T5WgSignalLeptonMap.GetNbinsX() + 1):
		for ij in range(1,T5WgSignalLeptonMap.GetNbinsY() + 1):
			M1=T5WgSignalLeptonMap.GetXaxis().GetBinCenter(ix);
			M2=T5WgSignalLeptonMap.GetYaxis().GetBinCenter(ij);
			if M1!=800 or M2!=600:continue
			DeltaM=M1-M2
			SignalYield=T5WgSignalLeptonMap.GetBinContent(ix,ij);
			if M1-M2<0 or SignalYield<0:continue
			SignalPath=os.getcwd()+"/T5WgTestCards/T5Wg_Mgo%d_MLSP%d" %(M1,M2)
			if not os.path.isdir(SignalPath):os.mkdir(SignalPath);
			M1=T5WgSignalLeptonMap.GetXaxis().GetBinCenter(ix);
			M2=T5WgSignalLeptonMap.GetYaxis().GetBinCenter(ij);
			fSTOut=open('%s/GGMCombination_M1_%d_M2_%d_STBin%d.txt' %(SignalPath,M1,M2,i),'w')
			ftemplate=open("GGMCombinationTemplateBin_STBin%d.txt" %i, 'r')
			for line in ftemplate:
				line=line.replace("GGMSig", "0.0" )
				fSTOut.write(line);
			fSTOut.close();
			ftemplate.close();
for i in range(len(observationsHTgammabinned)):
	T5WgSignalLeptonMap=SingleLeptonSignal.Get("h_chan%d_rate_nom" %(i+1));
	if not os.path.isdir(testPath):os.mkdir(testPath);
        for ix in range(1,T5WgSignalLeptonMap.GetNbinsX() + 1):
		for ij in range(1,T5WgSignalLeptonMap.GetNbinsY() + 1):
			M1=T5WgSignalLeptonMap.GetXaxis().GetBinCenter(ix);
			M2=T5WgSignalLeptonMap.GetYaxis().GetBinCenter(ij);
			if M1!=800 or M2!=600:continue
			DeltaM=M1-M2
			SignalYield=T5WgSignalLeptonMap.GetBinContent(ix,ij);
			if M1-M2<0 or SignalYield<0:continue
			SignalPath=os.getcwd()+"/T5WgTestCards/T5Wg_Mgo%d_MLSP%d" %(M1,M2)
			if not os.path.isdir(SignalPath):os.mkdir(SignalPath);
			M1=T5WgSignalLeptonMap.GetXaxis().GetBinCenter(ix);
			M2=T5WgSignalLeptonMap.GetYaxis().GetBinCenter(ij);
			fHTOut=open('%s/GGMCombination_M1_%d_M2_%d_HTGammaBin%d.txt' %(SignalPath,M1,M2,i),'w')
			ftemplate=open("GGMCombinationTemplateBin_HTgammaBin%d.txt" %i, 'r')
			for line in ftemplate:
				line=line.replace("GGMSig", "0.0" )
				fHTOut.write(line);
			fHTOut.close();
			ftemplate.close();

			os.system(" combineCards.py %s/*.txt >%s/GGMCombination_M1_%d_M2_%d.txt " %(SignalPath,testPath, M1, M2))
			
			#print i,M1,M2,SignalYield
#NOW NUISANCES:

