import hashlib
string = input("Enter the String: ").encode()
hex_value = hashlib.md5(string).hexdigest()
byte_value = hashlib.md5(string).digest()
print("Hexadecimal Value: " + str(hex_value))
print("Bytes: " + str(byte_value))
