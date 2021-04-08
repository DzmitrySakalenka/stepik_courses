inpOriginAlph = input()
inpReplAlphabet = input()

dictionary = {}
for i in range(len(inpOriginAlph)):
    key = inpOriginAlph[i]
    dictionary[key] = inpReplAlphabet[i]

inpText = input()
cipher = ""
for i in range(0,len(inpText)):
    if inpText[i] in dictionary:
        cipher += dictionary[inpText[i]]

inpCipher = input()
text = ""
for i in range(0,len(inpCipher)):
    for key in dictionary:
        if dictionary.get(key) == inpCipher[i]:
            text += key

print(cipher)
print(text)