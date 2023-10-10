#Ejercicio 01: Implementar una pila apartir de arreglo (inicio)
class PilaArray():

    def __init__(self) -> None:
        self.datos = []

    def push(self, valor):
        self.datos.append(valor)

    def pop(self):

        if self.isEmpty():
            raise Exception("Error: la pila esta vacia, no retorna nada")

        return self.datos.pop()

    def isEmpty(self):
        return len(self.datos) == 0
        
    def size(self):
        return len(self.datos)
    
    def top(self):
        return self.datos[len(self.datos) - 1]
    
    def imprimir_pila(self):
        print(self.datos)

#Ejercicio 01: Implementar una pila apartir de arreglo (fin)


#Ejercicio 02: Invertir caracteres (inicio, terminado)
#Complejidad de tiempo O(n)
#Complejidad de espacio O(n)

def invertir_cadena(cadena):
    pila_invertir = PilaArray()
    for i in cadena:
        pila_invertir.push(i)
    palabra_invertida = ""
    while pila_invertir.size() > 0:
        palabra_invertida += pila_invertir.pop()
    return palabra_invertida

cadena_normal = "HOLA"
print(invertir_cadena(cadena_normal))

#Ejercicio 02: Invertir caracteres (fin)

#Ejercicio 03: Parentesis balanceado (inicio, terminado)
#Complejidad de tiempo O(n)
#Complejidad de espacio 0(n)

def comprobar_parentesis(cadena):
    pila_comprobar = PilaArray()
    contenedor = ["(", ")"]
    for i in parentesis:
        if i == contenedor[1] and pila_comprobar.size() == 0:
            return False

        if i == contenedor[0]:
            pila_comprobar.push(i)

        if i == contenedor[1]:
            pila_comprobar.pop()

    if pila_comprobar.size() == 0:
        return True
    else:
        return False

parentesis = "((()))"
print(comprobar_parentesis(parentesis))

#Ejercicio 03: Parentesis balanceado (fin)

#Ejercicio 04: Evaluacion de expresiones postfijas (inicio, terminado)
#Complejidad de tiempo O(n)
#Complejidad de espacio O(1)
#operacion infija = 2+(3*1) - 9 = -4 (resultado esperado)

def opPostfija_result(cadena):
    pila_op = PilaArray()
    for i in cadena:
        if i.isdigit():
            pila_op.push(i)
        else:
            num1 = pila_op.pop()
            num2 = pila_op.pop()
            resultado = eval(num2 + i + num1)
            pila_op.push(str(resultado))
    return pila_op.pop()

cadena_postfija = "231*+9-"

print(opPostfija_result(cadena_postfija))

#Ejercicio 04: Evaluacion de expresiones postfijas (fin)

#Ejercicio 05: Conversion decimal a binario (inicio)
#Complejidad de tiempo O(n)
#Complejidad de espacio O(1)
def conversor_binario(num_decimal):
    pila_oper = PilaArray()
    resultado_final = ""
    while num_decimal >= 0:
        resultado = num_decimal % 2
        pila_oper.push(resultado)
        num_decimal = num_decimal // 2
        if num_decimal == 0 or num_decimal == 1:
            pila_oper.push(num_decimal)
            break

    while pila_oper.size() > 0:
        resultado_final += str(pila_oper.pop())

    return resultado_final


numero = 8

print(conversor_binario(numero))


#Ejercicio 05: Conversion decimal a binario (fin)

#Ejerciccio 06: Pila limitada clase (inicio, terminado)
class PilaLimitada(PilaArray):
    def __init__(self, limite):
        super().__init__()
        self.limite = limite
        self.contador = 0

    def push(self, valor):
        if self.contador >= self.limite:
            raise Exception("Error: Pila desbordada")
        super().push(valor)
        self.contador += 1

    def pop(self):
        self.contador -= 1
        return super().pop()

#Ejerciccio 06: Pila limitada clase (inicio)

#Ejercicio 07: Palindromos (inicio, terminado)
#Complejidad de tiempo O(n)
#Complejidad de espacio O(n)
def es_palindromo(cadena):
    cad_pila = PilaArray()
    pila_mitad = PilaArray()
    for caracter in cadena:
        cad_pila.push(caracter)

    if (len(cadena) % 2 == 0):
        num_apilar = len(cadena) // 2
        for i in range(num_apilar):
            pila_mitad.push(cad_pila.pop())

        cadena_mitad1 = ""
        cadena_mitad2 = ""

        for i in range(cad_pila.size()):
            cadena_mitad1 += cad_pila.pop()

        for i in range(pila_mitad.size()):
            cadena_mitad2 += pila_mitad.pop()

        return cadena_mitad1 == cadena_mitad2

    else:
        num_apilar = len(cadena) // 2
        for i in range(num_apilar):
            pila_mitad.push(cad_pila.pop())

        cad_pila.pop() # caracter medio
        cadena_mitad1 = ""
        cadena_mitad2 = ""

        for i in range(cad_pila.size()):
            cadena_mitad1 += cad_pila.pop()

        for i in range(pila_mitad.size()):
            cadena_mitad2 += pila_mitad.pop()

        return cadena_mitad1 == cadena_mitad2


palabra = "selles"

print(es_palindromo(palabra))


#Ejercicio 07: Palindromos (fin)

#Ejercicio 08: Historial web (inicio, terminado)
class Historial_web(PilaArray):
    def __init__(self):
        super().__init__()

    def navegar_pagina(self, url):
        self.push(url)
        return self.top()

    def retroceder_pagina(self):
        self.pop()
        return self.top()

    def pagina_actual(self):
        return self.top()


historial_prueba = Historial_web()

historial_prueba.navegar_pagina("www.tecsup.edu.pe")
print(historial_prueba.pagina_actual())
print(historial_prueba.navegar_pagina("www.google.com"))

print(historial_prueba.retroceder_pagina())

#Ejercicio 08: Historial web (fin)

#Ejercicio 09: Torres de hanoi (inicio, terminado)
#Complejidad de tiempo O(n)
#Complejidad de espacio O(n)
def torres_de_hanoi(n, origen, auxiliar, destino):

    if n == 1:
        print(f"Mover disco {n} desde {origen} a {destino}")
    else:
        torres_de_hanoi(n - 1, origen, destino, auxiliar)
        print(f"Mover disco {n} desde {origen} a {destino}")
        torres_de_hanoi(n - 1, auxiliar, origen, destino)

n = 3  # Número de discos
torres_de_hanoi(n, 'Torre A', 'Torre B', 'Torre C')
#Ejercicio 09: Torres de hanoi (fin)