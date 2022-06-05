import sys
import os
from pathlib import Path

# issues in importing parent directories as modules 
parent_subdirectory = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir)) 
parent_directory = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, os.pardir))


# append path directories as modules
sys.path.append(parent_directory)
sys.path.append(parent_subdirectory)

###################### Test set 1 #########################
print("Test set 1: Tekst: Coffea arabica, Chromosome 1c i paterni: ATGCATG, TCTCTCTA, TTCACTACTCTCA")

words = ['ATGCATG', 'TCTCTCTA', 'TTCACTACTCTCA']


file = "../../data/chr1.fna" # enter relative path to the data
#file = "C:\Users\tsretkovic\Desktop\skola\GI\PROJEKAT\chr1.fna.gz"

from src import search as s
from src.business_logic import heuristics as hh

# Alhabet in FASTA file
# TODO double check
alphabet = 'ACGTN'

for word in words:
    # TODO: h1, h2, h1 + h2
    program_4 = s.Search(file_path=file, word=word, heuristics=[hh.Badcharacter(word, alphabet), hh.Goodsuffix(word)])
    program_4.do_magic()



###################### Test set 2 #########################

print("Test set 2: Tekst: Mus pahari chromosome X, i paterni: ATGATG, CTCTCTA, TCACTACTCTCA")

# TODO: add correct filepath
words = ['ATGATG', 'CTCTCTA', 'TCACTACTCTCA']
#file = "C:\Users\tsretkovic\Desktop\skola\GI\PROJEKAT\chr1.fna.gz"

for word in words:
    # TODO: h1, h2, h1 + h2
    program_4 = s.Search(file_path=file, word=word, heuristics=[hh.Badcharacter(word, alphabet), hh.Goodsuffix(word)])
    program_4.do_magic()




###################### Test set 3 #########################

print("Test set 3: Genom po slobodnom izboru iz NIH baze i proizvoljna 3 paterna različite dužine.")

# TODO: change words and add correct filepath
words = ['ATGCATG', 'TCTCTCTA', 'TTCACTACTCTCA']
#file = "C:\Users\tsretkovic\Desktop\skola\GI\PROJEKAT\chr1.fna.gz"

for word in words:
    # TODO: h1, h2, h1 + h2
    program_4 = s.Search(file_path=file, word=word, heuristics=[hh.Badcharacter(word, alphabet), hh.Goodsuffix(word)])
    program_4.do_magic()
