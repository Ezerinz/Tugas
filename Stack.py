stack = []
max_size = int(input("Masukkan Ukuran Maksimal Stack: "))

def isEmpty():
	if len(stack) == 0:
		print("Stack Kosong.")
		return True
	return False
	
def isFull():
	if len(stack) == max_size:
		print("Stack Penuh.")
		return True
	return False
		
def pop():
	if isEmpty() == False:
		print(stack.pop(), "terhapus.")

def push():
	if isFull() == False:
		x = input("Masukkan Item Baru: ")
		stack.append(x)
		print(x, "ditambahkan.")
		
def peek():
	if isEmpty() == False:
		print("Top: ", stack[-1])


p = 0
while p != '6':
    print('''\n1. Push => Menambah Item
2. Pop => Menghapus Item
3. Peek => Melihat Item Teratas
4. Empty => Memeriksa Apakah Stack Penuh
5. Size => Melihat Ukuran Stack''')
    p = input("Ketik 6 untuk berhenti\nMasukkan Perintah: ")
    print()
    
    if p == '1':
    	push()
    elif p == '2':
    	pop()
    elif p == '3':
    	peek()
    elif p == '4':
    	if isEmpty() == False:
    		print("Stack memiliki isi.")
    elif p == '5':
    	print("Ukuran stack saat ini: ", len(stack), "\nUkuran maksimal stack: ", max_size)