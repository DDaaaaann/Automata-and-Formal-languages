from Automata import *

test = 'babbbaab'
string = list(test)


# Zelf implementeren??
def iterate(string):
    for i in string:
        if not M.move(i):
            return False
    if M.current_state.final_state:
        return True
    return False


# Zelf delta van csv omzetten naar dict?



Q = [0, 1, 2, 3]
Sigma = ['a', 'b']
delta = {0:{'a':1, 'b':0},
        1:{'a':2, 'b':1},
        2:{'a':3, 'b':2},
        3:{'a':3, 'b':3}}
s = 0
F = [3]
M = FA(Q, Sigma, delta, s, F)

print iterate(string)
