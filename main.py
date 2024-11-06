import random
def cargar_lista(nombreArchivo):
    fichero = open(nombreArchivo,"r")
    for linea in fichero:
        diccionarioCancion = {}
        diccionarioCancion["nombre"] = linea.split("-")[0].strip()
        diccionarioCancion["artista"] = linea.split("-")[1].strip()
        diccionarioCancion["genero"] = linea.split("-")[2].strip()
        listaCanciones.append(diccionarioCancion)
    fichero.close()
def agregar_cancion(listaCanciones,nombreCancion,nombreArtista,genero):
    cancionNueva = {"nombre": nombreCancion, "artista": nombreArtista, "genero": genero}
    listaCanciones.append(cancionNueva)

def eliminar_cancion(listaCanciones,nombreCancion):
    for cancion in listaCanciones:
        if cancion["nombre"] == nombreCancion:
            listaCanciones.remove(cancion)
            

def contar_canciones(listaCanciones):
    return len(listaCanciones)

def buscar_por_artista(listaCanciones,nombreArtista):
    cancionesDelArtista = []
    for cancion in listaCanciones:
        if cancion["artista"] == nombreArtista:
            cancionesDelArtista.append(cancion["nombre"])
    return cancionesDelArtista


def ordernar_alfabeticamente(listaCanciones):
    listaOrdenada = []
    for cancion in listaCanciones:
        listaOrdenada.append(cancion["nombre"])
    return sorted(listaOrdenada)
    
    
    
def crear_lista_aleatoria(diccionarioCanciones,n):
    listaAleatoria = []
    canciones = list(diccionarioCanciones.keys())
    for i in range(n):
        numAleatorio = random.randint(0,len(diccionarioCanciones)-1);
        listaAleatoria.append(canciones[numAleatorio])
    return listaAleatoria

def guardar_lista(listaCanciones,nombreArchivo):
    fichero = open(nombreArchivo,"w")
    for cancion in listaCanciones:
        fichero.write(cancion["nombre"] + " - " + cancion["artista"]+" - " + cancion["genero"]+"\n")
    fichero.close()
        
listaCanciones = []
cargar_lista("playlist.txt")
agregar_cancion(listaCanciones,"Corazón partido","Alejandro Sanz","Rock")
eliminar_cancion(listaCanciones,"Bohemian Rhapsody")
print(contar_canciones(listaCanciones))
print(buscar_por_artista(listaCanciones,"Led Zeppelin"))
print(ordernar_alfabeticamente(listaCanciones))
guardar_lista(listaCanciones,"playlist_nueva.txt")