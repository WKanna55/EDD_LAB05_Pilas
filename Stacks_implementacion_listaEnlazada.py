class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.contador = 0

    def insertar_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza == None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        self.contador += 1

    def insertar_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza == None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        self.contador += 1

    def insertar_dentro(self, dato, posicion):
        nuevo_nodo = Nodo(dato)
        actual = self.cabeza
        indice = 0
        while actual != None:
            if indice == posicion:
                anterior = actual
                siguiente = actual.siguiente
                anterior.siguiente = nuevo_nodo
                nuevo_nodo.siguiente = siguiente
                return
            indice += 1
            actual = actual.siguiente
        self.contador += 1

    def eliminar_primero(self):
        if self.cabeza == None:
            raise Exception("Lista enlazada vacia")
        if self.cabeza == self.cola:
            self.cabeza = None
            self.cola = None
        else:
            segundo = self.cabeza.siguiente
            self.cabeza.siguiente = None
            self.cabeza = segundo
        self.contador -= 1

    def eliminar_final(self):
        actual = self.head
        if self.cabeza == None:
            raise Exception("Lista enlazada vacia")
        if self.cabeza == self.cola:
            self.cabeza = None
            self.cola = None
        else:
            while actual != None:
                if actual.siguiente == self.cola:
                    break
                actual = actual.siguiente
            actual.siguiente = None
            self.cola = actual
        self.contador -= 1

    def eliminar_dentro(self, dato):
        actual = self.cabeza
        anterior = None
        while actual != None:
            if actual.siguiente.valor == dato:
                anterior = actual
                actual = actual.siguiente
                break
            actual = actual.siguiente
        anterior.siguiente = actual.siguiente
        self.contador -= 1

    def imprimir_lista(self):
        actual = self.cabeza
        while actual != None:
            print(actual.valor, end=" - ")
            actual = actual.siguiente
        print("None")

    """Ejercicio 01: implementacion básica (fin)"""

    """Ejercicio 02: Busqueda (inicio)"""
    def buscar(self, valor):
        actual = self.cabeza
        while actual != None:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False

    """Ejercicio 02: Busqueda (fin)"""

    """Ejercicio 03: invertir lista enlazada(inicio)"""
    def invertir(self):
        anterior = None
        actual = self.cabeza
        while actual:
            siguiente = actual.siguiente
            actual.siguiente = anterior
            anterior = actual
            actual = siguiente
        self.cabeza = anterior
    """Ejercicio 03: invertir lista enlazada(fin)"""

    """Ejercicio 04: Eliminacion de duplicados(inicio)"""

    def eliminar_duplicado(self):
        actual = self.cabeza

        while actual != None:
            comparador = actual
            while comparador.siguiente:
                if comparador.siguiente.valor == actual.valor:
                    comparador.siguiente = comparador.siguiente.siguiente
                else:
                    comparador = comparador.siguiente
            actual = actual.siguiente

    """Ejercicio 04: Eliminacion de duplicados(fin)"""

    """Ejercicio 05: Concatenar listas (inicio)"""
    def concatenar_listas(self, listaConc):
        lista_resultado = ListaEnlazada()
        actual_1 = self.cabeza
        while actual_1 != None:
            lista_resultado.insertar_final(actual_1.valor)
            actual_1 = actual_1.siguiente
        actual_2 = listaConc.cabeza
        while actual_2 != None:
            lista_resultado.insertar_final(actual_2.valor)
            actual_2 = actual_2.siguiente
        return lista_resultado
    """Ejercicio 05: Concatenar listas (fin)"""

    """Ejercicio 06: Detectar ciclo (inicio)"""
    def detectar_ciclo(self):
        tortuga = self.cabeza
        liebre = self.cabeza
        while liebre is not None and liebre.siguiente is not None:
            tortuga = tortuga.siguiente
            liebre = liebre.siguiente.siguiente
            if tortuga == liebre:
                return True
    """Ejercicio 06: Detectar ciclo (fin)"""

    """Ejercicio 07: Lista palindromo (inicio)"""
    def es_palindromo(self):
        def encontrar_punto_medio(lista):
            tortuga = lista.cabeza
            liebre = lista.cabeza

            while liebre is not None and liebre.siguiente is not None:
                tortuga = tortuga.siguiente
                liebre = liebre.siguiente.siguiente

            return tortuga

        punto_medio = encontrar_punto_medio(self)
        segunda_mitad = ListaEnlazada()
        segunda_mitad.cabeza = punto_medio.siguiente
        punto_medio.siguiente = None
        segunda_mitad.invertir()

        primera_mitad_actual = self.cabeza
        segunda_mitad_actual = segunda_mitad.cabeza

        while primera_mitad_actual is not None and segunda_mitad_actual is not None:
            if primera_mitad_actual.valor != segunda_mitad_actual.valor:
                return False
            primera_mitad_actual = primera_mitad_actual.siguiente
            segunda_mitad_actual = segunda_mitad_actual.siguiente

        return True
    """Ejercicio 07: Lista palindromo (fin)"""

    """Ejercicio 08: Eliminacion de nodos (inicio)"""
    def eliminar_todo(self):
        self.cabeza = None
    """Ejercicio 08: Eliminacion de nodos (fin)"""

    """Ejercicio 09: Insercion ordenada (inicio)"""

    def bubble_sort(self):
        if not self.cabeza:
            return

        while True:
            swapped = False
            actual = self.cabeza
            previo = None

            while actual.siguiente:
                siguiente = actual.siguiente
                if actual.valor > siguiente.valor:
                    # Realiza el intercambio de nodos
                    if previo:
                        previo.siguiente = siguiente
                    else:
                        self.cabeza = siguiente
                    actual.siguiente = siguiente.siguiente
                    siguiente.siguiente = actual
                    swapped = True
                previo = actual
                actual = siguiente

            if not swapped:
                break

    def insertar_ordenadamente(self, valor):
        nuevo_nodo = Nodo(valor)

        if not self.cabeza or valor <= self.cabeza.valor:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
            return

        actual = self.cabeza
        while actual.siguiente and valor > actual.siguiente.valor:
            actual = actual.siguiente

        nuevo_nodo.siguiente = actual.siguiente
        actual.siguiente = nuevo_nodo

    """Ejercicio 09: Insercion ordenada (fin)"""

    """Ejercicio 10: Longitud de la lista (inicio)"""
    def longitud_lista(self):
        return self.contador
    """Ejercicio 10: Longitud de la lista (fin)"""


class Pila(ListaEnlazada):
    def __init__(self):
        super().__init__()

    def push(self):
        self.insertar_final

    def pop(self):
        self.eliminar_final

    def isEmpty(self):
        if self.contador == 0:
            return True
        else:
            return False
        
    def size(self):
        return self.contador

    def Pila_imprimir(self):
        self.imprimir_lista


