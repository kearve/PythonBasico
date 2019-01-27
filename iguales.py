palabra1=input("Digite la primera palabra: ")
palabra2=input("Digite la segunda palabra: ")
esta=0
lista1=sorted(list(palabra1))
lista2=sorted(list(palabra2))

print(lista1,lista2)
if lista1 == lista2:
    print("Iguales")
else:
    print("Diferentes")
