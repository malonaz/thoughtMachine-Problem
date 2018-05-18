

class BoggleWord(object):
    """
    Class. Implements a boggle Word.
     @attributes:
      word: the word of this boggle word
      key: the cost of this word, to be used in a priority queue
      visited: the nodes that were visited to create this word
      position: the last node that was visited to create this word
    """

    def __init__(self, word, key, visited, position):
        """
        Constructor.
        """
        self.word = word
        self.key = key
        self.visited = visited
        self.position = position

    def getWord(self):
        """
        Observer. Getter function which returns the element
        """
        return self.word


    def visited(self, index):
        """
        Observer. Returns true if this element has visited the given index.
        """
        return self.visited[index]

    

