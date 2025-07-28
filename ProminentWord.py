text= input("Enter you sentence: ")
text= text.split()
Len_bigWord= 0

for word in text:
    wordLen= len(word)
    if wordLen>Len_bigWord:
        Len_bigWord = wordLen

print("\nLargest Word: ")
for word in text:
    wordLen= len(word)
    if wordLen == Len_bigWord:
        print(word)