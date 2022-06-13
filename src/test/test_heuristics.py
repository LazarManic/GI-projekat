import sys
import os

# issues in importing parent directories as modules 
parent_subdirectory = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir)) 
parent_directory = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, os.pardir))

# append path directories as modules
sys.path.append(parent_directory)
sys.path.append(parent_subdirectory)


alphabet = 'ACGT'

from src.business_logic import heuristics as hh

#########################################################################################################
#                                         Test LLongestJump                                             #
#########################################################################################################


# Test vector

word = 'ACGACGACGACG'
vector = hh.LLongestGap.get_jump_vector(word)
assert len(vector) == len(word) + 1
assert vector == [3,3,3,3,3,3,3,3,3,3,3,3,1]

word = 'AAAAAAAAAG'
vector = hh.LLongestGap.get_jump_vector(word)
assert len(vector) == len(word) + 1
assert vector == [10,10,10,10,10,10,10,10,10,10,1]

word = 'GAAAAAAAAA'
vector = hh.LLongestGap.get_jump_vector(word)
assert len(vector) == len(word) + 1
assert vector == [2,2,1,1,1,1,1,1,1,1,1]


# Test apply rule (does not depend on search text)

word = 'ACGACGACGACG'
h = hh.LLongestGap(word)
assert h.apply_rule('',1,3) == 3
assert h.apply_rule('',1,11) == 1
assert h.apply_rule('',1,0) == 3

word = 'AAAAAAAAAG'
h = hh.LLongestGap(word)
assert h.apply_rule('',1,3) == 10
assert h.apply_rule('',1,9) == 1
assert h.apply_rule('',1,0) == 10

word = 'GAAAAAAAAA'
h = hh.LLongestGap(word)
assert h.apply_rule('',1,3) == 1
assert h.apply_rule('',1,9) == 1
assert h.apply_rule('',1,0) == 2


# Test mach skipp

word = 'ACGACGACGACG'
h = hh.LLongestGap(word)
assert h.match_skip() == 3

word = 'AAAAAAAAAG'
h = hh.LLongestGap(word)
assert h.match_skip() == 10

word = 'GAAAAAAAAA'
h = hh.LLongestGap(word)
assert h.match_skip() == 2






#########################################################################################################
#                                         Test RLongestJump                                             #
#########################################################################################################


# Test vector

word = 'ACGACGACGACG'
vector = hh.RLongestGap.get_jump_vector(word)
assert len(vector) == len(word) + 1
assert vector == [3,3,3,3,3,3,3,3,3,3,2,1,1]

word = 'AAAAAAAAAG'
vector = hh.RLongestGap.get_jump_vector(word)
assert len(vector) == len(word) + 1
assert vector == [2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1]

