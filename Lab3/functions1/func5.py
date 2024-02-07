from itertools import *

def permutations_string(str):

    return (''.join(elem) for elem in permutations(str, len(str)))


