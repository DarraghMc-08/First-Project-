"""Calculate a number's cube root without using math functions."""

x = float(input("Enter a number: "))
guess = x / 3

if x != 0:
	iterations = 0
	while True:
		iterations += 1
		new_guess = (2 * guess + x / (guess ** 2)) / 3
		if abs(new_guess - guess) < 1e-6:
			guess = new_guess
			break
		guess = new_guess

print("Cube root:", guess)
print("Number of iterations:", iterations if x != 0 else 0)
