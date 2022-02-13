from itertools import cycle
import sys

print("WARNING: This program will encrypt or decrypt the very file you give, it will not make another file, so enter only if you want the cipher or plain file to be encrypted or decrypted.")
inp = input("Enter C if you want to continue, anything else if not: ")

def main():
    file = input("Enter the file directory: ")
    key = input("Enter the key: ")
    key = key.encode()

    def Multi_Byte_XOR(cipher,key):
        return bytes(i^j for i,j in zip(cipher,cycle(key)))

    f = open(file,'rb')
    g = f.read()
    encr = Multi_Byte_XOR(g,key)
    f.close()
    f = open(file,'wb')
    f.write(encr)
    f.close()

if inp == "C" or inp == "c":
    main()
else:
    sys.exit()
