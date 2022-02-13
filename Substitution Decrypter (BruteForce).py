Cipher = input("Enter Cipher Text: ")
def decrypt(string, shift):
 
  cipher = ''
  for char in string: 
    if char == ' ':
      cipher = cipher + char
    elif  char.isupper(): # isupper() checks that whether the letters are uppercase(true) or lowercase(false).
      cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65) # In ASCII uppercase letters start from 65 (decimal).
    elif char.islower():
      cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97) # In ASCII lowercase letters start from 97 (decimal).
    else:
      cipher = cipher + char
  
  return cipher
Key = 0
for Key in range(25):
    Key += 1
    print(decrypt(Cipher, Key))
