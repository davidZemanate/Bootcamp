numbers = [1,2,3,4,5,6]
for i in numbers:
    print("Aqui i es igual a:",i+1)
    
for i in  range(3, 10):
    print(i)
    
fruits = ["Manzana","Uva","Fresa","Mango"]
for fruta in fruits:
    print(fruta)
    if fruta == "Manzana":
        print("Manzana encontrada")
        
x=0

while x<5:
    if x==3:
        break
    print(x)
    x+=1
numbers = [1,2,3,4,5,6]
for i in numbers:
    if i==3:
        break
    print("Aqui i es igual a:",i+1)