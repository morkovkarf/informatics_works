f1 = open("C:/Users/Artyom/Desktop/inftxt.txt", 'r', encoding="utf-8")
c=f1.read()
fcode = open("C:/Users/Artyom/Desktop/txtcode.txt", 'r', encoding="utf-8")
dctstr= {}
dctback={}
for line in fcode.readlines():
    code, word = line.strip().split('-')
    dctstr[code]=word # создаем словари
    dctback[word]=code


lst = c.split()#вводим текст в массив

for index,word in enumerate(lst): # заменяем слова на коды
    #print(index, word)
    if dctstr.get(word):
        lst[index]=dctstr.get(word)
print(lst)
for index,num in enumerate(lst):
    #print(index, num)
    if dctback.get(num):
        lst[index]=dctback.get(num)
print(lst)
f1.close()
fcode.close()
        
