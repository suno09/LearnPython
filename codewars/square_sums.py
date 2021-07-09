import math
from time import time


def square_sums(num):
    start = time()
    if num < 1 or num > 1000:
        return False

    l_num = [num]
    n = num - 1

    while True:
        # print(l_num)
        rnums = filter(lambda x: x not in l_num, range(n, 0, -1))
        for i in rnums:
            pi = l_num[-1] + i
            if int(math.sqrt(pi) + 0.5) ** 2 == pi:
                l_num.append(i)
                n = num
                break
        else:
            n = l_num.pop() - 1
            if not l_num:
                if n == 0:
                    break
                else:
                    l_num.append(n)
                    n = num

        if l_num.__len__() == num:
            break

    print(f'time {time() - start} s')
    return l_num if l_num else False


def square_sums2(num):
    start = time()
    if num < 1 or num > 1000:
        return False

    l_num = [num]
    n = num - 1

    while True:
        # print(l_num)
        rnums = filter(lambda x: x not in l_num, range(n, 0, -1))
        for i in rnums:
            pi = l_num[-1] + i
            if int(math.sqrt(pi) + 0.5) ** 2 == pi:
                l_num.append(i)
                n = num
                break
        else:
            n = l_num.pop() - 1
            if not l_num:
                if n == 0:
                    break
                else:
                    l_num.append(n)
                    n = num

        if l_num.__len__() == num:
            break

    print(f'time {time() - start} s')
    return l_num if l_num else False


def square_sums3(num):
    if num < 1 or num > 1000:
        return False

    max_square = int(math.sqrt(num * 2 - 1)) ** 2
    ps = max_square
    l_num = [num]
    while True:
        n = ps - l_num[-1]
        while n > 0 and (n > num or n in l_num):
            n = n - int(math.sqrt(n + l_num[-1])) * 2 + 1

        if 0 < n <= num:
            l_num.append(n)
            ps = max_square
        else:
            n = l_num.pop()
            if l_num.__len__() > 1:
                ps = n + l_num[-1] - int(math.sqrt(n + l_num[-1])) * 2 + 1
            elif l_num.__len__() == 1:
                if 1 < l_num[0] <= num:
                    l_num[0] -= 1
                    ps = max_square
                else:
                    l_num.pop()
                    break
            else:
                break

        if l_num.__len__() == num:
            break

    return l_num if l_num else False


if __name__ == '__main__':
    for i in [5, 15, 23, 37]:
        start = time()
        ss = square_sums3(i)
        end = time()
        print(ss)
        print(f'for {end - start} s')
        # if ss:
        #     for j in range(ss.__len__()-1):
        #         if j % 2:
        #             print(f'    {ss[j]:2}, {ss[j + 1]:2} => {ss[j] + ss[j + 1]}')
        #         else:
        #             print(f'{ss[j]:2}, {ss[j + 1]:2} => {ss[j] + ss[j + 1]}')

        print()
