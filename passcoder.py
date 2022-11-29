#library reqs
import random
import string

#plan:
# create empty list, define password length, def passcoder() method

word_length = 15

components = [string.ascii_letters, string.digits, "!@#$%^&*"]
chars = []

for clist in components:
    chars.append(clist)
    for item in clist:
        chars.append(item)

def passcode_gen():
    passcode = []
    for i in range(word_length):
        rchar = random.choice(chars)
        passcode.append(rchar)

    return "".join(passcode)

print(passcode_gen())