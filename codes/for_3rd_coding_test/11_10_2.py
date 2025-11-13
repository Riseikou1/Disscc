def matrix_mult(a, b):
    size = len(a)
    result = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            # Boolean matrix multiplication (relation composition)
            for k in range(size):
                result[i][j] |= (a[i][k] and b[k][j])
    return result


def is_transitive(matrix):
    size = len(matrix)
    combined = [row[:] for row in matrix]
    power = [row[:] for row in matrix]

    # Check if matrix^2 still within the original matrix (transitivity)
    for _ in range(1, size):
        power = matrix_mult(power, matrix)
        for i in range(size):
            for j in range(size):
                combined[i][j] |= power[i][j]

    # If relation is transitive, R² ⊆ R
    for i in range(size):
        for j in range(size):
            if combined[i][j] and not matrix[i][j]:
                return False
    return True


def print_relation(matrix, a):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]:
                print(f"({a[i]}, {a[j]})", end=" ")
    print()


def input_relation_matrix():
    a = ['w', 'x', 'y', 'z']
    size = len(a)
    index_map = {ch: idx for idx, ch in enumerate(a)}
    matrix = [[0] * size for _ in range(size)]   

    print("Enter pairs like wx xy yz (no commas):")
    pairs = input("Input : ").split()
    for pair in pairs:
        if len(pair) != 2 or pair[0] not in index_map or pair[1] not in index_map:
            continue
        i, j = index_map[pair[0]], index_map[pair[1]]
        matrix[i][j] = 1
    return matrix, a    


def main():
    matrix, a = input_relation_matrix()
    print("\nRelation R contains:")
    print_relation(matrix, a)

    if is_transitive(matrix):
        print("The relation is transitive.")
    else:
        print("The relation is NOT transitive.")


if __name__ == "__main__":
    main()
