from itertools import cycle

h = input("Please Enter '1' for encryption and '2' for Decryption: ")

if h == "1":
    def bytexor(plaintext,key):
        return bytes([ ord(i)^ord(j) for i,j in zip(plaintext,(cycle(key)))])
    
    pt = input("Please Enter Plaintext: ")
    key = input("Please Enter Key in ASCII: ")
    bx = bytexor(pt,key)

    d = ""
    for i in bx:
        d += str(i) + " "

    b = ""
    for i in bx:
        b += str(bin(i)) + " "

    o = ""
    for i in bx:
        o += str(oct(i)) + " "

    h = ""
    for i in bx:
        h += str(hex(i)) + " "

    print("ASCII : " + str(bx))
    print("Decimal : " + d)
    print("Binary : " + b)
    print("Octal : " + o)
    print("Hexadecimal : " + h)

if h == "2":
    def bytexor(ciphertext,key):
        return bytes([ int(i)^ord(j) for i,j in zip(ciphertext,(cycle(key)))])

    ct = input("Please Enter Ciphertext in Decimal with Spaces Between Each Decimal: ").split()
    dn = ""
    for i in ct:
        dn += str(chr(int(i)))
    key = input("Please Enter Key in ASCII: ")
    bx = bytexor(ct,key)
    
    print("ASCII : " + str(bx)) 
