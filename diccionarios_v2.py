numbers = {1:"uno", 2:"dos", 3:"tres"} # en llaves

print(numbers)
print(numbers[1])
print(numbers[2])
print(numbers[3])

information = {"nombre" :"David",
               "apellido":"zemanate",
               "estatura":172,
               "edad":23}
print(information)
del information["apellido"]
print(information)

claves = information.keys()
print(claves)
print(type(claves))
values = information.values()
print(values)
pairs = information.items()
print(pairs)


contacts={"David":{"apellido":"Zemanate",
                   "altura":172, 
                   "edad":23,
                   "telefono":3118868050,
                   "signo zodiacal":"geminis",
                   "serie favorita":"Game of Thrones",
                   "canción favorita":"Hermanos Lebron - Fe",
                   "comida favorita":"arroz con pollo",
                   "lugar soñado vacaciones":"noruega",
                   "habilidad secreta":"estratega",
                   "pasatiempo":"jugar futbol",
                   "heroe o persona que admiras": "Mamá",
                   "libro que mas me ha impactado":"--",
                   "cenar con alguien":"Javier Santaolalla",
                   "que logro personal te enorgullese":"aprender python",},
            "Luz milena":{"apellido":"daza",
                          "altura":1.65,
                          "edad":56,
                          "parentesco":"mamá",
                          "color faavorito":"azul"
                          }
          }

print(contacts)