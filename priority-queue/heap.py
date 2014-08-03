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
            rightMoreExtreme = self.cmp(self.tree[left], self.tree[right])
            if rightMoreExtreme:
                j = right
            else:
                j = left

        elif two_i == n:
            j = two_i

        if self.cmp(self.tree[i], self.tree[j]):
            self.tree[i], self.tree[j] = self.tree[j], self.tree[i]
            self._heapify_down(j)


    def delete(self, index):
        if len(self.tree) == 0:
            return {}

        if len(self.tree) == 1:
            return self.tree.pop()

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

    def peek(self):
        if len(self.tree) == 0:
            return False

    def to_list(self):
        tree = self.tree[:]
        ret = []

        done = False
        while not done:
            top = self.get()
            if top:
                ret.append(top)
            else:
                done = True

        self.tree = tree
        return ret

def verify(heap):
    for i in xrange(len(heap.tree)):
        compare = heap.tree[i]
        child = i * 2 + 1
        # no child nodes
        if child + 1 >= len(heap.tree):
            continue
        a, b = heap.tree[child], heap.tree[child + 1]
        if heap.cmp(compare, a):
            print ""
            print "NOT OK- i:", i
            print "bad child, a:", child, "value: ", a
            print "tree: ", str(heap.tree)
            print
            return False
        if heap.cmp(compare, b):
            print ""
            print "NOT OK- i:", i
            print "bad child b:", child + 1, "value: ", b
            print "tree: ", str(heap.tree)
            print
            return False

    return str(heap.tree) + " is ok"


def main():
    h = Heap(lambda x, y: x > y)
    members = [43, 2, 38, 12, 31]
    for key in members:
        h.insert(key)

    print h.to_list()

if __name__ == '__main__':
    main()
