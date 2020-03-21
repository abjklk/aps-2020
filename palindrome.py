def createPalindrome(inp, isOdd): 
    n = inp 
    palin = inp
    
    if (isOdd): 
        n = n // 10

    while (n > 0):
        palin = palin * 10 + (n % 10) 
        n = n // 10
    return palin

def generatePalindromes(n):
    for j in [0,1]:
        i = 1
        while (createPalindrome(i, j % 2) < n): 
            print(createPalindrome(i, j % 2)) 
            i = i + 1
n = 141
generatePalindromes(n)
