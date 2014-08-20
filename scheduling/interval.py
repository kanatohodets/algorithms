#!/usr/bin/env python
import random

def schedule(requests):
    '''
    greedy algorithm to schedule requests based on 'nearest end time'
    '''
    result = []
    # stick smallest end date on the end of the list for .pop()-ing
    requests.sort(key = lambda x: x['end'], reverse=True)
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
        for i in xrange(num - 1):
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

    def create_linear_requests(num = 300, time_unit_max = 8):
        requests = []
        for i in xrange(0, num - 1, 2):
            requests.append({'start': i, 'end': i+1})
        return requests


    print schedule(create_random_requests())

if __name__ == '__main__':
    main()
