# 555-GET-FOOD
'''
Many companies use telephone numbers like 555-GET-FOOD so the number is
easier for their customers to remember. Write a program that asks the
user to enter a 10-character telephone number in the format XXX-XXX-XXXX.
The application should display the telephone number with any alphabetic
characters that appeared in the original translated to their numeric equivalent.
'''

phoneNumber = input("Enter a phone number to be translated: ")

translateNumber = []
i = 0

for ch in phoneNumber:

    if phoneNumber[i].isalpha():
        
        if phoneNumber[i] == 'A' or phoneNumber[i] == 'B' or phoneNumber[i] == 'C':
           translateNumber.append('2')
        elif phoneNumber[i] == 'D' or phoneNumber[i] == 'E' or phoneNumber[i] == 'F':
           translateNumber.append('3')
        elif phoneNumber[i] == 'G' or phoneNumber[i] == 'H' or phoneNumber[i] == 'I':
           translateNumber.append('4')
        elif phoneNumber[i] == 'J' or phoneNumber[i] == 'K' or phoneNumber[i] == 'L':
           translateNumber.append('5')
        elif phoneNumber[i] == 'M' or phoneNumber[i] == 'N' or phoneNumber[i] == 'O':
           translateNumber.append('6')
        elif phoneNumber[i] == 'P' or phoneNumber[i] == 'Q' or phoneNumber[i] == 'R' or phoneNumber[i] == 'S':
           translateNumber.append('7')
        elif phoneNumber[i] == 'T' or phoneNumber[i] == 'U' or phoneNumber[i] == 'V':
           translateNumber.append('8')
        else:
            translateNumber.append('9')
    else:
        translateNumber.append(phoneNumber[i])
        
    i += 1
j=0
for len in translateNumber:
    print(translateNumber[j], end="")
    j+=1

