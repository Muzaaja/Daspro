"""Nama : Muhammad Zaidan Rahman
Kelas : 1B
NIM : 2404903"""

panjang = 100
lebar = 4800
mKeKM = 1000
CmKeKM = 100000
pKM = float(panjang/mKeKM)
lKM = float(lebar/CmKeKM)

KelilingPersegiP = float(2 * pKM + 2 * lKM)
total = float(KelilingPersegiP * 10)
print(float(total))

#atau

panjang2 = 100/1000
lebar2 = 4800/100000
KelilingPersegiP2 = (2 * panjang2 + 2 * lebar2)
print(KelilingPersegiP2 * 10)

"""Bu Rinda merupakan seorang mantan altlet lari dan berencana untuk berlari sore ini.
Running track yang akan digunakan beliau memiliki ukuran panjang 100 meter, lebar
4800 centimeter. Beliau berencana akan berlari sebanyak 10x putaran. Buatlah sebuah
program untuk menghitung total jarak yang akan ditempuh oleh Bu Rinda dalam satuan
kilometer. Gunakan rumus menghitung keliling persegi panjang."""