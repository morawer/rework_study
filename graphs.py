import matplotlib.pyplot as plt

def graphsAvgCreator(sabanas):
    
    dates = []
    lines = []

    for sabana in sabanas:
        dates.append(sabana.model)
        lines.append(sabana.lines)
        
    eje_x = dates
    eje_y = lines

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
