string1= input("Enter your sentence: ")
total= 1

for i in range(len(string1)):
    if string1[i] == ' ': 
        total= total +1

print("This number of words in this string = ",total)        