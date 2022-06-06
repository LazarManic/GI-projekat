import tracemalloc
import time

import business_logic.string_search_alg as ss
import business_logic.heuristics as hh

class Search():
    """Class for searching word in tekst provided in FASTA file format"""
     
    def __init__(self, file_path:str, word:str, heuristics:hh.IHeuristicstrategy):
        """Constructor with FASTA file path"""
        self.__file_path = file_path
        self.word = word
        self.__heuristics = heuristics
        self.__time = 0
        self.__memory = (0, 0)
        self.__search = ss.Stringsearch(self.__heuristics)
        _, self.text = Search.read_fasta(self.__file_path)
    
    def __init__(self, text:str, word:str, heuristics:hh.IHeuristicstrategy):
        """Constructor with text"""
        self.text = text
        self.word = word
        self.__heuristics = heuristics
        self.__time = 0
        self.__memory = (0, 0)
        self.__search = ss.Stringsearch(self.__heuristics)

    @staticmethod
    def read_fasta(file_path:str):
        """Read bytes? from FASTA file"""
        defline = ''
        sequence = ''
        file = open(file_path)
        for line in file:
            if line[0] == '>':
                defline = line.strip()
                defline = defline.replace('>', '')
            else:
                sequence += line.strip()
        return (defline, sequence)



    def do_magic(self):
        """Apply a heuristic rule and return the number of alignments that can be skipped"""
        # start of monitoring memory allocation and time of execusion
        tracemalloc.start()
        start_time = time.time()

        # run the algorithm
        sol = self.__search.find(self.text, self.word)

        # end of monitoring memory allocation and time of execusion
        end_time = time.time()
        memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        self.__time = end_time - start_time
        # memory at its peak - memory at start point
        self.__memory = memory[1] - memory[0]

        print("Number of occurences: {0}, indexes:{1}".format(len(sol), sol))
        print("Execution time: {time:.10f}, execution memory peak: {mem} KiB".format(time = self.__time, mem = self.__memory))

    def get_execution_time(self):
        return self.__time

    def get_execution_memory(self):
        return self.__memory

    def get_word(self):
        return self.word

    def get_heuristics(self):
        h = type(self.__heuristics[0]).__name__
        if len(self.__heuristics) > 1:
            h += " + " + type(self.__heuristics[1]).__name__
        return "{}".format(h)

