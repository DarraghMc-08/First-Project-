"""Calculate a number's cube root without using math functions."""

# Ask the user for a number, convert the typed text to a floating-point value,
# and store it in x.
x = float(input("Enter a number: "))
# Use one third of x as the initial estimate of its cube root.
guess = x / 3

# != means "not equal": only run the calculation when x is not zero.
# In !=, ! is the logical NOT symbol, so != means NOT equal.
if x != 0:
	# Start counting the iterations of the estimate-improvement loop.
	iterations = 0
	# Repeat until the new estimate is sufficiently close to the previous one.
	while True:
		# Count this pass through the loop.
		iterations += 1
		# Apply Newton's method to get a better estimate of the cube root.
		new_guess = (2 * guess + x / (guess ** 2)) / 3
		# Stop when the change between estimates is less than one millionth.
		if abs(new_guess - guess) < 1e-6:
			# Keep the improved estimate before leaving the loop.
			guess = new_guess
			break
		# Otherwise, use this estimate as the starting point for the next pass.
		guess = new_guess

# Display the calculated cube root.
print("Cube root:", guess)
# Display the iteration count; use zero when x is zero and the loop was skipped.
print("Number of iterations:", iterations if x != 0 else 0)
