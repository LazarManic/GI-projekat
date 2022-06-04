import tracemalloc
import time

import business_logic.string_search_alg as ss
import business_logic.heuristics as hh

## Create strings for matching
t = 'CTTATCGATGAAACAACTGAATCGTACTCAGGTCA'
p = 'TGAAT'

## String that contains all possible characters
alphabet = 'ACGT'

# Create a list of heuristics
heuristics = [hh.Badcharacter(p, alphabet), hh.Goodsuffix(p)]
search = ss.Stringsearch(heuristics)

# start of monitoring memory allocation and time of execusion
tracemalloc.start()
start_time = time.time()

# run the algorithm
sol = search.find(t, p)

# end of monitoring memory allocation and time of execusion
end_time = time.time()
memory = tracemalloc.get_traced_memory()
tracemalloc.stop()

print("Number of occurences: {0}, indexes:{1}".format(len(sol), sol))
print("Execution time: {time:.10f}, execution memory peak: {mem} KiB".format(time = end_time - start_time, mem = memory[1] - memory[0]))




