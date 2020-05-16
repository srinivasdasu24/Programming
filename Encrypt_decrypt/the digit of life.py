dob = input("enter your dob")
digit = 0
for i in dob:
    digit += int(i)
final = 0
while digit != 0:
    final += digit % 10
    digit = digit // 10
    if final > 9:
        digit = final
        final = 0

print(final)