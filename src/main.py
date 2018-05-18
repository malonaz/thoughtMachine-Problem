from PriorityQueue import *
from BoggleWord import *
from Dictionary import *
from BoggleSolver import *


# constants of the game

BOARD = [['a', 'b', 'c', 'd'],
         ['a', 'm', 'y', 'e'],
         ['t', 's', 'u', 'v'],
         ['b', 's', 't', 'e']]



DICTIONARY = Dictionary(["my", "deve"])


for row in range(HEIGHT_OF_BOARD):
    for col in range(WIDTH_OF_BOARD):
        findWords(BOARD, DICTIONARY, row, col)
