from BoggleWord import *

class PriorityQueue(object):
    """
    Class. Implements a priority queue using a min heap.
    """

    def __init__(self):
        """
        Constructor. Creates an empty queue.
        """        
        self.queue = [None]

        
    @staticmethod
    def getParent(index):
        return index/2
    

    @staticmethod
    def getLeft(index):
        return 2 * index
    
    
    @staticmethod
    def getRight(index):
        return 2 * index  + 1
    

    def getSize(self):
        """
        Observer. Returns the number of items queued.
        """
        return len(self.queue) - 1

    
    def swap(self, a, b):
        """
        Mutator. Performs a swap between elements at indices a and b.
        """
        self.queue[a], self.queue[b] = self.queue[b], self.queue[a]


    def push(self, element):
        """
        Mutator. Inserts element into this priority queue.
         @params:
          element: the element to be inserted. Element must have an attribute key, which is 
                   a comparable used to compare cost with other elements present in the heap
        """
        
        # begin by inserting item at the end of the heap
        self.queue.append(element)

        # will be used to track the current index of the element
        element_index = self.getSize()

        while (PriorityQueue.getParent(element_index) > 0):

            if element.key >= self.queue[PriorityQueue.getParent(element_index)].key:
                # element is in the correct position
                break

            # swap child with its parent
            self.swap(element_index, PriorityQueue.getParent(element_index))

            # update index of element
            element_index = PriorityQueue.getParent(element_index)
        

    def popMin(self):
        """
        Mutator. Removes and returns the element at the front of the queue.
        caller must check whether queue is empty before making a call.
        """
        # assert queue is not empty
        assert self.getSize() > 0
        

        # save element at front of the queue
        front = self.queue[1]

        if (self.getSize() == 1):
            # corner case.
            del self.queue[1]
            return front

        
        # move last element to the first position
        self.queue[1] = self.queue[self.getSize()]
        del self.queue[self.getSize()]

        # will be used to track the current index of the element
        element_index = 1
        
        while PriorityQueue.getLeft(element_index) <= self.getSize():

            # get left and right indices
            left_index = PriorityQueue.getLeft(element_index)
            right_index = PriorityQueue.getRight(element_index)

            # get index of lowest of left and right elements
            child_index = 0
            if PriorityQueue.getRight(element_index) <= self.getSize() and self.queue[right_index].key < self.queue[left_index].key:
                child_index = right_index
            else:
                child_index = left_index

            if self.queue[child_index].key >= self.queue[element_index].key:
                # element is in correct position
                break

            # swap the element with its child
            self.swap(element_index, child_index)

            # update the current element index
            element_index = child_index

        return front
        
        
    def isEmpty(self):
        """
        Observer. Returns true if there are no items queued
        """
        return self.getSize() == 0


    def checkRepresentationInvariant(self):
        """
        Observer. Asserts that min-heap properties are not violated.
        Used for testing
        """

        for i in range(1, self.getSize() + 1):

            # get left and right children indices
            left_index = PriorityQueue.getLeft(i)
            right_index = PriorityQueue.getRight(i)

            # check left child index is within boundaries
            if left_index > self.getSize():
                return

            # check left child obeys min-heap properties
            assert self.queue[i].key <= self.queue[left_index].key

            # check right child index is within boundaries
            if right_index > self.getSize():
                return

            # check right child obeys min-heap properties
            assert self.queue[i].key <= self.queue[right_index].key
            
                
    def printQueue(self):
        """
        Observer. Prints the elements present in self.queue to 
        the standard output stream. Used for testing.
        """

        # print opening bracket
        print '['

        # print elements with their keys
        for i in range(1, self.getSize() + 1):
            print str(element.key) + ' ' 

        # closing bracket and end of line
        print "]\n"
            
        

        


def test():
    """
    Helper function which tests the priority queue implementation.
    Could use more thorough testing...
    """
    
    pq = PriorityQueue()
    
    for i in range(1000):
        pq.push(BoggleWord('a', i, [], 0))
        pq.checkRepresentationInvariant()
        
    for i in range(1000):
        pq.popMin()
        pq.checkRepresentationInvariant()

    

