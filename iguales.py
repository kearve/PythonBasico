palabra1=input("Digite la primera palabra: ")
palabra2=input("Digite la segunda palabra: ")
esta=0
if len(palabra1) == len(palabra2):
    for x in palabra1: 
        if not x in palabra2:
            esta=1
    if esta==1:
        print("Diferentes")
    else:
        print("Iguales")
else:
    print("Diferentes")
