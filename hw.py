print("      BITWISE SWAP CHALLENGE")

print("\nSTEP 1: Swap Without a Third Variable")
a = 10
b = 20
print("Before swap:")
print("a =", a)
print("b =", b)
a = a + b
b = a - b
a = a - b
print("After swap:")
print("a =", a)
print("b =", b)

print("STEP 2: XOR Swap")
x = 15
y = 25
print("Before swap:")
print("x =", x)
print("y =", y)
x = x ^ y
y = x ^ y
x = x ^ y
print("After swap:")
print("x =", x)
print("y =", y)

print("STEP 3: Left Shift to Double Numbers")
number = 6
print("Original number:", number)
print("Binary:", bin(number))
double = number << 1
multiply_by_4 = number << 2
print("Shift left by 1:", double)
print("Shift left by 2:", multiply_by_4)

print("STEP 4: Detect Different Signs with XOR")
num1 = -8
num2 = 12
negative1 = num1 < 0
negative2 = num2 < 0
different_signs = negative1 ^ negative2
print("Number 1:", num1)
print("Number 2:", num2)
if different_signs:
    print("The numbers have different signs.")
else:
    print("The numbers have the same sign.")

print("STEP 5: Divide Without Using /")
dividend = 17
divisor = 5
original_dividend = dividend
quotient = 0
while dividend >= divisor:
    dividend = dividend - divisor
    quotient = quotient + 1
remainder = dividend
print("Dividend:", original_dividend)
print("Divisor:", divisor)
print("Quotient:", quotient)
print("Remainder:", remainder)
print("PROGRAM COMPLETE!")
