#!/usr/bin/env python

class Heap(object):
    '''
    a heap implementation with customizable comparison function. 
    defaults to min heap
    '''
    def __init__(self, root, compare = lambda x, y: x > y):
        self.cmp = compare
        self.tree = [root]

    def _heapify_up(self, i):
        if i > 0:
            j = i/2
            if self.cmp(self.tree[j], self.tree[i]):
                self.tree[i], self.tree[j] = self.tree[j], self.tree[i]
                self._heapify_up(j)

    def _heapify_down(self, i):
        n = len(self.tree)
        j = None
        two_i = 2*i
        if two_i > n:
            return
        elif two_i < n:
            left, right = two_i, two_i + 1
            j = min(self.tree[left], self.tree[right])
            pass
        elif two_i == n:
            j = two_i

        if self.tree[j] < self.tree[i]:
            self.tree[i], self.tree[j] = self.tree[j], self.tree[i]
            self._heapify_down(j)


    def delete(self, index):
        pass

    def insert(self, elem):
        self.tree.append(elem)
        self._heapify_up(len(self.tree) - 1)

    def get(self):
        pass

    def find(self):
        return self.tree[0]


def verify(heap):
    for i in xrange(len(heap.tree)):
        compare = heap.tree[i]
        child = i * 2
        # no child nodes
        if child + 1 >= len(heap.tree):
            continue
        a, b = heap.tree[child], heap.tree[child+1]
        if heap.cmp(compare, a) or heap.cmp(compare, b):
            return False

    return True

def main():
    h = Heap(11)
    h.insert(3)
    print verify(h)
    h.insert(5)
    print verify(h)
    h.insert(8)
    print verify(h)
    h.insert(4)
    print verify(h)
    print "t", h.tree
    print "inserting 15"
    h.insert(15)

    print "i", range(len(h.tree))
    print "t", h.tree
    print verify(h)
    
if __name__ == '__main__':
    main()
