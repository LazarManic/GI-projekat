


import numpy as np

class Stringsearch():
    """Class is used for implementing a heuristic based string search,
    where a heuristic defines how much alignments to skip after a mismatch or a match"""


    def __init__(self, heuristics:list = []):
        """Constructor takes a list of heuristics(as function pointers) 
        that help define when/how much to move while iterating through 
        a string while trying to match"""
        
        self.__heuristics = heuristics


    def get_heuristic_iter_orders(self):
        """Return iteration orders when comparing word to big string for each heuristic"""
        sol = []
        for heur in self.__heuristics:
            sol.append(heur.index)
        return sol
    
    def match_skip(self):
        """When a match occurs, calculate the maximum distance that can be skipped without missing match alignments""" 
    
        ## Init skip, find max skip value from heuristisc
        skip = 0 

        ## Iterate through heuristiscs
        for heur in self.__heuristics:
            res = heur.match_skip()
            if skip < res:
                skip = res
            
        return skip


    def find(self, t:str, p:str):
        """Find the number of times the substring occurs in the match_string. t - is the big string, p - is the small string
        Iterating mimics Boyer-Moore algorithm"""

        i = 0
        occurrences = []
        cnt = 0
        while i < len(t) - len(p) + 1:
            shift = 1
            mismatched = False
            ## Iterate through small string in reverse order (like Boyer-Moore)
            for j in range(len(p)-1, -1, -1):
                cnt += 1
                if p[j] != t[i+j]:
                    
                    ## Init shift values of every heuristic to 0
                    heur_shifts = [0]*len(self.__heuristics)
                    
                    ## Calculate shift by every heuristic rule
                    for k, heur in enumerate(self.__heuristics):
                        heur_shifts[k] = heur.apply_rule(t,p,i,j)
                    
                    ## Get the maximum shift from heuristics
                    heur_maxshift = max(heur_shifts) 

                    ## If every heuristic shift value was 0, move instead by 1 
                    shift = max(shift, heur_maxshift)
                    mismatched = True
                    break
            
            ## If a match occured, append the position where it occured 
            ## and shift alignments based on the heuristics
            if not mismatched:
                occurrences.append(i)
                skip = self.match_skip()
                
                shift = max(shift, skip)
            
            i += shift
        return occurrences

