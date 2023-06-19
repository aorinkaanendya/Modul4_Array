bilangan = int(input("Masukan jumlah kata: "))
kata = []
for x in range(bilangan):
    kata.append(input("Masukan kata: "))
if x == bilangan - 1:
    print("")
cari = input("Masukan kata yang ingin dicari: ")
for h in kata:
    if(h == cari):
        print(cari,"Ditemukan pada indeks ke-",kata.index(h))
else:
    print("Data tidak ditemukan !")

