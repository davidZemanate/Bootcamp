#Ejemplo de como funcionan los iteradores
#crear una lista con algunos numeros

my_list = [1,2,3,4]

#obtener el iterador de la lista
#un iterador es un objetos que nos permite recorrer una coleccion (como una lista) uno por uno

my_iter = iter(my_list)
#usar el iterardo para acceder a los elementors de la lista

print(next(my_iter))

print(next(my_iter))

print(next(my_iter))

print(next(my_iter))

text  = "David Zemanate"
iter_text=iter(text)
for char in iter_text:  
    print(char)
    
#crear un iterador que genere  números impares desde 1 hasta el limite
#range (1, limit+1, 2) esto genera numeros comenzando en 1, con saltos de 2, hasta lllegar a 9 (el limite se incluye)
odd_iter = iter(range(1,10,2)) 
for num in odd_iter: 
    print(num)
    
#definir una función generadora
def my_generator():
    #la palabra clave yield nos permite devolver un valor y pausa la funcion en ese punto
    yield 1
    yield 2
    yield 3
print("----------------------")
for value in my_generator():
    print(value)
    
#fibonacci 
#la serie de fibonacci hace referencia a que vamos a obtener un valor sumado 
#los dos anteriores [0,1,1,2,3,5,8,13...]
print("---------------")
def fibonacci(limit):
    #iniciarlizar los dos primeros numero de la secuencia de fibonacci
    a,b = 0,1.
    #continuar generando numeros mientras 'a' sea menor que el limite
    while a < limit:
       yield a #devolver el valor atual de 'a' y pausar la ejecucion de la función
       a,b=b,a+b
       
for num in fibonacci(10):
    print(num)