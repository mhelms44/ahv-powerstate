import re
import argparse
parser = argparse.ArgumentParser(description="Matches VM Name/UUID to power events from Acropolis logs")
parser.add_argument("acroplogs", type=argparse.FileType('r'), help="Put your acropolis log here")
parser.add_argument("vmlist", type=argparse.FileType('r'), help="Pass the output from acli vm.list here")
args = parser.parse_args()

def main(acroplogs, vmlist):
    logs = str(args.acroplogs.read())
    vmList = str(args.vmlist.read())
    uuid = re.findall( "[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}", vmList)
    vmName = re.sub("[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}", "", vmList)
    vmNameList = vmName.split()
    for u, v in zip(uuid, vmNameList):
        print(v + "\t" + u)
        for powerEvents in logs.split("/n"):
            if u in powerEvents:
                grep = re.match(r'^[^:]+:(?P<date>.+?) INFO.+(?P<event>kPower[^\)]+)', powerEvents.strip())
                print(v + " Had a power event at: " + grep.group("date") + (" ") + grep.group("event"))

main(acroplogs=args.acroplogs, vmlist=args.vmlist)