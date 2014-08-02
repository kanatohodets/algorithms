#!/usr/bin/env python

class Heap(object):
    '''
    A heap implementation with customizable comparison function.

    The major benefit of this (aside from easily allowing a switch between
    min heap and max heap) is the ability to stuff complex objects into the
    heap with a suitable lambda for comparing them (properties, dict lookups,
    position in some other list, etc).

    defaults to min heap of simple comparison of the keys
    '''
    def __init__(self, compare = lambda x, y: x > y):
        self.cmp = compare
        self.tree = []

    def _heapify_up(self, i):
        if i > 0:
            j = i/2
            if self.cmp(self.tree[j], self.tree[i]):
                self.tree[i], self.tree[j] = self.tree[j], self.tree[i]
                self._heapify_up(j)

    def _heapify_down(self, i):
        n = len(self.tree) - 1
        j = None
        two_i = 2*i
        if two_i > n:
            return
        elif two_i < n:
            left, right = two_i, two_i + 1 
            # use the compare func to determine which index (left/right) has the
            # more extreme value in the tree
            j = sorted([left, right], cmp=lambda x, y: self.cmp(self.tree[x], self.tree[y])).pop()
        elif two_i == n:
            j = two_i

        if self.cmp(self.tree[i], self.tree[j]):
            self.tree[i], self.tree[j] = self.tree[j], self.tree[i]
            self._heapify_down(j)


    def delete(self, index):
        if len(self.tree) == 0:
            return False

        self.tree[index] = self.tree.pop()
        self._heapify_down(index)

    def insert(self, elem):
        self.tree.append(elem)
        self._heapify_up(len(self.tree) - 1)

    def get(self):
        if len(self.tree) == 0:
            return False

        old_root = self.tree[0]
        self.delete(0)
        return old_root

    def find(self):
        if len(self.tree) == 0:
            return False

        return self.tree[0]


def verify(heap):
    for i in xrange(len(heap.tree)):
        compare = heap.tree[i]
        child = i * 2 + 1
        # no child nodes
        if child + 1 >= len(heap.tree):
            continue
        a, b = heap.tree[child], heap.tree[child + 1]
        if heap.cmp(compare, a): 
            print "index i: ", i, " has a too extreme child, a: ", child, "value: ", a
            print heap.tree
            return False
        if heap.cmp(compare, b):
            print "index i: ", i, " has a too extreme child, b: ", child, "value: ", b
            print heap.tree
            return False

    return str(heap.tree) + " is ok"
 

def main():
    h = Heap()
    h.insert(11)
    h.insert(3)
    h.insert(5)
    h.insert(8)
    h.insert(4)
    print "t", h.tree
    print "inserting 15", 
    h.insert(15)
    print verify(h)
    print "pre-get tree",  verify(h)
    print "getting root: ", h.get()
    print "post get tree", verify(h)
    h.delete(2)
    print "post delete 2", verify(h)
    
if __name__ == '__main__':
    main()
