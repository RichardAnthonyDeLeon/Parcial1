

#Escribe una función en Python que reciba una lista como parámetro y devuelva la suma de todos los elementos de la lista.
def suma(lista):
    suma = 0
    while lista:
        ultimo = lista.pop() # accedemos con un while a el último elemento de la lista y lo vamos almacenando 
        suma = suma + ultimo  # vamos sumando los elementos almacenados
    print('Suma: ',suma)
lista = [1,2,3,8,9,5,6]
suma(lista)    



#Define una función llamada "inverso_palabra" que reciba una cadena como parámetro y devuelva la
#cadena invertida. Por ejemplo, si la entrada es "python", la salida
#debería ser "nohtyp".
def invertir_cadena_manual(cadena):
    cadena_invertida = "" # Creamos una cadena vacía para ir almacenando las letras
    for letra in cadena:
        cadena_invertida = letra + cadena_invertida #Concatenamos de manera que la primer letra de la cadena se vaya corriendo hasta la última posicioón
    return cadena_invertida

cadena = 'hola'
print(invertir_cadena_manual(cadena))




#Escribe un programa que pida al usuario una lista de números y luego
#imprima la suma de los números
#pares en la lista.

# lista = input('Ingrese números separados por ,')
# listaNueva = lista.split()

# while listaNueva:
#     numeroUltimo = int(ultimo = listaNueva.pop())
#     suma = suma + numeroUltimo
# print(suma)




#Crea un diccionario en Python que represente un libro, con claves como "título", "autor" y "año de
#publicación". Luego, escribe un código que agregue un nuevo campo al
#diccionario, como "género", y
#lo imprima.


# datos = {
#     'titulo': 'DogBoy',
#     'Autor': 'Monika Zak',
#     'Año': 2005   
# }




