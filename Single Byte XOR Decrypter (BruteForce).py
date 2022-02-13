from itertools import cycle
from codecs import *

def bytexor(ciphertext,key):
    return ascii(bytes([ ord(i)^(j) for i,j in zip(ciphertext,cycle(key))]))

ct = input("Enter Ciphertext in Decimal with Spaces Between Each Number : ").split()
ct2 = ""
key = ""
ORD = -1

for h in ct:
        ct2 += " " + chr(int(h))

m = ""
x = 0
v = 63
k = 96
y = 32
 
for i in range(256):
    key = chr(i).encode()
    ORD += 1
    b = bytexor(ct2,key)
    if ORD < 33:
        b = bytexor(ct2,key).replace(chr(y),"")
        y += 1
    if i > 32 and i < 65:
        x += 1
        ax = hex(x)
        b = bytexor(ct2,key).split(chr(92) + ax.replace("0","")) # Let l be a string and 'a' and 'b' are two characters. l.replace("a","b") replaces 'a' with 'b' in string 'l'.
    if i > 64 and i <95:
        k += 1
        b = bytexor(ct2,key).replace(chr(k),"")
    if i > 95 and i < 128:
        v += 1
        b = bytexor(ct2,key).replace(chr(v),"")
    print(str(ORD) + ": " + str(m.join(b))) # Let x be any variable and l be any list. x.join(l) joins all the elements of the list.
