# Lohgan Joseph
# 2038027

word = input()
password = ''
i = 0
#This while loop will replace and append each letter onto the password
while i < len(word):
    ch = word[i]
    if ch == 'i':
        password += '!'
    elif ch == 'a':
        password += '@'
    elif ch == 'm':
        password += 'M'
    elif ch == 'B':
        password += '8'
    elif ch == 'o':
        password += '.'
    else:
        password += ch
    i += 1
password += "q*s"
print(password)
