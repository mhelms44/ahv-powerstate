import re
import argparse
parser = argparse.ArgumentParser(description="Matches VM Name/UUID to power events from Acropolis")
parser.add_argument("acropolislog", type=argparse.FileType('r'), help="put your acropolis log blob here")
parser.add_argument("vmlist", type=argparse.FileType('r'), help="put your vm list here")
args = parser.parse_args()

logs = str(args.acropolislog.read())
vmList = str(args.vmlist.read())

uuid = re.findall( "[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}", vmList)

vmName = re.sub("[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}", "", vmList)
vmNameList = vmName.split()
print (uuid)
print (vmNameList)

for u, v in zip(uuid, vmNameList):
    print(v + "\t" + u)




'''
for vmsID in uuid:
    for powerEvents in logs.split("\n"):
        if vmsID in powerEvents:
            grep = re.match(r'^[^:]+:(?P<date>.+?) INFO.+(?P<event>kPower[^\)]+)', powerEvents.strip())        
            print(grep.group("date") + (" ") + grep.group("event"))
'''