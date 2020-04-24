# Program to print all Kaprekar numbers in a given range
# A number is a p-Kaprekar number if the representation of its square in that base
# can be split into two parts, where the second part has p digits, that add up to the original number.
# Eg. 99 is Kaprekar number because 99**2 = 9801, 98+01=99

def kaprekarNumbers(p, q):
    flag=0
    for i in range(p,q+1):
        sq=str(i**2)
        f=sq[:len(sq)//2]
        l=sq[len(sq)//2:]
        if f=="":
            f="0"
        elif l=="":
            l="0"
        if i==int(f)+int(l):
            print(i,end=' ')
            flag=1
    if flag==0:
        print("Invalid Range")

kaprekarNumbers(1,100)