word = 'GAAAAAAAAA'
vector = hh.RLongestGap.get_jump_vector(word)
assert len(vector) == len(word) + 1
assert vector == [10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


# Test apply rule (does not depend on search text)

word = 'ACGACGACGACG'
h = hh.RLongestGap(word)
assert h.apply_rule('',1,3) == 3
assert h.apply_rule('',1,11) == 1
assert h.apply_rule('',1,0) == 3

word = 'AAAAAAAAAG'
h = hh.RLongestGap(word)
assert h.apply_rule('',1,3) == 2
assert h.apply_rule('',1,9) == 1
assert h.apply_rule('',1,0) == 2

word = 'GAAAAAAAAA'
h = hh.RLongestGap(word)
assert h.apply_rule('',1,3) == 1
assert h.apply_rule('',1,9) == 1
assert h.apply_rule('',1,0) == 1


# Test mach skipp

word = 'ACGACGACGACG'
h = hh.RLongestGap(word)
assert h.match_skip() == 3

word = 'AAAAAAAAAG'
h = hh.RLongestGap(word)
assert h.match_skip() == 2

word = 'GAAAAAAAAA'
h = hh.RLongestGap(word)
assert h.match_skip() == 10





#########################################################################################################
#                                         Test Badcharacter                                             #
#########################################################################################################



# Test amap -> a map that maps each valid character(that can occur in matching string) to a unique integer
# Does not depend on word but on alphabet

word = 'ACGACGACGACG'
h = hh.Badcharacter(word, alphabet)
assert h.get_amap() == {'A': 0, 'C': 1, 'G': 2, 'T': 3}

word = 'AAAAAAAAAG'
h = hh.Badcharacter(word, alphabet)
assert h.get_amap() == {'A': 0, 'C': 1, 'G': 2, 'T': 3}

word = 'GAAAAAAAAA'
h = hh.Badcharacter(word, alphabet)
assert h.get_amap() == {'A': 0, 'C': 1, 'G': 2, 'T': 3}


# Test dense_bad_char_tab
from src.business_logic.util import bad_char_util as bu

amap = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

word = 'ACGACGACGACG'
expected_table = [
    [0, 0, 0, 0],
    [1, 0, 0, 0],
    [1, 2, 0, 0],
    [1, 2, 3, 0],
    [4, 2, 3, 0],
    [4, 5, 3, 0],
    [4, 5, 6, 0],
    [7, 5, 6, 0],
    [7, 8, 6, 0],
    [7, 8, 9, 0],
    [10, 8, 9, 0],
    [10, 11, 9, 0]
    ]
bc_table = bu.dense_bad_char_tab(word, amap)
assert bc_table == expected_table

word = 'AAAAAAAAAG'
expected_table = [
    [0, 0, 0, 0],
    [1, 0, 0, 0],
    [2, 0, 0, 0],
    [3, 0, 0, 0],
    [4, 0, 0, 0],
    [5, 0, 0, 0],
    [6, 0, 0, 0],
    [7, 0, 0, 0],
    [8, 0, 0, 0],
    [9, 0, 0, 0]
    ]

bc_table = bu.dense_bad_char_tab(word, amap)
assert bc_table == expected_table

word = 'GAAAAAAAAA'
expected_table = [
    [0, 0, 0, 0],
    [0, 0, 1, 0],
    [2, 0, 1, 0],
    [3, 0, 1, 0],
    [4, 0, 1, 0],
    [5, 0, 1, 0],
    [6, 0, 1, 0],
    [7, 0, 1, 0],
    [8, 0, 1, 0],
    [9, 0, 1, 0]
    ]
bc_table = bu.dense_bad_char_tab(word, amap)
assert bc_table == expected_table


# Test apply rule (does not depend on search text)
text = 'TTATCGATGAAAA'
word = 'CTTATCGATGAAA'
h = hh.Badcharacter(word, alphabet)

assert h.apply_rule(text,1,3) == 3
assert h.apply_rule(text,1,11) == 1
assert h.apply_rule(text,1,0) == 1

word = 'AAAAAAAAAG'
h = hh.Badcharacter(word, alphabet)

assert h.apply_rule(text,1,3) == 4
assert h.apply_rule(text,1,9) == 1
assert h.apply_rule(text,1,0) == 1

word = 'GAAAAAAAAA'
h = hh.Badcharacter(word, alphabet)

assert h.apply_rule(text,1,3) == 4
assert h.apply_rule(text,1,9) == 1
assert h.apply_rule(text,1,0) == 1


# Test mach skipp

word = 'ACGACGACGACG'
h = hh.Badcharacter(word, alphabet)
assert h.match_skip() == 1

word = 'AAAAAAAAAG'
h = hh.Badcharacter(word, alphabet)
assert h.match_skip() == 1

word = 'GAAAAAAAAA'
h = hh.Badcharacter(word, alphabet)
assert h.match_skip() == 1






#########################################################################################################
#                                         Test Goodsuffix                                               #
#########################################################################################################


# Test tabels
import business_logic.util.good_suffix_util as gs

word = 'ACGACGACGACG'
_, table1, table2 = gs.good_suffix_table(word)
assert table1 == [0, 0, 0, 9, 9, 9, 9, 9, 9, 9, 9, 9]
assert table2 == [12, 9, 9, 9, 6, 6, 6, 3, 3, 3, 0, 0]

word = 'AAAAAAAAAG'
_, table1, table2 = gs.good_suffix_table(word)
assert table1 == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
assert table2 == [10, 0, 0, 0, 0, 0, 0, 0, 0, 0]

word = 'GAAAAAAAAA'
_, table1, table2 = gs.good_suffix_table(word)
assert table1 == [0, 0, 9, 9, 9, 9, 9, 9, 9, 9]
assert table2 == [10, 0, 0, 0, 0, 0, 0, 0, 0, 0]


# Test apply rule (does not depend on search text)

word = 'ACGACGACGACG'
h = hh.RLongestGap(word)
assert h.apply_rule('',1,3) == 3
assert h.apply_rule('',1,11) == 1
assert h.apply_rule('',1,0) == 3

word = 'AAAAAAAAAG'
h = hh.RLongestGap(word)
assert h.apply_rule('',1,3) == 2
assert h.apply_rule('',1,9) == 1
assert h.apply_rule('',1,0) == 2

word = 'GAAAAAAAAA'
h = hh.RLongestGap(word)
assert h.apply_rule('',1,3) == 1
assert h.apply_rule('',1,9) == 1
assert h.apply_rule('',1,0) == 1


# Test mach skipp

word = 'ACGACGACGACG'
h = hh.Goodsuffix(word)
assert h.match_skip() == 3

word = 'AAAAAAAAAG'
h = hh.Goodsuffix(word)
assert h.match_skip() == 10

word = 'GAAAAAAAAA'
h = hh.Goodsuffix(word)
assert h.match_skip() == 10


