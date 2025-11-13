def matrixout(mx, size):
    print("𐌲" + "        " * size + "ㄱ")
    for i in range(size):
        print("|", end=" ")
        for j in range(size):
            print("%7.3f" % mx[i][j], end=" ")
        print("|")
    print("ㄴ" + "        " * size + "^")

def transposeMatrix(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

def getMatrixMinor(m, i, j):
    return [row[:j] + row[j+1:] for row in (m[:i] + m[i+1:])]

def getMatrixDeterminant(m):
    if len(m) == 1:
        return m[0][0]
    if len(m) == 2:
        return m[0][0]*m[1][1] - m[0][1]*m[1][0]
    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeterminant(getMatrixMinor(m, 0, c))
    return determinant

def has_inverse(m):
    determinant = getMatrixDeterminant(m)
    if abs(determinant) < 1e-10:
        print("Error! Determinant is 0 → inversion impossible.")
        return False
    return True

def getMatrixInverse(m):
    determinant = getMatrixDeterminant(m)
    if len(m) == 1:
        return [[1.0 / m[0][0]]]
    if len(m) == 2:
        return [[m[1][1]/determinant, -m[0][1]/determinant],
                [-m[1][0]/determinant, m[0][0]/determinant]]
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m, r, c)
            cofactorRow.append(((-1)**(r+c))*getMatrixDeterminant(minor))
        cofactors.append(cofactorRow)
    adjugate = transposeMatrix(cofactors)
    for r in range(len(adjugate)):
        for c in range(len(adjugate)):
            adjugate[r][c] /= determinant
    return adjugate

def main():
    try:
        k = int(input("Input square matrix's degree: "))
        if k <= 0:
            print("Degree must be positive!")
            return
        print(f"Enter a {k}x{k} matrix. Each row separated by Enter, numbers separated by spaces.")
        matrix_a = []
        for i in range(k):
            while True:
                try:
                    row_input = input(f"{i+1}-row: ").strip()
                    row_values = [float(x) for x in row_input.split()]
                    if len(row_values) != k:
                        print("Row must have exactly", k, "numbers.")
                        continue
                    matrix_a.append(row_values)
                    break
                except ValueError:
                    print("Input Error! Numbers only.")
        if has_inverse(matrix_a):
            print("\nMatrix Inverse is:")
            inverse = getMatrixInverse(matrix_a)
            matrixout(inverse, k)
    except ValueError:
        print("Input Error. Please enter integers.")
    except Exception as e:
        print(f"Unexpected Error: {e}")
    print()

if __name__ == "__main__":
    main()
