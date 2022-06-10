import tracemalloc
import time

import business_logic.string_search_alg as ss
import business_logic.heuristics as hh

class Search():
    """Class for searching word in tekst provided in FASTA file format"""
     
    def __init__(self, file_path:str="", text:str="", word:str="", heuristics:list[hh.IHeuristicstrategy]=None):
        """Constructor with FASTA file path or with text"""
        self.word = word
        self.__heuristics = heuristics
        self.__time = 0
        self.__memory = (0, 0)
        self.__search = ss.Stringsearch(self.__heuristics)
        self.__file_path = file_path
        self.text = text

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

    def search_text(self):
        return self.__search.find(self.text, self.word)

    def search_fasta(self):
        _, self.text = Search.read_fasta(self.__file_path)
    
        return self.__search.find(self.text, self.word)

    def search_fasta_as_datastream(self, chunk_size:int = 1000):

        file_obj = open(self.__file_path)
        overlap = len(self.word)
        prepend = ""

        # Read defline
        file_obj.readline()

        offset = 0
        sol = []
        while True:

            data = file_obj.read(chunk_size)
            if not data:
                break
            data = prepend + data
            data = data.replace('\n', '')
            data_sz = len(data)
            sol_chunk = self.__search.find(data, self.word)
            sol_chunk = [align if offset == 0 else offset + align for align in sol_chunk]
            sol = sol + sol_chunk
            offset = offset + data_sz - overlap
            prepend = data[-overlap:] 


        return sol


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

