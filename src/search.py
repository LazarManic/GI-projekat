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

    def get_heuristics(self):
        h = type(self.__heuristics[0]).__name__
        if len(self.__heuristics) > 1:
            h += " + " + type(self.__heuristics[1]).__name__
        return "{}".format(h)

