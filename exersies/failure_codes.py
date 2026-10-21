# failure-codes: labels this section of the program.
run1 = [101, 102, 404, 500, 404, 101]  # Stores the failure codes from the first run.
run2 = [102, 303, 404, 500, 500, 102]  # Stores the failure codes from the second run.

unique_codes = set(run1 + run2)  # Combines both lists and removes duplicate codes.
print("Total number of unique codes:", len(unique_codes))  # Displays how many different codes were found.
print("Unique codes:", unique_codes)  # Displays the set of different codes.

run1_counts = {code: run1.count(code) for code in set(run1)}  # Counts each distinct code in the first run.
print("Run 1 distinct codes and counts:", run1_counts)  # Displays each Run 1 code and its count.

