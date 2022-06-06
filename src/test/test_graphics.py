import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
import search as s
import business_logic.heuristics as hh

## Create strings for matching
alphabet = 'ACGT'
t = 'CTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCA'
program = s.Search(text=t, word='CCCTA', heuristics=[hh.Badcharacter('CCCTA', alphabet), hh.Goodsuffix('CCCTA')])
program.do_magic()

program2 = s.Search(text=t, word='CCCTA', heuristics=[hh.Goodsuffix('CCCTA')])
program2.do_magic()

program3 = s.Search(text=t, word='AT', heuristics=[hh.Badcharacter('AT', alphabet), hh.Goodsuffix('AT')])
program3.do_magic()

program4 = s.Search(text=t, word='AT', heuristics=[hh.Goodsuffix('AT')])
program4.do_magic()

program5 = s.Search(text=t, word='ATATATA', heuristics=[hh.Badcharacter('ATATATA', alphabet), hh.Goodsuffix('ATATATA')])
program5.do_magic()

program6 = s.Search(text=t, word='ATATATA', heuristics=[hh.Goodsuffix('ATATATA')])
program6.do_magic()

program7 = s.Search(text=t, word='GCGCGGGGC', heuristics=[hh.Badcharacter('GCGCGGGGC', alphabet), hh.Goodsuffix('GCGCGGGGC')])
program7.do_magic()

program7 = s.Search(text=t, word='GCGCGGGGC', heuristics=[hh.Goodsuffix('GCGCGGGGC')])
program7.do_magic()

program8 = s.Search(text=t, word='CACTTATCGATGAAACAACT', heuristics=[hh.Badcharacter('CACTTATCGATGAAACAACT', alphabet), hh.Goodsuffix('CACTTATCGATGAAACAACT')])
program8.do_magic()

program9 = s.Search(text=t, word='CACTTATCGATGAAACAACT', heuristics=[hh.Goodsuffix('CACTTATCGATGAAACAACT')])
program9.do_magic()

program10 = s.Search(text=t, word='GCGCGGAAAGGCGCGCGGAAAGGC', heuristics=[hh.Badcharacter('GCGCGGAAAGGCGCGCGGAAAGGC', alphabet), hh.Goodsuffix('GCGCGGAAAGGCGCGCGGAAAGGC')])
program10.do_magic()

program11 = s.Search(text=t, word='GCGCGGAAAGGCGCGCGGAAAGGC', heuristics=[hh.Goodsuffix('GCGCGGAAAGGCGCGCGGAAAGGC')])
program11.do_magic()

import business_logic.util.graph as g
g.Graph().Drive([program, program2, program3, program4, program5, program6, program11, program10, program9, program8, program7])
