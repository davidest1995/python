# AÚN NO FUNCIONA

def way (dimension, wall):
    way= []
    for i in range(dimension):
        fila=[]
        for j in range(dimension):
            if tuple([i,j]) in wall:
                fila.append('[]')
            else:
                fila.append(' ')
        way.append(fila)
    return way


wall = ((0,1), (0,2), (0,3), (0,4),(1,1), (2,1), (2,3), (3,3),(4,0), (4,1), (4,2), (4,3))
lab = way(5,wall)
for i in lab:
    print(''.join(i))

def run_way(way):
    fila = columna = 0
    movimientos=['Abajo']

    while (fila < n-1 and columna < n-1):
        if movimientos [-1] != 'Arriba' and fila + 1 < n and way[fila + 1][columna] != 'X':
            fila += 1
            movimientos.append('Abajo')

        elif movimientos[-1] != 'Abajo'and fila -1 > 0 and way[fila - 1][columna] != 'X':
            fila -=1
            movimientos.append('Derecha')

        elif movimientos[-1] != 'Izquierda'and columna + 1 > 0 and way[fila][columna + 1] != 'X':
            columna +=1
            movimientos.append('Derecha')  

        elif movimientos[-1] != 'Derecha'and columna - 1 > 0 and way[fila][columna - 1] != 'X':
            columna -=1
            movimientos.append('Izquierda')
        else:
            movimientos.append('No hay salida')

    return movimientos

print('Solution', run_way(lab))