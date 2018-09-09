def sort(lista):
    if type(lista)!=list:
        return('Invalid Input')
    if lista==[]:
        return('Empty list')
    for a in lista:
        if type(a)!=int:
            return('List should contain numbers')
    n=len(lista)
    print(n)
    last_value=lista[n-1]
    print(last_value)
    listb=[]
    for i in range(last_value):
        if i not in lista:
            listb.append(i)
    return(listb)
        
            
v=[1,6,9]
print(sort(v))


