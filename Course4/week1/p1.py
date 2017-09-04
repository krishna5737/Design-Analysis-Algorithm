import math

def floyd_warshall(n, edges):

    range_n = range(n)
    A = [[[0 if i == j else math.inf] for j in range_n] for i in range_n]

    for (s, t, c) in edges:
        A[s - 1][t - 1][0] = c

    for k in range(1, n):
        print(k,n)
        for i in range_n:
            for j in range_n:
                A[i][j].append(min(A[i][j][k - 1], A[i][k][k - 1] + A[k][j][k -1]))

    shortest_path = math.inf

    for i in range_n:
        if A[i][i][n - 1] < 0:
            print('Negative cycle detected')
            return

        for j in range_n:
            if A[i][j][n - 1] < shortest_path:
                shortest_path = A[i][j][n - 1]

    print('Shortest shortest path:', shortest_path)



input_file_name = 'g2.txt'

with open(input_file_name) as f:
    n = int(f.readline().split()[0])
    input = [tuple(map(int, x.split())) for x in f.readlines()]

floyd_warshall(n, input)
