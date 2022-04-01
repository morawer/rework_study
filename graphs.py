import matplotlib.pyplot as plt



## Declaramos valores para el eje x
eje_x = ['Python', 'R', 'Node.js', 'PHP']

## Declaramos valores para el eje y
eje_y = [50, 20, 35, 47]

## Creamos Gráfica
plt.bar(eje_x, eje_y)

## Legenda en el eje y
plt.ylabel('Media de lineas por equipo:')

## Legenda en el eje x
plt.xlabel('Semana:')

## Título de Gráfica
plt.title('Gráfica de media de líneas')

## Mostramos Gráfica
plt.show()
