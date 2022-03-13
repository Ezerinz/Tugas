a = ['sapi', 'mangga', 'apel', 'kambing', 'burung']
print(a)

#Mengakses List
print(a[1]) #Mengakses satu item
print(a[0:3]) #Mengakses beberapa item

#Mengganti List
a [1] = 'kelapa'

#Menambahkan
a.append('anggur')
a.insert(1, 'anggur')

#Menghapus
a.pop(2)
a.remove('kambing')
del a [1]
a.clear() #mengosongkan
