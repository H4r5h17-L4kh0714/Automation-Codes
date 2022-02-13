o = input("Octal : ").split()
d = ""
e = ""
f = ""
g = ""
for i in o:
    d += str(int(i, base = 8)) + " "
    e += str(bin(int(i, base = 8))) + " "
    f += str(hex(int(i, base = 8))) + " "
    g += chr(int(i, base = 8))
print("Decimal : " + (d))
print("Binary : " + (e))
print("Hexadecimal : " + (f))
# As python cannot concatenate a string and integer together, we converted them to string with str().
print("ASCII :",g)