# Given an items in a collection, scan through every items in the collection and check indices whose sum will give a target. Example, Items[1] + items[4] = 13. 

                # solutin

items = [2, 4, 6, 8, 9] ; target = 8


for i in range(len(items)):
	for j in range(i + 1, len(items)):
	
		if (items[i] + items[j]) == target:
			print(i, end=" and ")
			print(j, end=", are the indices in the list below that will give the target")
		
print(" \n")
print(items)
