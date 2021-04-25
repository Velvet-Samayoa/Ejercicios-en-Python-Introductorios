class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None

class Arbol:
    # Funciones privadas
    def __init__(self, dato):
        self.raiz = Nodo(dato)

    def agregar_dato(self, nodo, dato):
        if dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(dato)
            else:
                self.agregar_dato(nodo.izquierda, dato)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(dato)
            else:
                self.agregar_dato(nodo.derecha, dato)

    def r_inorden(self, nodo):
        if nodo is not None:
            self.r_inorden(nodo.izquierda)
            print(nodo.dato, end=", ")
            self.r_inorden(nodo.derecha)

    def r_preorden(self, nodo):
        if nodo is not None:
            print(nodo.dato, end=", ")
            self.r_preorden(nodo.izquierda)
            self.r_preorden(nodo.derecha)

    def r_postorden(self, nodo):
        if nodo is not None:
            self.r_postorden(nodo.izquierda)
            self.r_postorden(nodo.derecha)
            print(nodo.dato, end=", ")

    def __buscar(self, nodo, busqueda):
        if nodo is None:
            return None
        if nodo.dato == busqueda:
            return nodo
        if busqueda < nodo.dato:
            return self.__buscar(nodo.izquierda, busqueda)
        else:
            return self.__buscar(nodo.derecha, busqueda)


    # Funciones públicas
    def agregar(self, dato):
        self.agregar_dato(self.raiz, dato)

    def inorden(self):
        print("\nIMPRIMIENDO ARBOL CON RECORRIDO INORDEN: ")
        self.r_inorden(self.raiz)
        print("")

    def preorden(self):
        print("\nIMPRIMIENDO ARBOL CON RECORRIDO PREORDEN: ")
        self.r_preorden(self.raiz)
        print("")

    def postorden(self):
        print("\nIMPRIMIENDO ARBOL CON RECORRIDO POSTORDEN: ")
        self.r_postorden(self.raiz)
        print("")

    def buscar(self, busqueda):
        return self.__buscar(self.raiz, busqueda)


#árbol binario con String
arbol = Arbol("Samayoa")
arbol.agregar("Eunice")
arbol.agregar("Velvet")
arbol.agregar("Aguilar")
arbol.agregar("Es")
arbol.agregar("Una")
arbol.agregar("Universitaria")
nombre = input("\nINGRESA UNA PALABRA PARA AGREGARLE AL ARBOL:  ")
print("\n*****************ARBOL BINARIO CON STRING****************")
arbol.agregar(nombre)
arbol.preorden()
arbol.inorden()
arbol.postorden()
# Buscando
busqueda = input("\nBUSQUEMOS ALGO EN EL ARBOL: ")
nodo = arbol.buscar(busqueda)
if nodo is None:
    print(f"--> {busqueda} no existe :'(\n")
else:
    print(f"-->{busqueda} sí existe :)\n")
  

#árbol binario con Int
arbol_numeros = Arbol(50)
arbol_numeros.agregar(90)
arbol_numeros.agregar(35)
arbol_numeros.agregar(30)
arbol_numeros.agregar(56)
arbol_numeros.agregar(68)
arbol_numeros.agregar(40)
arbol_numeros.agregar(32)
arbol_numeros.agregar(28)
arbol_numeros.agregar(10)
arbol_numeros.agregar(98)
arbol_numeros.agregar(55)
arbol_numeros.agregar(95)
arbol_numeros.agregar(99)
arbol_numeros.agregar(29)
print("\n********ARBOL BINARIO CON NUMEROS ENTEROS********")
arbol_numeros.preorden()
arbol_numeros.inorden()
arbol_numeros.postorden()
#buscando
busqueda = int(input("\nBUSQUEMOS ALGO EN EL ARBOL DE NUMEROS: "))
n = arbol_numeros.buscar(busqueda)
if n is None:
    print(f"--> {busqueda} no existe :'(\n")
else:
    print(f"--> {busqueda} sí existe :)\n")