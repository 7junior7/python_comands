# *******************************************************CONVERSIONES********************************************************
# Algunas de las funcionalidades que nos ofreced Python son las conversiones, las cuales nos permiten modificar o cambiar el
# tipo de dato que contiene una variable
numero = 4
print float(numero) # convertimos el valor de la variable numero a float
print str(numero) # convertimos el valor de la variable numero a string (texto)

lista_no_modificable = (1,2,3,4,5)
print lista_no_modificable
lista_no_modificable_convertida = list(lista_no_modificable)
print lista_no_modificable_convertida
print type(lista_no_modificable_convertida) # convertimos la lista no modificable(tupla) a modificable (lista)
lista_no_modificable_convertida[0] = 0 # modificamos el 1er elemento de la lista
print lista_no_modificable_convertida