from PriorityQueue import *
from BoggleWord import *

# these constants should really be in the main function.
# I should create a Board class that gets contains these variables
WIDTH_OF_BOARD = 4
HEIGHT_OF_BOARD = 4

VISITED_BLANK_ARRAY = [0] * WIDTH_OF_BOARD * HEIGHT_OF_BOARD


def mapToInt(row, col):
    """
    Helper function which maps the row and col to a single integer
    """
    return row * WIDTH_OF_BOARD + col


def mapToRowCol(x):
    """
    Helper function which complements mapToInt() by reversing the mapping.
    """
    row = x / WIDTH_OF_BOARD
    col = x % WIDTH_OF_BOARD

    return row, col


def getMoves(position):
    """
    Helper iterator that generates moves for the given position
    """
    if position + 1 < WIDTH_OF_BOARD * HEIGHT_OF_BOARD:
        yield position + 1

    if position - 1 >= 0:
        yield position - 1

    if position - WIDTH_OF_BOARD >= 0:
        yield position - WIDTH_OF_BOARD

    if position + WIDTH_OF_BOARD < WIDTH_OF_BOARD * HEIGHT_OF_BOARD:
        yield position + WIDTH_OF_BOARD

        
def findWords(board, dictionary, row, col):
    """
    Function which prints each word that can be found according to the Boggle Rules
     @params:
      board: a buggle board as a simple 2D array of characters
      dictionary: a class implementing a dictionary of all english words
      row, col: the first node visited from the board.
    """
    
    # instantiate priority queue
    pq = PriorityQueue()

    # add element at (row, col) to the queue.
    # key does not matter as it will be popped first
    visited = VISITED_BLANK_ARRAY[:]
    visited[mapToInt(row, col)] = 1
    boggleWord = BoggleWord(board[row][col], 0, visited, mapToInt(row, col))
    pq.push(boggleWord)
    
    while not pq.isEmpty():

        # pop min element
        boggleWord = pq.popMin()

        if dictionary.isWord(boggleWord.word):
            print boggleWord.word

        if not dictionary.isPrefix(boggleWord.word):
            continue

        # now we may expand
        for move in getMoves(boggleWord.position):

            # skip element if it has been visited
            if boggleWord.visited[move]:
                continue

            # add it to the queue
            r, c = mapToRowCol(move)
            word = boggleWord.word + board[r][c]
            cost = dictionary.getCost(word)
            visited = boggleWord.visited[:]
            visited[move] = 1

            pq.push(BoggleWord(word, cost, visited, move))


            

            
        

    
