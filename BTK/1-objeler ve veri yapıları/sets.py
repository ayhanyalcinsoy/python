fruits = {'apple', 'orange', 'banana'}


#print (fruits[0]) #indeks numarası ile ulaşılamaz
# A-Z sıralanamaz
# var olan bir eleman eklenmez

fruits.add('cherry')
fruits.update(['mango', 'grape', 'apple']) # var olan bir eleman eklenmez

fruits.remove('mango')
fruits.discard('banana')
fruits.pop() #rasgele bir eleman siler

fruits.clear() #tüm elemanlar silinir

#for döngüsü ile listelenebilir
for x in fruits:
  print(x)

print(fruits)


myList = [1,2,3,5,4,4,2,1,5]
print(myList)

print(set(myList)) #Tekrarlanan elamanları siler

