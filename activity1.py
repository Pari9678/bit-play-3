input("XOR swap - exchange 2 values without the thrid variable. Press Enter ")
print(" before: a = 5, b = 9")
a, b = 5, 9
a^=b; b^=a; a^=b
print(" after: a =", a, "b =", b)

n = int(input("Enter a number: "))
guess = input("After XOR swap of " + str(n) + " and 8 what does n become?")
a, b = n, 8
a^=b; b^=a; a^=b
input("XOR swap exchanges values. Press Enter ")
print(" n become:", a, " your guess:", guess)