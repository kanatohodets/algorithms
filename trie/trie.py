#!/usr/bin/env python

# using dicts feels a bit like cheating, here
# still, they'll always be quite sparsely populated with very little chance of
# hash collisions

# this tree is obviously fairly bloated -- next step is a radix tree, to
# compress things.
class Trie(object):
    def __init__(self):
        self.root = {}

    def search(self, search):
        workingNode = self.root
        # move workingNode to the point in the tree
        # where the search prefix ends.
        level = 0
        for prefix in search:
            if not workingNode.has_key(prefix):
                break
            else:
                level += 1
                workingNode = workingNode[prefix]

        # no complete values will be found: search term is too long
        if len(search) > level:
            return []

        def traverse(node, string, collect):
            if len(node.keys()) == 0:
                collect.append(string)
                return collect

            if string == search:
                collect.append(string)

            for key in node:
                collect = traverse(node[key], string + key, collect)
            return collect

        results = traverse(workingNode, search, [])
        return results

    def insert(self, data):
        workingNode = self.root
        for prefix in data:
            if not workingNode.has_key(prefix):
                workingNode[prefix] = {}
            workingNode = workingNode[prefix]


if __name__ == '__main__':
    t = Trie()
    #t.insert("bob has three plates")
    #t.insert("bob has three pineapples")
    t.insert("jane can run fast")
    t.insert("jane can run a business")
    t.insert("j")
    t.insert("joe")
    t.insert("job")
    t.insert("jo")
    #print "bob", t.search("bob")
    print "jane", t.search("jane")
    print "j", t.search("j")
    print "jo", t.search("jo")
    #print "joe", t.search("joe")
    print "joerb", t.search("joerb")
