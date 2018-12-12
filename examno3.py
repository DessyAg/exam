def rowSumOddNumbers(n) :
	thelist = []
	nilai = 1

	for i in range(1, n+1): 
		rowlist = []
		for j in range (i):
			rowlist.append(nilai)
			nilai += 2
		thelist.append(rowlist)
	return thelist

row = 3
nilai3 = rowSumOddNumbers(row)
print(sum(nilai3[row-1]))
