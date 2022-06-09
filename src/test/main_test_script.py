import sys
import os
from pathlib import Path

# issues in importing parent directories as modules 
parent_subdirectory = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir)) 
parent_directory = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, os.pardir))


# append path directories as modules
sys.path.append(parent_directory)
sys.path.append(parent_subdirectory)

programs = []
###################### Test set 1 #########################
print("Test set 1: Tekst: Coffea arabica, Chromosome 1c i paterni: ATGCATG, TCTCTCTA, TTCACTACTCTCA")

words = ['ATGCATG', 'TCTCTCTA', 'TTCACTACTCTCA']
file = "../../data/chr1.fna" # enter relative path to the data
#file = 'C:/Users/tsretkovic/Desktop/skola/GI/PROJEKAT/GI-projekat/src/data/chr1.fna'

from src import search as s
from src.business_logic import heuristics as hh
from src.business_logic import performance as pf

# Alhabet in FASTA file
alphabet = 'ACGTN'

# Calculates performance
perf_calc = pf.Performance()
data_metrics = []

for word in words:

    # Initialize searcher for each word
    searcher = s.Search(file_path=file, word=word, heuristics=[hh.Badcharacter(word, alphabet), hh.Goodsuffix(word)])
    
    # Start performance check 
    perf_calc.start_clock()
    sol1 = searcher.search_fasta_as_datastream()
    #sol2 = searcher.search_fasta()
    time, mem = perf_calc.stop_clock()

    # Create dataclass that stores performances for heuristic combinations
    data = pf.PerformanceData(
        heuristic_name=searcher.get_heuristics(),
        word_length = len(word),
        time = time,
        memory = mem
    )

    data_metrics.append(data)

# ###################### Test set 2 #########################

# print("Test set 2: Tekst: Mus pahari chromosome X, i paterni: ATGATG, CTCTCTA, TCACTACTCTCA")

# # TODO: add correct filepath
# words = ['ATGATG', 'CTCTCTA', 'TCACTACTCTCA']
# #file = "C:\Users\tsretkovic\Desktop\skola\GI\PROJEKAT\chr1.fna.gz"

# for word in words:
    # TODO add all heuristics
    # programs.append(s.Search(word=word, heuristics=[hh.Badcharacter(word, alphabet), hh.Goodsuffix(word)], text_or_file_path=file, is_file_path=True))
    # programs[len(programs) - 1].do_magic()




# ###################### Test set 3 #########################

# print("Test set 3: Genom po slobodnom izboru iz NIH baze i proizvoljna 3 paterna različite dužine.")

# # TODO: change words and add correct filepath
# words = ['ATGCATG', 'TCTCTCTA', 'TTCACTACTCTCA']
# #file = "C:\Users\tsretkovic\Desktop\skola\GI\PROJEKAT\chr1.fna.gz"

# for word in words:
    # TODO add all heuristics
    # programs.append(s.Search(word=word, heuristics=[hh.Badcharacter(word, alphabet), hh.Goodsuffix(word)], text_or_file_path=file, is_file_path=True))
    # programs[len(programs) - 1].do_magic()


import business_logic.util.graph as g
g.Graph().Drive(data_metrics)