n = 3
while n < 5:
    n = int(input("Ingrese un número entero mayor o igual a 5: "))  

ind = int(n*(2/3))

for i in range(n):
    for j in range(n):
        # Diagonal desde ind, 0 hasta 0, ind en la otra direccion 
        if (i == ind - j and j <= ind)  or i == ind or j == ind:
            print('*', end=' ')

        else:
            print(' ', end=' ')
    print()