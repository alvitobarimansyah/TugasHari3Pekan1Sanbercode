# soal no 1

# comparison tipe data string

a = "Indonesia"
b = "Konoha"

if a == b:
    print('sama')
else:
    print('beda')
    
# comparison tipe data boolean

print(10 > 5)

# comparison tipe data integer

a = 10
b = 20
c = a + b

if c < 25:
    print('salah')
else:
    print('benar')

# soal no 2

# comparison and

x = 15

if x > 10 and x < 20:
    print('benar')
else:
    print('salah')
    
# comparison or
 
y = 25

if y < 10 or y > 20 :
    print('benar')
else:
    print('salah')
    
# comparison not

i = not a
print(i)

# soal no 3

ruangan = 'Kamar'
size = 20

if size > 12:
    print('Besar')
elif size > 6:
    print('Sedang')
else:
    print('Kecil')

#  soal no 4

def bilangan(angka):
    if angka >= 2 and angka <= 5 or angka %2 == 0 and angka > 20:
        print('Tidak Aneh')
    else:
        print('Aneh')
bilangan(18)

# soal no 5

For loop digunakan untuk melakukan perlakuan yang sama dan berulang kepada setiap komponen / elemen pada list yang ada, sedangkan
while loop melakukan perulangan selama statement/ kondisi pada while loop tersebut benar/ TRUE.

# contoh while loop

angka = 0

while angka < 10:
    if angka == 5:
        angka += 1
        continue
        
    print('nilai angka adalah:',angka)
    angka += 1
else:
    print('nilai angka diakhir while adalah', angka)

contoh for loop
for i in range(1,10):
    if i == 6:
        print("nilai i adalah",6)

# soal no 6
a = 10

def fungsi_while(angka):
    while angka > 0:
        print(angka)
        angka -= 1

fungsi_while(a)

# soal no 7

obj_list= [1, 16, 11, 10, 5]

for index,i in enumerate(obj_list):
    print(index * i)
    