from itertools import permutations, count

list_n = {'c': '1236', 't': '6123', 's': '3612', 'x': '2361'}
correct_seq = ''
for i in count(start=7, step=1):
    list_i = ''.join([item * i for item in list_n])
    l_i = permutations(list_i, i)
    for item in l_i:
        correct_n = '0000'
        for c in item:
            correct_n = ''.join([str((int(c1) + int(c2)) % 10)
                                 for c1, c2 in zip(correct_n, list_n[c])])
            # correct_n = str(int(correct_n) + int(list_n[c]))

        print(f'{"".join(item)} => {correct_n}')
        if correct_n == '0223':
            print(f'{"".join(item)} ===============> {correct_n}')
            correct_seq = correct_n
            break

    if correct_seq:
        break
