#!/usr/bin/env python
import random

length = 3

def generate_individual(i):
    individual = {}
    individual['name'] = i
    individual['partner'] = -1
    individual['pref'] = random.sample(range(0, length), length)
    return individual

women = [generate_individual(i) for i in xrange(length)]
men = [generate_individual(i) for i in xrange(length)]

free = women[:]

# the prefs are a stack that work from the end of the list, but
# it's easier to read preferences from left to right
for woman in women:
    print "woman", woman['name'], 'has prefs: ', woman['pref'][::-1]

for man in men:
    print "man", man['name'], 'has prefs: ', man['pref'][::-1]

while len(free) > 0:
    eligible_woman = free.pop()
    while len(eligible_woman['pref']) > 0:
        compare = eligible_woman['pref'].pop()
        man = men[compare]
        man_prefs = man['pref']
        man_current_partner = man['partner']
        try:
            current_partner_rank = man_prefs.index(man_current_partner['name'])
            eligible_woman_rank = man_prefs.index(eligible_woman['name'])
            if eligible_woman_rank > current_partner_rank:
                man['partner'] = eligible_woman
                eligible_woman['partner'] = man
                free.append(man_current_partner)
                break
        except TypeError:
            man['partner'] = eligible_woman
            eligible_woman['partner'] = man
            break

print

result = set([(woman['name'], woman['partner']['name']) for woman in women])
print result
