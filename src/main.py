import string_search_alg as ss
import heuristics as hh

## Create strings for matching
t = 'CTTATCGATGAAACTGAATCGTACTCAGGTCA'
p = 'TGAAT'

## String that contains all possible characters
alphabet = 'ACGT'


# Create a list of heuristics
heuristics = [hh.Badcharacter(p, alphabet), hh.Goodsuffix(p)]


search = ss.Stringsearch(heuristics)
sol = search.find(t, p)
print("Number of occurences: {0}, indexes:{1}".format(len(sol), sol))




