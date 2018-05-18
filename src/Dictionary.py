class Dictionary(object):
    """
    Class. Implements a dummy dictionary for the purposes of the exercise
    If properly carried out, this dictionary would be implemented using a tries 
    data structure.
    """

    def __init__(self, words):
        """
        Constructor.
        """
        self.words = words


    def isWord(self, word):
        """ 
        Returns true if word is in this dictionary
        """
        return word in self.words

    def isPrefix(self, word):
        """
        Returns true if word is a prefix of a word in this dictionary.
        Since this is a dummy, it always returns true.
        """
        return True

    def getCost(self, word):
        """
        Returns the cost of a word. Since this is a dummy class, this simply  
        returns the cost as the negative length of the word
        """
        return -len(word)
