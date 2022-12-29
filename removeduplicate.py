# This code takes input from user and convert it to strings  and filter out the 
#  duplicatate characters in the user input and display the characters that has the highest occurance and display number of times it occur in the string
# example a = "hdhhhg" h is maximum and is 4 in number

string = ""
maxchar1  = ""
maxchar2 = ""
duplicates = []

user = input("Enter a value: \n")

while len(user) < 1:
	print("You have not Entered anything, please enter a value first: \n")
	user = input("Enter a value: \n")
if len(user) > 1:
	string += user.lower()

if len(string) > 1:
    string += user
else:
    print("Please enter a value\n")
    userInput = input("Enter characters: \n")


# store the duplicate values in a list
for i in string:
    if string.replace(" ", "").count(i) > 1:

        if i not in duplicates:
            duplicates.append(i)

#store the number of times each character
#appear in the string in a list
maxN = []

for r in duplicates:
	if r not in maxN:
		maxN.append(string.count(r))

# create empty list to store characters that has the highest occurance
maxChar = [] 

outputText = "{} are the duplicates and also the maximum characters because {} appears {} times more  than other characters in the string"

if len(maxN) > 0:
    for k in string:
        if string.count(k) == max(maxN):
            maxChar.append(k)
    for n in maxChar:
        if maxChar.count(n) == max(maxN):
            maxchar1 += n
    charset = set(maxchar1)
    for characters in charset:
        maxchar2 += characters + ", "
    print(outputText.format(maxchar2, maxchar2,  max(maxN)))
									
else:
	print("No duplicate or maximum character found")
