# Lohgan Joseph
# 2038027

term = input()

input_value = term

input_value = input_value.lower()

input_value = input_value.replace(" ", "")

low = 0
high = len(input_value) - 1
result = True

while(low<high):

    if(input_value[low]!=input_value[high]):
        result = False

    low+=1

    high-=1

if result:
    print(term, "is a palindrome")

else:
    print(term, "is not a palindrome")