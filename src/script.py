import argparse
import business_logic.heuristics as hh

# Define arguments for the script
msg = "Usage: script.py --input/-i <InoutFilePath> --heuristic/-he <h>"
parser = argparse.ArgumentParser(description=msg)
parser.add_argument("-i", "--input", help="Input file is missing", required=True, type=str)
parser.add_argument("-s", "--search", help="Search text is missing", required=True, type=str)
parser.add_argument("-he", "--heuristic", help="Enter desired heuristics. Example: 1", type=int, default=4)
parser.add_argument("-a", "--alphabet", required=False, help="Enter posible alphabet. Example 'ABC'", type=str, default='ACGT')
args = parser.parse_args()

# Ceate list of heuristics
# TODO add new heuristics
if args.heuristic == 1:
    heuristics = [hh.Goodsuffix(args.search)]
elif args.heuristic == 2:
    heuristics = [hh.Goodsuffix(args.search)]
elif args.heuristic == 3:
    heuristics = [hh.Goodsuffix(args.search)]
else:
    # Default
    heuristics = [hh.Badcharacter(args.search, args.alphabet), hh.Goodsuffix(args.search)]


import search as s

## Create strings for matching
program = s.Search(text_or_file_path=args.input, word=args.search, heuristics=heuristics, is_file_path=True)
program.do_magic()

import business_logic.util.graph as g

g.Graph().Drive([program])

