# 사용자로부터 행렬 크기 입력
maxvalue = int(input("입력으로 넣을 관계행렬의 크기를 입력하라.: "))
print()
print("1과 0으로 구성된", maxvalue, "x", maxvalue, "인 관계행렬을 입력하라.:", sep='')

# 사용자 입력 저장
data = []
for i in range(maxvalue):
    row = input().split()
    data.append(row)

# 문자열 → 정수로 변환하여 관계행렬 m에 저장
m = []
for i in range(maxvalue):
    m.append([int(data[i][j]) for j in range(maxvalue)])

# 길이 3의 경로 탐색
print("\n주어진 관계행렬에 대해 길이가 3인 경로들의 리스트는 다음과 같다:\n")
count = 0

for i in range(maxvalue):
    for j in range(maxvalue):
        if m[i][j]:
            for x in range(maxvalue):
                if m[j][x]:
                    for y in range(maxvalue):
                        if m[x][y]:
                            print("(%d→%d→%d→%d) ⇒ (%d...%d)" %
                                  (i + 1, j + 1, x + 1, y + 1, i + 1, y + 1))
                            count += 1

if count == 0:
    print("주어진 관계행렬에 대해 길이가 3인 경로가 없다.")
