import tracemalloc
import time

import business_logic.string_search_alg as ss

class Search:
    """Class for searching word in tekst provided in FASTA file format"""
     
    def __init__(self, file_path, word, heuristics):
        """Constructor with FASTA file path"""
        self.__file_path = file_path
        self.__word = word
        self.__heuristics = heuristics
        self.__time = 0
        self.__memory = (0, 0)

    def __init__(self, text, word, heuristics):
        """Constructor with text for searching. Used for testings."""
        self.__text = text
        self.__word = word
        self.__heuristics = heuristics

    def open_file(self):
        """Open FASTA file"""
        # TODO
        pass

    def read_file(self):
        """Read bytes? from FASTA file"""
        # TODO
        pass

    def do_magic(self):
        """Apply a heuristic rule and return the number of alignments that can be skipped"""
        search = ss.Stringsearch(self.__heuristics)
        # start of monitoring memory allocation and time of execusion
        tracemalloc.start()
        start_time = time.time()

        # TODO: Replace text with file content?
        # run the algorithm
        sol = search.find(self.__text, self.__word)

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
        return "{time:.10f}".format(time=self.__time)

    def get_execution_memory(self):
        return "{}".format(self.__memory)

    def get_word(self):
        return self.__word

    def get_heuristics(self):
        h = type(self.__heuristics[0]).__name__
        if len(self.__heuristics) > 1:
            h += " + " + type(self.__heuristics[1]).__name__
        return "{}".format(h)



