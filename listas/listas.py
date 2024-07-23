to_do=["alistar la pelicula",
       "freir la maispira",
       "preparar pasabocas"]
print(to_do)


mi_dia=["me desperte a las 5 am",
        "me aliste para ir a trabajar",
        "comer",
        "jugar partido de futbol a las 4pm"]

print(mi_dia)

numeros=[1,3,4,5,"cinco"]
print(type(numeros))


mix =["uno",2,3,4.4,True,[1,2,3,]]
print(len(mix))
print("primer elemento",mix[0])
print("Segundo elemento",mix[1])
print("Tercero elemento",mix[2])
print("Cuarto elemento",mix[3])
print("Quinto elemento",mix[4])
print("sexto elemento",mix[5])

mix.append("David")
print(mix)

mix.insert(1,["a", "b", "c", "d", "e"])
print(mix)

numbers=[1,2,22,400,445,900]
print("mayor:",max(numbers))
print("menor:",min(numbers))
del numbers[-1]
print(numbers)