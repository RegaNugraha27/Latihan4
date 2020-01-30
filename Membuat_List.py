print ("\n<><><><><><><><><><><><><><><><><><><><><><><>\n")
print ("\t\tLATIHAN\t\t")
print ("\n<><><><><><><><><><><><><><><><><><><><><><><>\n")
List = [1, 4, 6, 8, 11, 19]

#Akses List
print("Akses List")
Data1 = List[3]
Data2 = List[2:4]
Data3 = List[-1]
print(Data1)
print(Data2)
print(Data3)

#Ubah Elemen List
print("Ubah Elemen List")
print(List)
List[4] = 80
print(List)
List[4:6] = [90, 20]
print(List)

#Menambahkan Elemen List
print("Menambahkan Elemen List")
print(List)
a = List
print(a)
b = a[2:4]
print(b)
b.append(15)
b.extend([16, 17, 18])
print(b)
c = a + b
a.extend(b)
print(c)
print ("\n<><><><><><><><>TerimaKasih<><><><><><><><><><><>\n")
print ("Rega Nugraha")
print ("TI.19.D.1")
print ("311910481")
print ("UNIVERSITAS PELITA BANGSA")
print ("\n<><><><><><><><><><><><><><><><><><><><><><><><><>\n")