msg = input("Enter the message you want to encrypt")
shift_code= int(input("Must enter a shift value in range from 1 to 25"))
text=""
for ch in msg:
    if not ch.isalpha():
        text += ch
        continue
    code=ord(ch)-shift_code
    if ch.isupper():
        while code > ord('Z'):
            code = code-26
    elif ch.islower():
        while code > ord('z'):
            code = code-26
    text += chr(code)
print(text)