n = 5
relation = [(1, 1), (1, 4), (2, 2), (3, 4), (3, 5), (4, 1), (5, 2), (5, 5)]

matrix = [[0] * n for _ in range(n)]
for i, j in relation :
    matrix[i - 1][j - 1] = 1

def print_matrix(matrix) :
    for row in matrix :
        print(row)
    print()

print("relation matrix's initial state : ")
print_matrix(matrix)

print("Doing connections between paths and shi-")
for k in range(n) :
    for i in range(n) :
        for j in range(n) :
            if not matrix[i][j] and matrix[i][k] and matrix[k][j] :
                print(f"step k={k + 1} : {i + 1} -> {k + 1} -> {j + 1}")
                matrix[i][j] = 1

print("after applying floyd warshal algo on it : ")
print_matrix(matrix)
