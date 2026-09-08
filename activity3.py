input("XOR sign detection - n ^ m < 0 means different signs. Press Enter ")
print(" 4 ^ 2 =", 4 ^ 2, "same signs means positive")
print(" 4 ^ -2 =", 4 ^ -2, "different signs mean negative")

n = int(input("Enter a number: "))
guess = input("Will " + str(n) + " ^ -8 be positive or negative?")
input("XOR is negative when signs differ. Press Enter ")
print(" ", n, "^ -8 =", n ^ -8, " your guess:", guess)