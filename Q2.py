print("The character pattern ")
asciiValue = 65     #ASCII value of A
for i in range(0, 5):
    for j in range(0, i + 1):
        # It will convert the ASCII value to the character
        alphabate = chr(asciiValue)
        print(alphabate, end=' ')
        asciiValue += 1
    print()  