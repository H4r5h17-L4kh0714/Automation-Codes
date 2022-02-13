RPT = input("Please enter the ACII String: ")
RPT = list(RPT)

CT = ""
CT2 = ""
CT3 = ""
CT4 = ""

for i in RPT:
    CT += str(ord(i)) + " "
    CT2 += str(hex(ord(i))) + " "
    CT3 += str(bin(ord(i))) + " "
    CT4 += str(oct(ord(i))) + " "
print("Decimal:",CT)
print("Hexadecimal:",CT2)
print("Binary:",CT3)
print("Octal:",CT4)
