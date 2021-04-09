import pygame
#inicia pygame
pygame.init()

#creo una ventana y le asigno un nombre al juego
t_ventana = 1000
pantalla = pygame.display.set_mode((t_ventana, t_ventana))
pygame.display.set_caption("Juego De La Vida")

#variables para los colores y pinto la pantalla
Negro = 0, 0, 0
Azul = 0, 0, 255
Gris = 25, 25, 25

pantalla.fill(Gris)

#especifico el numero n*n celdas que quiero en mi programa
numero_de_celdas = 100

#asigno el tamaño de cada celda
d_celdas = t_ventana / numero_de_celdas

#creo una matriz de ceros por comprension de tamaño nxn
juego = [[0 for i in range(numero_de_celdas)] for j in range(numero_de_celdas)]

#agrego un patron preconfigurado
juego[49][49] = 1
juego[50][49] = 1
juego[50][50] = 1
juego[50][51] = 1
juego[51][50] = 1

#creo un bucle
run = True
while run:
    #agrego una condicion si se cumple salgo del bucle
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            run = False
    #creo una nueva matriz a partir de la matriz juego
    actualizo_juego = []
    for i in juego:
        actualizo_juego.append(list(i))
    pantalla.fill(Gris)
    #hago un ciclo que recorra la matriz y compruebe cuantas celulas vivas hay alrededor de cada celula
    for y in range(numero_de_celdas):
        for x in range(numero_de_celdas):
            celulas_vecinas = juego[(x - 1) % numero_de_celdas][(y - 1) % numero_de_celdas] \
                              + juego[x % numero_de_celdas][(y - 1) % numero_de_celdas] \
                              + juego[(x + 1) % numero_de_celdas][(y - 1) % numero_de_celdas] \
                              + juego[(x - 1) % numero_de_celdas][y % numero_de_celdas] \
                              + juego[(x + 1) % numero_de_celdas][y % numero_de_celdas] \
                              + juego[(x - 1) % numero_de_celdas][(y + 1) % numero_de_celdas] \
                              + juego[x % numero_de_celdas][(y + 1) % numero_de_celdas] \
                              + juego[(x + 1) % numero_de_celdas][(y + 1) % numero_de_celdas]
           #reglas del juego
            #Una célula viva con 2 o 3 células vecinas vivas sigue viva, en otro caso muere (por "soledad" o "superpoblación")
            if juego[x][y] == 1 and (celulas_vecinas < 2 or celulas_vecinas > 3):
                actualizo_juego[x][y] = 0
            #1 si una celula esta muerta y tiene 3 vecinas vivas la celula nace
            elif juego[x][y] == 0 and celulas_vecinas == 3:
                actualizo_juego[x][y] = 1


            #creo una lista especificando sus coordenadas x & y de las celulas para posteriormente ser pintadas
            celda = [(x * d_celdas, y * d_celdas), ((x + 1) * d_celdas, y * d_celdas),
                     ((x + 1) * d_celdas, (y + 1) * d_celdas), (x * d_celdas, (y + 1) * d_celdas)]

            # pinto la celdas
            if actualizo_juego[x][y] == 0:
                pygame.draw.polygon(pantalla, Negro, celda, 1)
            else:
                pygame.draw.polygon(pantalla, Azul, celda, 0)

    #actualizo el estado del juego
    juego = []
    for i in actualizo_juego:
        juego.append(list(i))
    pygame.display.flip()