size = int(input("masukkan "))

n=1
for i in range(size):
	for j in range(0, i + 1):
		print(n, end= " ")
		n = n+1
	print()

