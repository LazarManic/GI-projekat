




class Stringmatch():


    def __init__(self, heuristics:list = []):
        """Constructor takes a list of heuristics(as function pointers) 
        that help define when/how much to move while iterating through 
        a string while trying to match"""
        
        self.__heuristics = heuristics



    def find(self, match_string:str, substring:str):
        """Find the number of times the substring occurs in the match_string"""
        pass


