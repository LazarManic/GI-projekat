import argparse
import business_logic.heuristics as hh

# Define arguments for the script
msg = "Usage: script.py --input/-i <InoutFilePath> --heuristic/-he <h>"
parser = argparse.ArgumentParser(description=msg)
parser.add_argument("-i", "--input", help="Input file is missing", required=True, type=str)
parser.add_argument("-s", "--search", help="Search text is missing", required=True, type=str)
parser.add_argument("-he", "--heuristic", help="Enter desired heuristics. Example: 1", required=True, type=int)
parser.add_argument("-a", "--alphabet", required=False, help="Enter posible alphabet. Example 'ABC'", type=str, default='ACGT')
args = parser.parse_args()

# Ceate list of heuristics
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
# TODO try FASTA file
t = 'CTTATCGATGAAACAACTGAATCGTACTCAGGTCA'
program = s.Search(text=t, word=args.search, heuristics=heuristics)
program.do_magic()

import business_logic.util.cvs as c

c.Cvs().write("output.csv", [program])

