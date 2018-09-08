def list_sort(lista):
    if not type(lista)==list:
        return('Invalid Input')
    else:
        final={}
        evens=[]
        final['evens']=[]
        odds=[]
        final['odds']=[]
        chars=[]
        final['chars']=[]

        for i in lista:
            if type(i)==int or type(i)==float:
                if i%2==0:
                    evens.append(i)
                    final['evens']=sorted(evens)
                elif i%2==1:
                    odds.append(i)
                    final['odds']=sorted(odds)
            else:
                chars.append(i)
                final['chars']=sorted(chars)
        return(final)
   


y=[4,3,2]
print(list_sort(y))