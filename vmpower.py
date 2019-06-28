import re
import argparse
parser = argparse.ArgumentParser(description="Matches VM Name/UUID to power events from Acropolis logs")
parser.add_argument("acroplogs", type=argparse.FileType('r'), help="Put your acropolis log here")
parser.add_argument("vmlist", type=argparse.FileType('r'), help="Pass the output from acli vm.list here")
args = parser.parse_args()

def main(acroplogs, vmlist):
    logs = str(args.acroplogs.read())
    vmList = str(args.vmlist.read())
    nameRegex = re.compile(r"^(?P<name>.+?)\s+(?P<uuid>[^\s]+)$", re.MULTILINE)

    for match in nameRegex.finditer(vmList):
        print(f'{match.group("name")}\t{match.group("uuid")}')
        for powerEvents in logs.split("/n"):
            if match.group("uuid") in powerEvents:
                grep = re.match(r'^[^:]+:(?P<date>.+?) INFO.+(?P<event>kPower[^\)]+)', powerEvents.strip())
                print(match.group("name") + " Had a power event at: " + grep.group("date") + (" ") + grep.group("event"))

main(acroplogs=args.acroplogs, vmlist=args.vmlist)