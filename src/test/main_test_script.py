import sys
import os
from pathlib import Path

# issues in importing parent directories as modules 
parent_subdirectory = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir)) 
parent_directory = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, os.pardir))


# append path directories as modules
sys.path.append(parent_directory)
sys.path.append(parent_subdirectory)
from src import search as s
from src.business_logic import heuristics as hh
from src.business_logic import performance as pf
from src.test.util import test_helper as helper



# GLOBAL
# Calculates performance
perf_calc = pf.Performance()
data_metrics = []





###################### Test set 1 #########################
print("Test set 1: Tekst: Coffea arabica, Chromosome 1c i paterni: ATGCATG, TCTCTCTA, TTCACTACTCTCA")


words = ['ATGCATG', 'TCTCTCTA', 'TTCACTACTCTCA']
# file = "../../data/chr1.fna" # enter relative path to the data
file = 'C:/Users/tsretkovic/Desktop/skola/GI/PROJEKAT/GI-projekat/src/data/chr1.fna'
# Alhabet in FASTA file
alphabet = 'ACGTN'

helper.spin_heuristics(file, words, alphabet, perf_calc, data_metrics)


# ###################### Test set 2 #########################

# print("Test set 2: Tekst: Mus pahari chromosome X, i paterni: ATGATG, CTCTCTA, TCACTACTCTCA")

# # TODO: add correct filepath
# words = ['ATGATG', 'CTCTCTA', 'TCACTACTCTCA']
# #file = "C:\Users\tsretkovic\Desktop\skola\GI\PROJEKAT\chr1.fna.gz"

# # Alhabet in FASTA file
# alphabet = 'ACGTN'

# helper.spin_heuristics(file, words, alphabet, perf_calc, data_metrics)




# ###################### Test set 3 #########################

# print("Test set 3: Genom po slobodnom izboru iz NIH baze i proizvoljna 3 paterna različite dužine.")

# # TODO: change words and add correct filepath
# words = ['AAAAAAG', 'TGGGGGGGG', 'CTAAAAAAAAAAAAAAAAA', 'AAAAAAAAAAAAAAAAAAC]
# #file = "C:\Users\tsretkovic\Desktop\skola\GI\PROJEKAT\chr1.fna.gz"

# # Alhabet in FASTA file
# alphabet = 'ACGTN'

# helper.spin_heuristics(file, words, alphabet, perf_calc, data_metrics)


import business_logic.util.graph as g
g.Graph().Drive(data_metrics)