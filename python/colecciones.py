conjunto = { 1, 5, 9 }

conjunto.add(10)
conjunto.remove(5)

for elem in conjunto:
  print(elem)

conjunto2 = {1, 3, 4}

print(conjunto.union(conjunto2))

#diccionarios
diccionario = {
  "nombre": "Marco",
  "edad": 19
}
diccionario["apellido"] = "Cruz"
del diccionario["edad"]
print( diccionario )

for k, v in (diccionario.items()):
  print(k, v)