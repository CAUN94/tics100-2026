fecha = ["01/01/2026", "01/01/2026", "03/01/2026", "03/01/2026", "03/01/2026"]
npersonas = [2, 2, 1, 4, 5]
nombre = ["Ana", "Luis", "Pedro", "Maria", "Juan"]

u_fecha = input("Ingrese la fecha (dd/mm/yyyy): ")
u_npersonas = int(input("Ingrese el número de personas: "))
u_nombre = input("Ingrese el nombre: ")

suma = 0
for i in range(len(fecha)):
    if fecha[i] == u_fecha:
        suma = suma + npersonas[i]

if suma + u_npersonas > 50:
    print("No es posible reservar para esa fecha, quedan", 50 - suma, "lugares disponibles.")
else:
    print("Es posible reservar para esa fecha, quedan", 50 - (suma + u_npersonas), "lugares disponibles.")
    fecha.append(u_fecha)
    npersonas.append(u_npersonas)
    nombre.append(u_nombre)