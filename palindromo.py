palabra=input("Ingrese una palabra para corroborar que si es una anagrama : ")
palabra_vuelta=palabra[::-1]
print(palabra_vuelta)
if palabra == palabra_vuelta:
    print("ANAGRAMA")
else:
    print("NO ES")

