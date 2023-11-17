def validacion(lista,valor):
    conjunto=[]
    for i in range (len(lista)):
        conjunto.append( lista[i]["LU"] )
    
    while (valor in conjunto):
        valor = int( input("Ingrese nro de la LU: ") )

    return valor



def cargar(lista,n):
    
    for i in range (n):
        estudiante = {}
        estudiante["Nombre"] = input("Ingrese su nombre: ")
        estudiante["Apellido"] = input("Ingrese su apellido: ")
        estudiante["Carrera"] = input("Ingrese la carrera: ")
        estudiante["LU"] = validacion(lista, int( input("Ingrese nro de la LU: ") ) )

        lista.append(estudiante)

def mostrar(lista):
    print(f"{'Nombre':10} {'Apellido':10} LU")
    for elemento in lista:
        #print( "Nombre: "+elemento["Nombre"] )
        print(f"{elemento['Nombre']:10} {elemento['Apellido']:10} {elemento['LU']} ")   #:<10.3     alinea a izquierda

limite = 2
lista =[]
cargar(lista,limite)

#print(lista)

mostrar(lista)