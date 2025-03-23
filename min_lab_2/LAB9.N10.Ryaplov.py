#10. удалить минимальный положительный элемент из списка
f1 = open ("LAB9.numtxt.txt", 'r')# файл с исзодными данными
a=f1.read()
lst=list(map(int, a.split(", ")))
f1.close()
print(lst)
lst_min=lst[0]+1
for i in range (len(lst)):
    if lst[i]>0:
        if lst[i]<lst_min:
            lst_min=lst[i]
            i_min=i
print(i_min)
lst.pop(i_min)
print(lst)
lst=list(map(str, lst))
s=", ".join(lst)
f1 = open ("numtxt.txt", 'w')
f1.write(s)# изменили данные в файле
f1.close()


        
