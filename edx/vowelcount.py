# Program to count vowels {a,e,i,o,u} in a given Sring variable.
s = 'azcbobobegghakl'
numVowels = 0
for letter in s:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        numVowels += 1
print("Number of vowels: " + str(numVowels))
