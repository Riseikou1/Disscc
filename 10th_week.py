def print_relation(matrix) :
    for r in range(len(matrix)) :
        for c in range(len(matrix[0])) :
            if matrix[r][c] :
                print(f"{(r + 1, c + 1)}", end = " ")
    print()
    
def is_reflexive(matrix,) :
    for i in range(len(matrix)) :
        if not matrix[i][i] :
            return False
    return True 

temuujin = [1, 2, 3, 4, 5]
n = len(temuujin)
matrix = []
print("pisda : ")

for _ in range(n) :
    input_row = list(map(int, input().split()))
    matrix.append(input_row)

print_relation(matrix)

if is_reflexive(matrix) :
    print("this shit is 반사 ")
else :
    print("not 반사.")
    
