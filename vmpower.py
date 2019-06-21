import re
import argparse
parser = argparse.ArgumentParser(description="Matches VM Name/UUID to power events from Acropolis")
parser.add_argument("acropolislog", type=argparse.FileType('r'), help="put your acropolis log blob here")
parser.add_argument("vmlist", type=argparse.FileType('r'), help="put your vm list here")
args = parser.parse_args()

aLog = str(args.acropolislog.read())
vmList = str(args.vmlist.read())

uuid = re.findall("[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}", vmList)
print(uuid)