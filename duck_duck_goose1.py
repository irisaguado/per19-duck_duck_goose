import sys
nom_jugadores = ['juan', 'pepa', 'antonio', 'luisa', 'ana]
num_elegigo = sys.argv[1]
num_elegido = int(num_elegido)
def duck_duck_goose(nom_jugadores, num_elegido):
    while num_elegido > len(nom_jugadores):
        num_elegido = num_elegido -4
    jug_elegido = nom_jugadores[num_elegido-1]
    return jug_elegido

print(duck_duck_goose(nom_jugadores, num_elegido))


