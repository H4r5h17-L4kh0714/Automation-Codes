d = input("Decimal : ").split()
e = ""
b = ""
o = ""
x = ""
a = ""
for i in d:
    g = int(i)
    b += str(bin(g))
    o += str(oct(g))
    x += str(hex(g))
    a += chr(g)
    
print("Binary : " + str(b)) # As python cannot concatenate a string and integer together, we converted them to string with str().
print("Octal : " + str(o))
print("Hexadecimal : " + str(x))
print("ASCII : " + a)
