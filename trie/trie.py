#!/usr/bin/env python

def _search_traverse(node, string, collect):
    if len(node.keys()) == 0:
        collect.append(string)
        return collect

    for key in node:
        collect = _search_traverse(node[key], string + key, collect)
    return collect

# using dicts feels a bit like cheating, here
# still, they'll always be quite sparsely populated with very little chance of
# hash collisions

# this tree is obviously fairly bloated -- next step is a radix tree, to
# compress things.
class Trie(object):
    def __init__(self):
        self.root = {}

    def search(self, key):
        workingNode = self.root
        # move workingNode to the point in the tree
        # where the search prefix ends.
        for prefix in key:
            if not workingNode.has_key(prefix):
                return []
            else:
                workingNode = workingNode[prefix]

        results = _search_traverse(workingNode, key, [])
        return results

    def insert(self, data):
        workingNode = self.root
        for prefix in data:
            if not workingNode.has_key(prefix):
                workingNode[prefix] = {}
            workingNode = workingNode[prefix]


if __name__ == '__main__':
    t = Trie()
    t.insert("bob has three plates")
    t.insert("bob has three pineapples")
    t.insert("jane can run fast")
    t.insert("jane can run a business")
    t.insert("joe")
    print t.root
    print len(t.root)
    print t.search("bob")
    print t.search("jane")
    print t.search("j")
