def print_relation(matrix, a):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                print(f"({a[i]}, {a[j]})", end=" ")
    print()

def is_reflexive(matrix):
    for i in range(len(matrix)):
        if matrix[i][i] != 1:
            return False
    return True

def main():
    a = [1, 2, 3, 4, 5]
    n = len(a)
    matrix = []
    print("Input the 5x5 matrix (each row separated by Enter):")

    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    print("\nRelation R contains:")
    print_relation(matrix, a)

    if is_reflexive(matrix):
        print("This is a reflexive relation.")
    else:
        print("This ain't a reflexive relation.")


if __name__ == "__main__":
    main()
