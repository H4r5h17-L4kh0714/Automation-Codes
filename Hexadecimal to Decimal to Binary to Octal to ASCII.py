x = input("Hexadecimal with Spaces between each number: ").split()
d = ""
e = ""
f = ""
for i in x:
    d += " " + str(int(i, base = 16))
    e += str(int(i, base = 16))
    f += chr(int(i, base = 16))
print("Decimal : " + str(d)) # As python cannot concatenate a string and integer together, we converted 'd' to string.
print("Binary : " + bin(int(e)))
print("Octal : " + oct(int(e)))
print("ASCII : " + f) 