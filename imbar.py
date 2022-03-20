print('''TOKO MAKANAN ENAK
Pilih Menu
1. Nasi Kuning -> Rp.10000
2. Nasi Goreng -> Rp.15000
Beli Minimal 2 Diskon 20%''')

menu = input("Pilih menunya: ")
#menghindari salah ketik menu,
#misalnya ketik menu 3
#maka akan disuruh input ulang
while menu != '1' and menu != '2':
	menu = input("Pilih ulang menu: ")
	if menu == '1' or menu == '2':
		break

jumlah = int(input("Jumlah: "))
#menghindari jika jumlah 0, disuruh ulang
while jumlah <= 0: 
	jumlah = int(input("Masukkan ulang jumlah: "))
	if jumlah >= 1:
		break
	
uang_kamu = int(input("Masukkan Uang Kamu: "))

if menu == '1':
	harga = 10000
elif menu == '2':
	harga = 15000
	
total_harga = harga*jumlah
total_diskon = total_harga*20/100

#Jika jumlah lebih dari 2, dikurang diskon
if jumlah >= 2: 
	total_bayar = total_harga - total_diskon
else:
	total_bayar = total_harga
	
kembalian = uang_kamu - total_bayar

if menu == "1":
	if jumlah == 1:
		print('''Kamu akan membeli {} nasi kuning
dengan total harga: Rp{}'''. format(jumlah, total_harga))
		print("Uang Kamu: Rp", uang_kamu)
		print("Total Bayar: Rp", total_bayar)
		if uang_kamu >= total_bayar:
			print("Kembalian: Rp", kembalian)
		else:
			print("UANG KAMU TIDAK CUKUP")
			
	if jumlah >= 2:
		print('''Kamu akan membeli {} nasi kuning
dengan total harga: Rp{}'''. format(jumlah, total_harga))
		print('''Kamu mendapat diskon sebesar 20%! 
Total Diskon: Rp''', total_diskon)
		print("Uang Kamu: Rp", uang_kamu)
		print("Total Bayar: Rp", total_bayar)
		if uang_kamu >= total_bayar:
		      print("Kembalian: Rp", kembalian)
		else:
			print("UANG KAMU TIDAK CUKUP")

#//-------------------------------//
if menu == "2":
	if jumlah == 1:
		print('''Kamu akan membeli {} nasi goreng
dengan total harga: Rp{}'''. format(jumlah, total_harga))
		print("Uang Kamu: Rp", uang_kamu)
		print("Total Bayar: Rp", total_bayar)
		if uang_kamu >= total_bayar:
			print("Kembalian: Rp", kembalian)
		else:
			print("UANG KAMU TIDAK CUKUP")
			
	if jumlah >= 2:
		print('''Kamu akan membeli {} nasi goreng
dengan total harga: Rp{}'''. format(jumlah, total_harga))
		print('''Kamu mendapat diskon sebesar 20%! 
Total Diskon: Rp''', total_diskon)
		print("Uang Kamu: Rp", uang_kamu)
		print("Total Bayar: Rp", total_bayar)
		if uang_kamu >= total_bayar:
		      print("Kembalian: Rp", kembalian)
		else:
			print("UANG KAMU TIDAK CUKUP")
		