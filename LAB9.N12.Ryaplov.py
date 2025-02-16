f1 = open ("C:/Users/Artyom/Desktop/numtxt.txt", 'r')# файл с исзодными данными
a=f1.read()
lst=list(map(int, a.split(", ")))
f1.close()
print(lst)
lst_max=lst[0]-1
ind=0
s=0
for i in range (len(lst)):
    if lst[i]<0 and ind==0:
        i_ng=i
        ind=1
    s+=lst[i]
    if lst[i]>lst_max:
        lst_max=lst[i]
        s=0
lst[i_ng]=s
print(lst)
lst=list(map(str, lst))
s=", ".join(lst)
print(s)
f1 = open ("C:/Users/Artyom/Desktop/numtxt.txt", 'w')
f1.write(s)# изменили данные в файле
f1.close()


        
