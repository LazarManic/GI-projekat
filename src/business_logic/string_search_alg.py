


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
        num_heur = len(self.__heuristics)

        ## list contains the order of iteration through the word for each heuristic (list of lists)
        iter_orders = self.get_heuristic_iter_orders()

        while i < len(t) - len(p) + 1:
            shift = 1
            mismatched = False
            
            ## Iterate through small string in reverse order (like Boyer-Moore)
            for k, index in enumerate(zip(*iter_orders)):

                ## Each heuristic might check different index 
                for l in range(num_heur):
                    ## Fetch position of character to be checked by heuristic
                    j = index[l]
                    if p[j] != t[i+j]:
                        ## Init shift values of every heuristic to 0
                        heur_shifts = [0]*(num_heur)
                        heur = self.__heuristics[l]
                        heur_shifts[l] = heur.apply_rule(t, p, i, j) 
                        ## Go through all other heuristics and find where all mismatches occured

                        for n in range(l+1, num_heur):
                            j = index[n]
                            if p[j] != t[i+j]:
                                heur = self.__heuristics[n]
                                ## Calculate shift 
                                heur_shifts[n] = heur.apply_rule(t, p, i, j)
                    
                        ## Get the maximum shift from heuristics
                        heur_maxshift = max(heur_shifts) 

                        ## If every heuristic shift value was 0, move instead by 1 
                        shift = max(shift, heur_maxshift)
                        mismatched = True
                        break
                if mismatched:
                    break
            
            
            ## If a match occured, append the position where it occured 
            ## and shift alignments based on the heuristics
            if not mismatched:
                occurrences.append(i)
                skip = self.match_skip()
                
                shift = max(shift, skip)
            
            i += shift
        return occurrences

