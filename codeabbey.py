m_str = """---X-X-
XX--X-X
------X
-X--XXX
---X-XX"""

result = []
m1 = [list(line) for line in m_str.split()]
n, m = len(m1), len(m1[0])
for r in range(5):
    m2 = [['-' for j in range(len(m1[0]))] for i in range(len(m1))]
    #m2 = [list(line) for line in str(('-' * len(m1[0]) + '\n') * len(m1)).split()]
    for i in range(n):
        for j in range(m):
            indices = [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j+1), 
            (i+1, j+1), (i+1, j), (i+1, j-1), (i, j-1)]
            s = sum([int(m1[k][e] == 'X') for k, e in indices 
            if (k >= 0) and (k < len(m1)) and (e >= 0) and (e < len(m1[0]))])
            if ((m1[i][j] == 'X') and (s in [2, 3])) or ((m1[i][j] == '-') and (s == 3)):
                m2[i][j] = 'X'
    result.append(str(sum([line.count('X') for line in m2])))
    m1 = [[c for c in l] for l in m2]

print(' '.join(result))
