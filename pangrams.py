# A pangram is a sentence containing all 26 letters of the English Alphabet 

def pangram(s):
    s=s.replace(" ","")
    s=s.lower()
    s=set(s)
    if len(s)==26:
        return "Pangram"
    return "Not Pangram"

a = "We promptly judged antique ivory buckles for the prize"
print(pangram(a))
b = "The quick brown fox jumps over the lazy dog"
print(pangram(b))