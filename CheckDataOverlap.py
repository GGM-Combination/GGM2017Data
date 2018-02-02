fileDipho=open("DiPhoton/signalEvents.txt", 'r');
fileLep=open("LeptonPhoton/signalEvents.txt", 'r');
DiphotonEvtRunLumi=[]
for line in fileDipho:
	parse=line.split(",")
	event=int(parse[0].split(":")[1])
	run=int(parse[1].split("=")[1])
	lumi=int(parse[2].split("=")[1])
	#print event,run,lumi
	DataString="%d:%d:%d" %(event,run,lumi)
	DiphotonEvtRunLumi.append(DataString);
for line in fileLep:
	parse=line.split(",")
	if len(parse)<6:continue
	event=int(parse[0].split(":")[1])
	run=int(parse[1].split("=")[1])
	lumi=int(parse[2].split("=")[1])
	#print event,run,lumi
	DataString="%d:%d:%d" %(event,run,lumi)
	if DataString in DiphotonEvtRunLumi:print DataString
	
