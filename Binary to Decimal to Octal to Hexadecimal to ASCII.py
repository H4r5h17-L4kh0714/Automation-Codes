b = input("Binary : ").split()
d = ""
e = ""
a = ""
for i in b:
    d += str(int(i, 2))
    e += " " + str(int(i, 2))
    a += chr(int(i, 2))
de = int(d, 10)
print("Decimal : " + str(e))
print("Octal : " + str(oct(de)))
print("Hexadecimal : " + str(hex(de)))
print("ASCII : " + a)
# As python cannot concatenate a string and integer together, we converted them to string with str().
