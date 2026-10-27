def suvat(u, a, t):
	"""Calculate displacement and final velocity from initial velocity, acceleration, and time.

	parameters:
		u: Initial velocity in m/s.
		a: Acceleration in m/s^2.
		t: Time in seconds.

	Returns:
		A tuple containing displacement in metres and final velocity in m/s.
	"""
	s = u * t + 0.5 * a * t**2
	v = u + a * t
	return s, v


if __name__ == "__main__":
	u = float(input("Enter initial velocity (m/s): "))
	a = float(input("Enter acceleration (m/s^2): "))
	t = float(input("Enter time (s): "))

	s, v = suvat(u, a, t)
	print(f"Displacement: {s:.2f} m")
	print(f"Final velocity: {v:.2f} m/s")
