string = "james"

duplicates = []


# store the duplicate values in a list
for i in string:
    if string.replace(" ", "").count(i) > 1:

        if i not in duplicates:
            duplicates.append(i)
    else:
        print("No duplicate value")
						


#store the numbers of times each character
#appear in the string in a list
maxN = []
for r in duplicates:
	if r not in maxN:
		maxN.append(string.count(r))


# create empty list to store characters that has the highest occuranc
maxChar = [] 


outputText = "{} is the maximum character because it appears {} times than others"


for k in string:
	if string.count(k) == max(maxN) and maxN.len() != 0:
		maxChar.append(k)
		
print(outputText.format(maxChar[1], max(maxN)))

