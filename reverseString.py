string= input("Enter your word: ")

string2= ('')
#loop for printing in reverse
for i in string:
    string2= i + string2
    string2= string2.lower()

print("\nOriginal string = ", string)    
print("Reversed string = ", string2)    