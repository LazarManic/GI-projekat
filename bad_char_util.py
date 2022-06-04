

def dense_bad_char_tab(p:str, amap:dict)->list[list[int]]:
    """ Given pattern string and list with ordered alphabet characters, create
    and return a dense bad character table.  Table is indexed by offset
    then by character.
    function returns a list of lists containing integers,
    think of it as a matrix where each row represents 
    the occurence of each possible character
    (each character has a unique integer associated with it by amap,
    which is also its position in each row of matrix)
    previously in the string(relative to start of string) 
    """
    tab = []
    nxt = [0] * len(amap)
    for i in range(0, len(p)):
        c = p[i]
        assert c in amap
        tab.append(nxt[:])
        nxt[amap[c]] = i+1
    return tab