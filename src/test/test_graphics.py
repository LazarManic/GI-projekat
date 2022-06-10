import sys
from os import path
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
words = ['CCCTA', 'AT', 'ATATATA', 'GCGCGGGGC', 'CACTTATCGATGAAACAACT', 'GCGCGGAAAGGCGCGCGGAAAGGC']

# Class used for tracing memory allocation and execution time
perf_calc = pf.Performance()

data_metrics = []
for word in words:
    # Fetch metrics for each combination of heuristics
    searcher = s.Search(text=t, word=word,  heuristics=[hh.Badcharacter(word, alphabet), hh.Goodsuffix(word)])

    sol, data = get_data(searcher, perf_calc)
    data_metrics.append(data)
    print(sol)

    searcher = s.Search(text=t, word=word, heuristics = [hh.RLongestGap(word)])

    sol, data = get_data(searcher, perf_calc)
    data_metrics.append(data)
    print(sol)

    searcher = s.Search(text=t, word=word, heuristics = [hh.LolngestGap(word)])

    sol, data = get_data(searcher, perf_calc)
    data_metrics.append(data)
    print(sol)

    searcher = s.Search(text=t, word=word, heuristics = [hh.RLongestGap(word), hh.LolngestGap(word)])

    sol, data = get_data(searcher, perf_calc)
    data_metrics.append(data)
    print(sol)




import business_logic.util.graph as g
g.Graph().Drive(data_metrics)