#!/usr/bin/env python
import random

def overlap(point, request):
    if point >= request['start'] and point <= request['end']:
        return True
    return False

def depth(requests):
    maxDepth = 1
    for request in requests:
        s = request['start']
        e = request['end']
        overlap_start = [r for r in requests if overlap(s, r)]
        overlap_end = [r for r in requests if overlap(e, r)]
        local_max_depth = max(len(overlap_start), len(overlap_end))
        maxDepth = max(local_max_depth, maxDepth)
    return maxDepth

def schedule_unlimited_resources(requests):
    d = depth(requests)
    requests.sort(key = lambda x: x['start'])
    for i in xrange(len(requests)):
        start = requests[i]['start']
        end = requests[i]['end']
        in_consideration = [True for x in xrange(d)]

        for request in requests[0:i]:
            if overlap(start, request) or overlap(end, request):
                if 'label' in request:
                    in_consideration[request['label']] = False

        requests[i]['label'] = in_consideration.index(True)
    return requests


def schedule_limited_resources(requests):
    '''
    greedy algorithm to schedule requests based on 'nearest end time'
    '''
    result = []
    # stick smallest end date on the end of the list for .pop()-ing
    requests.sort(key = lambda x: x['end'], reverse=True)
    # make a copy so as not to destroy original
    requests = requests[:]
    comparisons = 0
    while (len(requests) > 0):
        winner = requests.pop()
        result.append(winner)
        for i in xrange(len(requests) - 1, -1, -1):
            request = requests[i]
            comparisons += 1
            if request['start'] < winner['end']:
                requests.pop(i)

    return result, comparisons

def main():
    def create_random_requests(num = 300, time_unit_max = 8):
        requests = []
        for i in xrange(num):
            start = random.randint(0, time_unit_max)
            # can't start in the final time unit: every interval must be at
            # least len 1
            if start == time_unit_max:
                start -= 1
            end = random.randint(start, time_unit_max)
            while not (end > start):
                end = random.randint(start, time_unit_max)
            requests.append({'start': start, 'end': end})
        return requests

    def create_linear_requests(num = 30, time_unit_max = 8):
        requests = []
        for i in xrange(0, num - 1, 2):
            requests.append({'start': i, 'end': i+1})
        return requests

    def has_conflict(requests):
        for base in requests:
            start = base['start']
            end = base['end']
            label = base['label']
            for compare in requests:
                if compare == base:
                    continue
                if overlap(start, compare) or overlap(end, compare):
                    if compare['label'] == label:
                        return True
        return False

    rand_requests = create_random_requests(num = 5)
    #print schedule_limited_resources(rand_requests)
    #print depth(rand_requests)
    scheduled = schedule_unlimited_resources(rand_requests)
    print scheduled
    print "which has a depth of", depth(rand_requests), "and uses", len(set([x['label'] for x in scheduled])), "resources"
    print "does it have any conflicts?", has_conflict(scheduled)


if __name__ == '__main__':
    main()
