import sys
import os

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

# Alhabet in FASTA file
alphabet = 'ACGTNU'


###################### Test set 1 #########################
print("Test set 1: Tekst: Coffea arabica, Chromosome 1c i paterni: ATGCATG, TCTCTCTA, TTCACTACTCTCA")


words = ['ATGCATG', 'TCTCTCTA', 'TTCACTACTCTCA']
# file = "../../data/chr1.fna" # enter relative path to the data
file = 'C:/Users/tsretkovic/Desktop/skola/GI/PROJEKAT/GI-projekat/src/data/chr1.fna'

helper.spin_heuristics(file, words, alphabet, perf_calc, data_metrics)



###################### Test set 2 #########################

print("Test set 2: Genom po slobodnom izboru: PhiX_genome.fasta, i paterni: ATGATG, CTCTCTA, TCACTACTCTCA")

words = ['ATGATG', 'CTCTCTA', 'TCACTACTCTCA']
file = 'C:/Users/tsretkovic/Desktop/skola/GI/PROJEKAT/GI-projekat/src/data/PhiX_genome.fasta'
# file = "../../data/PhiX_genome.fasta" # enter relative path to the data

helper.spin_heuristics(file, words, alphabet, perf_calc, data_metrics)




# ###################### Test set 3 #########################

print("Test set 3: Genom po slobodnom izboru: example_human_reference.fasta, paterni: 'AATCTTT', 'TCAG', 'CTTTTGTTGCCTGTGCCTTTGATGT'")

words = ['AATCTTT', 'TCAG', 'CTTTTGTTGCCTGTGCCTTTGATGT']
file = 'C:/Users/tsretkovic/Desktop/skola/GI/PROJEKAT/GI-projekat/src/data/example_human_reference.fasta'
# file = "../../data/example_human_reference.fasta" # enter relative path to the data

helper.spin_heuristics(file, words, alphabet, perf_calc, data_metrics)


import business_logic.util.graph as g
g.Graph().Drive(data_metrics)