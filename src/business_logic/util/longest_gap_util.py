
def get_jump_vector_right(word:str):

    sol = [1]*(len(word)+1)
    char_dict = get_char_dict(word)
    for arr in char_dict.values():
        arr.append('#')

    max_jump = 1
    for i, c in reversed(list(enumerate(word))):

        assert c in char_dict
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


def get_jump_vector_left(word:str):

    sol = [1]*(len(word)+1)
    char_dict = get_char_dict(word)

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


def get_char_dict(word:str):
    char_dict = {}
    for i, c in enumerate(word):
        if c in char_dict:
            char_dict[c].append(i)
        else:
            char_dict[c] = [i]            

    return char_dict