from simplecrypt import decrypt


passwords = []
with open("passwords.txt", "r") as inp:
    passwords = inp.readlines() 

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()

print(passwords, encrypted)

for password in passwords:
    print(password[:-1])
    try:
        print(decrypt(password[:-1], encrypted))
    except BaseException:
        print("Nope")