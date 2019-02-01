#1
mis_valores = [5, 6, 10, 13, 3, 4]
promedio = sum(mis_valores)/len(mis_valores)
print("1- El promedio de la lista :",mis_valores," es : ",promedio)

#2

todos = [

[177,145,167,190,140,150,180,130], # grupo 1

[165,176,145,189,170,189,159,190], # grupo 2

[145,136,178,200,123,145,145,134], # grupo 3

[201,110,187,175,156,165,156,135], # grupo 4
]
maximo_lista=max(todos[0]),max(todos[1]),max(todos[2]),max(todos[3])
max_lista=list(maximo_lista)
maximo=max(max_lista)
print("2- El numero maximo de la lista",todos, " es ", maximo," y pertenece al grupo: ", max_lista.index(maximo)+1)
