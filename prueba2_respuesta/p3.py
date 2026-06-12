tablero = [
    ["","*"," "],
    ["*","","*"],
    [" ","*",""]
]

n = len(tablero)
m = len(tablero[0])

for i in range(n):
    for j in range(m):
        bombas = 0
        for di in [-1,0,1]:
            for dj in [-1,0,1]:
                if 0 <= i + di < n and 0 <= j + dj < m:
                    if tablero[i + di][j + dj] == "*":
                        bombas += 1
        if tablero[i][j] != "*":
            tablero[i][j] = bombas
for i in range(n):
    for j in range(m):
        print(tablero[i][j], end=' ')
    print()