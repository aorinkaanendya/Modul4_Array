#1. cara menampilkan array
buah = ["Apel", "Jeruk", "Anggur","Pisang"] 
nilai = buah[1] 
print(nilai) 

#2. cara merubah nilai array
buah = ["Apel", "Jeruk", "Anggur","Pisang"] 
buah[1] = "Melon"
print(buah)

#3. mengetahui panjang array
buah = ["Apel", "Jeruk", "Anggur","Pisang"] 
panjang = len(buah) 
print(panjang) 

#4. looping elemen array
buah = ["Apel", "Jeruk", "Anggur","Pisang"] 
for x in buah: 
    print(x) 

#5. menambah elemen array
buah = ["Apel", "Jeruk", "Anggur","Pisang"] 
buah.append("Delima")
print(buah)

#6. menghapus elemen array
buah = ["Apel", "Jeruk", "Anggur","Pisang"] 
buah.pop(2)
buah.remove("Jeruk")

print(buah)

#menampilkan bilangan bulat
bil = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in bil:
    if x % 2 == 0:
        genap = x

        print(genap)     
        
        
#array 1 dimensi
buah = ["Apel", "Jeruk", "Anggur","Pisang"] 
for x in buah: 
    print(x) 
        
#array 2 dimensi
buah = [["Pisang", "Jeruk", "Pir", "Jambu"], 
        ["Nanas","Melon", "Delima"]]

for i in range(len(buah)):
    for x in range(len(buah[i])):
        print(buah[i][x])
        