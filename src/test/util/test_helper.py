
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


def get_pergormance(file_path:str, word:str, heuristics, perf_calc):
    # Initialize searcher for each word
    searcher = s.Search(file_path=file_path, word=word, heuristics=heuristics)
    
    # Start performance check 
    perf_calc.start_clock()
    sol = searcher.search_fasta_as_datastream()
    time, mem = perf_calc.stop_clock()
    print("Searching word: {0}, number of occurences: {1}, indexes:\n{1}".format(word, len(sol), sol))


    # Create dataclass that stores performances for heuristic combinations
    data = pf.PerformanceData(
        heuristic_name=searcher.get_heuristics(),
        word_length = len(word),
        time = time,
        memory = mem
    ) 

    return data


def spin_heuristics(file_path, words, alphabet, perf_calc, data_metrics):
    for word in words:

        h = [hh.Badcharacter(word, alphabet), hh.Goodsuffix(word)]
        data_metrics.append(get_pergormance(file_path, word, h, perf_calc))

        h = [hh.LolngestGap(word)]
        data_metrics.append(get_pergormance(file_path, word, h, perf_calc))

        h = [hh.RLongestGap(word)]
        data_metrics.append(get_pergormance(file_path, word, h, perf_calc))

        h = [hh.LolngestGap(word), hh.RLongestGap(word)]
        data_metrics.append(get_pergormance(file_path, word, h, perf_calc))


