import sys
from os import path
from unittest import result
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
import search as s
import business_logic.heuristics as hh
import business_logic.performance as pf

# function creates data relevant to time and memory performance optimization
def get_data(searcher:s.Search, perf_calc:pf.Performance):
    # Time process 
    perf_calc.start_clock()
    sol = searcher.search_text()
    time, mem = perf_calc.stop_clock()

    data = pf.PerformanceData(
        heuristic_name=searcher.get_heuristics(),
        word_length = len(word),
        time = time,
        memory = mem
    )
    
    return sol, data


## Create strings for matching
alphabet = 'ACGT'
t = 'CTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCA'
words = ['CCCTA', 'ATG', 'ATATATA', 'GCGCGGGGC', 'CACTTATCGATGAAACAACT', 'GCGCGGAAAGGCGCGCGGAAAGGC', 'ATCGTA']
results = [0,21,0,0,20,0,21]
# Class used for tracing memory allocation and execution time
perf_calc = pf.Performance()

data_metrics = []
for i, word in enumerate(words):
    # Fetch metrics for each combination of heuristics
    searcher = s.Search(text=t, word=word,  heuristics=[hh.Badcharacter(word, alphabet), hh.Goodsuffix(word)])

    sol1, data = get_data(searcher, perf_calc)
    data_metrics.append(data)
    print(sol1)

    searcher = s.Search(text=t, word=word, heuristics = [hh.RLongestGap(word)])

    sol2, data = get_data(searcher, perf_calc)
    data_metrics.append(data)
    print(sol2)

    searcher = s.Search(text=t, word=word, heuristics = [hh.LolngestGap(word)])

    sol3, data = get_data(searcher, perf_calc)
    data_metrics.append(data)
    print(sol3)

    searcher = s.Search(text=t, word=word, heuristics = [hh.LolngestGap(word),hh.RLongestGap(word)])

    sol4, data = get_data(searcher, perf_calc)
    data_metrics.append(data)
    print(sol4)

    # check that every heuristic found the same data and number of matched text aligns with what we can find doing ctrl+f :)
    assert sol1 == sol2
    assert sol1 == sol3
    assert sol1 == sol4
    assert len(sol1) == results[i]



# by human eye double check if data in table and graph is correct
import business_logic.util.graph as g
#g.Graph().Drive(data_metrics)