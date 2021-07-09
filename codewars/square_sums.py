import math
from time import time
from collections import defaultdict


def square_sums2(num):
    if num < 1 or num > 1000:
        return False

    squares = [i ** 2 for i in range(2, int(math.sqrt(num * 2)) + 1)]
    len_squares = squares.__len__()
    l_num = [[num, -1]]  # (number, index in squares)

    while True:
        l_num[-1][1] += 1
        vn1, in1 = l_num[-1]
        # print(vn1, in1)
        if vn1 <= num and in1 < len_squares:
            tl_num = [vn for vn, _ in l_num]
            vn2 = squares[in1] - vn1
            if 0 < vn2 <= num and vn2 not in tl_num:
                l_num.append([vn2, -1])
        elif l_num.__len__() == 1:
            l_num[-1][0] -= 1
            l_num[-1][1] = -1
        else:
            l_num.pop()

        if not l_num or l_num.__len__() == num:
            break

        # print([vn for vn, _ in l_num])
        # print(l_num)

    return [vn for vn, _ in l_num] if l_num else False


def square_sums(num):
    start = time()
    if num < 1 or num > 1000:
        return False

    l_num = [num]
    n = num - 1

    while True:
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

        # print(l_num)

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
        # while n > 0 and (n > num or n in l_num):
        #     n = n - int(math.sqrt(n + l_num[-1])) * 2 + 1

        if n > num or n in l_num:
            ps = n + l_num[-1] - int(math.sqrt(n + l_num[-1])) * 2 + 1
        elif n > 0:
            l_num.append(n)
            ps = max_square
            # ps = int(math.sqrt(n + num)) ** 2
        else:
            n = l_num.pop()
            if l_num.__len__() > 0:
                ps = n + l_num[-1] - int(math.sqrt(n + l_num[-1])) * 2 + 1
            elif 1 < n <= num:
                l_num.append(n - 1)
                ps = max_square
            else:
                break

        if l_num.__len__() == num:
            break

    return l_num if l_num else False


def square_sums4(num):
    if num < 1 or num > 1000:
        return False

    s = sum(range(num + 1))
    ps = int(math.sqrt(num * 2 - 1)) ** 2
    fs = 0
    d_l_num = defaultdict(bool)
    l_num = [num]
    d_l_num[num] = True
    while True:
        if fs == ps:
            ps = ps - int(math.sqrt(ps)) * 2 + 1
            continue

        n = ps - l_num[-1]
        # print(l_num, n)
        if n > 0:
            if d_l_num[n]:
                ps = ps - int(math.sqrt(ps)) * 2 + 1
            else:
                l_num.append(n)
                d_l_num[n] = True
                fs = ps
                ps = int(math.sqrt(n + num)) ** 2
                if l_num.__len__() == num:
                    if sum(l_num) == s:
                        print(l_num)
                        # f.write(f'{l_num.__str__()}\n')
                    # break
        else:
            n = l_num.pop()
            d_l_num[n] = False
            if l_num.__len__() > 0:
                ps = n + l_num[-1] - int(math.sqrt(n + l_num[-1])) * 2 + 1
            elif 1 < n <= num:
                l_num.append(n - 1)
                d_l_num[n - 1] = True
                fs = 0
                ps = int(math.sqrt(n + num - 1)) ** 2
            else:
                # f.write('\n')
                break

            # print(l_num)
        # print(l_num)

    # f.close()
    return l_num if l_num else False


if __name__ == '__main__':
    # for i in range(1, 38):
    # for i in [5, 15, 23, 27, 37]:
    for i in [15]:
        # start = time()
        # ss = square_sums3(i)
        # end = time()
        # print(ss)
        # print(f'{i} for ss4 {end - start} s')
        start = time()
        ss = square_sums4(i)
        end = time()
        print(ss)
        print(f'{i} for ss5 {end - start} s')
        # squares = [j ** 2 for j in range(2, int(math.sqrt(i * 2)) + 1)]
        # if ss:
        #     for j in range(ss.__len__()-1):
        #         if j % 2:
        #             print(f'    {ss[j]:2}, {ss[j + 1]:2} => {ss[j] + ss[j + 1]}')
        #         else:
        #             print(f'{ss[j]:2}, {ss[j + 1]:2} => {ss[j] + ss[j + 1]}')

        print()
