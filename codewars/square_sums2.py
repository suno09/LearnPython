from math import sqrt
from time import time
from collections import defaultdict
from pprint import pprint


class Number:
    def __init__(self, n, prv, nxt):
        self.n = n
        self.prv = prv
        self.nxt = nxt


def gen_seq(num):
    sequences = []
    while sequences.__len__() < num:
        
        pass


def square_sums(num):
    """ generate dict for get all numbers graph """
    sequences = defaultdict(list)

    for n in range(num, 0, -1):
        max_square = int(sqrt(n + num)) ** 2
        while max_square > n:
            diff = max_square - n
            if diff != n:
                sequences[n].append(max_square - n)
            max_square = max_square - int(sqrt(max_square)) * 2 + 1

    return sequences
    # """ generate graph """
    # pass


if __name__ == '__main__':
    # for i in range(1, 38):
    # for i in [5, 15, 23, 27, 37, 1000]:
    for i in [15]:
        start = time()
        ss = square_sums(i)
        end = time()
        pprint(ss)
        print(f'{i} for ss {end - start} s')
        # squares = [j ** 2 for j in range(2, int(math.sqrt(i * 2)) + 1)]
        # if ss:
        #     for j in range(ss.__len__()-1):
        #         if j % 2:
        #             print(f'    {ss[j]:2}, {ss[j + 1]:2} => {ss[j] + ss[j + 1]}')
        #         else:
        #             print(f'{ss[j]:2}, {ss[j + 1]:2} => {ss[j] + ss[j + 1]}')

        print()
