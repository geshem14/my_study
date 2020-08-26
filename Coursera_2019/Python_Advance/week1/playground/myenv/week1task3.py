import sys

digit_string = sys.argv[1]
sumOfChars = 0
for char in digit_string:
    sumOfChars += int(char)
print(sumOfChars)
