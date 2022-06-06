import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
import search as s
import business_logic.heuristics as hh

## Create strings for matching
alphabet = 'ACGT'
t = 'CTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCACTTATCGATGAAACAACTGAATCGTACTCAGGTCA'
program = s.Search(text_or_file_path=t, word='CCCTA', heuristics=[hh.Badcharacter('CCCTA', alphabet), hh.Goodsuffix('CCCTA')], is_file_path=False)
program.do_magic()

program2 = s.Search(text_or_file_path=t, word='CCCTA', heuristics=[hh.Goodsuffix('CCCTA')], is_file_path=False)
program2.do_magic()

program17 = s.Search(text_or_file_path=t, word='CCCTA', heuristics=[hh.Badcharacter('CCCTA', alphabet)], is_file_path=False)
program17.do_magic()

program3 = s.Search(text_or_file_path=t, word='AT', heuristics=[hh.Badcharacter('AT', alphabet), hh.Goodsuffix('AT')], is_file_path=False)
program3.do_magic()

program4 = s.Search(text_or_file_path=t, word='AT', heuristics=[hh.Goodsuffix('AT')], is_file_path=False)
program4.do_magic()

program16 = s.Search(text_or_file_path=t, word='AT', heuristics=[hh.Badcharacter('AT', alphabet)], is_file_path=False)
program16.do_magic()

program5 = s.Search(text_or_file_path=t, word='ATATATA', heuristics=[hh.Badcharacter('ATATATA', alphabet), hh.Goodsuffix('ATATATA')], is_file_path=False)
program5.do_magic()

program15 = s.Search(text_or_file_path=t, word='ATATATA', heuristics=[hh.Badcharacter('ATATATA', alphabet)], is_file_path=False)
program15.do_magic()

program6 = s.Search(text_or_file_path=t, word='ATATATA', heuristics=[hh.Goodsuffix('ATATATA')], is_file_path=False)
program6.do_magic()

program7 = s.Search(text_or_file_path=t, word='GCGCGGGGC', heuristics=[hh.Badcharacter('GCGCGGGGC', alphabet), hh.Goodsuffix('GCGCGGGGC')], is_file_path=False)
program7.do_magic()

program7 = s.Search(text_or_file_path=t, word='GCGCGGGGC', heuristics=[hh.Goodsuffix('GCGCGGGGC')], is_file_path=False)
program7.do_magic()

program14 = s.Search(text_or_file_path=t, word='GCGCGGGGC', heuristics=[hh.Badcharacter('GCGCGGGGC', alphabet)], is_file_path=False)
program14.do_magic()

program8 = s.Search(text_or_file_path=t, word='CACTTATCGATGAAACAACT', heuristics=[hh.Badcharacter('CACTTATCGATGAAACAACT', alphabet), hh.Goodsuffix('CACTTATCGATGAAACAACT')], is_file_path=False)
program8.do_magic()

program9 = s.Search(text_or_file_path=t, word='CACTTATCGATGAAACAACT', heuristics=[hh.Goodsuffix('CACTTATCGATGAAACAACT')], is_file_path=False)
program9.do_magic()

program13 = s.Search(text_or_file_path=t, word='CACTTATCGATGAAACAACT', heuristics=[hh.Badcharacter('CACTTATCGATGAAACAACT', alphabet)], is_file_path=False)
program13.do_magic()

program10 = s.Search(text_or_file_path=t, word='GCGCGGAAAGGCGCGCGGAAAGGC', heuristics=[hh.Badcharacter('GCGCGGAAAGGCGCGCGGAAAGGC', alphabet), hh.Goodsuffix('GCGCGGAAAGGCGCGCGGAAAGGC')], is_file_path=False)
program10.do_magic()

program11 = s.Search(text_or_file_path=t, word='GCGCGGAAAGGCGCGCGGAAAGGC', heuristics=[hh.Goodsuffix('GCGCGGAAAGGCGCGCGGAAAGGC')], is_file_path=False)
program11.do_magic()

program12 = s.Search(text_or_file_path=t, word='GCGCGGAAAGGCGCGCGGAAAGGC', heuristics=[hh.Badcharacter('GCGCGGAAAGGCGCGCGGAAAGGC', alphabet)], is_file_path=False)
program12.do_magic()

import business_logic.util.graph as g
g.Graph().Drive([program, program2, program3, program4, program5, program6, program11, program10, program9, program8, program7, program12, program13, program14, program15, program16, program17])
