#errors
errors = [404, 500, 404, 302, 500, 200, 404]
unique_errors = set(errors)
#print
print("Total error events:", len(errors))
print("Distinct error types:", len(unique_errors))
print("Sorted unique codes:", sorted(unique_errors))
#counting errors
for code in sorted(unique_errors):
	print(f"Code {code}: {errors.count(code)} occurrences")

