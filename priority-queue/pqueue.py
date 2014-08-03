#!/usr/bin/env python

import random
from heap import Heap, verify

class pqueue(object):
    def __init__(self, cmp = lambda x, y: x < y):
        self.h = Heap(cmp)

    def insert(self, item):
        self.h.insert(item)
        pass

    def get(self):
        return self.h.get()

    def peek(self):
        return self.h.peek()


if __name__ == '__main__':
    def make_example_member():
        ret = {
            'pri': random.randint(0, 100),
            'd': ''.join([l if random.random() < 0.1 else '' for l in "abcdefghijklmnopqrstuvqxwz"])
        }
        return ret

    p = pqueue(lambda x, y: x['pri'] < y['pri'])

    members = [make_example_member() for i in range(5)]

    print "members: ", members
    for member in members:
        p.insert(member)

    print "tree", p.h.tree

    done = False
    while not done:
        top = p.get()
        if top:
            print top, p.h.to_list()
        else:
            done = True
