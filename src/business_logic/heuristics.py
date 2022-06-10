## Implement a strategy design pattern for different heuristics
class IHeuristicstrategy:
    """Class serves as a interface for heuristic rules, 
    that evaluate which alignments to skip when comparing two strings"""
    def __init__(self, word_len:int):
        pass
    def match_skip(self)->int:
        """Return amount to shift after a match occured"""
        pass

    def apply_rule(self, match_string:str, i:int, j:int)->int:
        """Apply a heuristic rule and return the number of alignments that can be skipped"""
        pass



import business_logic.util.bad_char_util as bc

class Badcharacter(IHeuristicstrategy):
    """Class implements the 'bad character' heuristic rule """
    def __init__(self, word:str, alphabet: str):
        IHeuristicstrategy.__init__(self, len(word))

        
        #Construct a map that maps each valid character(that can occur in matching string) to a unique integer 
        self.amap = {char:i for i,char in enumerate(alphabet)}
        
        self.bad_char = bc.dense_bad_char_tab(word, self.amap)

    def get_amap(self):
        return self.amap

    def get_bad_char(self):
        return self.bad_char

    def match_skip(self)->int:
        return 1

    def bad_character_rule(self, i:int, c:str)->int:
        """ Return # skips given by bad character rule at offset i """
        assert c in self.amap
        ci = self.amap[c]
        assert i > (self.bad_char[i][ci]-1)
        return i - (self.bad_char[i][ci]-1)
    
    
    def apply_rule(self, match_string:str, i:int, j:int)->int:
        
        # Get alignment shift from the bad character matrix, based on the character in position
        return self.bad_character_rule(j,match_string[i+j])





import business_logic.util.good_suffix_util as gs
    
class Goodsuffix(IHeuristicstrategy):
    """ Class implements the good suffix strategy"""
    def __init__(self, word:str): 
        IHeuristicstrategy.__init__(self, len(word))
        ## Create good suffix rule table
        _, self.big_l, self.small_l_prime = gs.good_suffix_table(word)

    def match_skip(self)->int:
        return len(self.small_l_prime) - self.small_l_prime[1]

    def good_suffix_rule(self, i:int)->int:
        """ Given a mismatch at offset i, return amount to shift
            as determined by (weak) good suffix rule. """
        length = len(self.big_l)
        assert i < length
        if i == length - 1:
            return 0
        i += 1  ## i points to leftmost matching position of P
        if self.big_l[i] > 0:
            return length - self.big_l[i]
        return length - self.small_l_prime[i]
    

    def apply_rule(self, match_string:str, i:int, j:int)->int:
        return self.good_suffix_rule(j)




class RLongestGap(IHeuristicstrategy):

    def __init__(self, word:str):
        IHeuristicstrategy.__init__(self, len(word))
        self.jump_vec = RLongestGap.get_jump_vector(word)
    
    def match_skip(self)->int:
        return self.jump_vec[0]

    @staticmethod
    def get_jump_vector(word:str):

        sol = [1]*(len(word)+1)

        char_dict = {}
        for i, c in enumerate(word):
            if c in char_dict:
                char_dict[c].append(i)
            else:
                char_dict[c] = [i]            
        
        for arr in char_dict.values():
            arr.append('#')


        max_jump = 1
        for i, c in reversed(list(enumerate(word))):

            assert c in char_dict
            arr = char_dict[c]

            if len(char_dict[c]):
                next_i = char_dict[c].pop()
                if next_i == '#':
                    jump =  len(word) - i
                else:
                    jump = next_i - i 

            else:
                jump = len(word) - i 
            
            if max_jump < jump:
                max_jump = jump

            sol[i] = max_jump 

        return sol
    

    def apply_rule(self, match_string:str, i:int, j:int)->int:
        return  self.jump_vec[j+1]




class LolngestGap(IHeuristicstrategy):

    def __init__(self, word:str):
        IHeuristicstrategy.__init__(self, len(word))
        self.jump_vec = LolngestGap.get_jump_vector(word)

    def match_skip(self)->int:
        return self.jump_vec[0]

    @staticmethod
    def get_jump_vector(word:str):

        sol = [1]*(len(word)+1)

        char_dict = {}
        for i, c in enumerate(word):
            if c in char_dict:
                char_dict[c].append(i)
            else:
                char_dict[c] = [i]

        for i, c in reversed(list(enumerate(word))):
            assert c in char_dict
            arr = char_dict[c]

            if len(arr) > 1:
                next_i = char_dict[c].pop() - char_dict[c][len(arr) - 1]
            else:
                next_i = char_dict[c].pop() + 1

            if sol[i+1] > next_i:
                sol[i] = sol[i+1]
            else:
                sol[i] = next_i

        sol[0] = sol[1]
        return sol

    def apply_rule(self, match_string:str, i:int, j:int)->int:
        return  self.jump_vec[j+1]
