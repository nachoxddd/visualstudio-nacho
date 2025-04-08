#coleccion de datos
#LISTAS, colecciones ordenadas de datos mutables 
lista = ['ignacio', 49, True]
print(lista)
print(type(lista))

print([45,46,47])
print(type([45,46,47]))

print(lista[1])
lista[1] = 35
print(lista)

#DICCIONARIOS, colecciones ordenadas de pares datos o elementos mutables (lista es corchete "[]" y para diccionario es "{}")
diccionario = {'nombre':'ignacio','edad':49,'es_alumno':True}
print(diccionario)
print(type(diccionario))
print(diccionario['edad'])
diccionario['edad'] = 45
print(diccionario)

#CONJUNTOS, coleccion desordenada de elementos
conjunto = {'ignacio',49,True}
print(conjunto)
print(type(conjunto))

conjunto.add(45)
print(conjunto)
conjunto.pop()
print(conjunto)
conjunto.pop
print(conjunto)

# TUPLA, coleccion INMUTABLE de elementos
tupla = ('ignacio', 49, True)
print(tupla)
print(type(tupla))

tupla [2] =45
print(tupla[2])
