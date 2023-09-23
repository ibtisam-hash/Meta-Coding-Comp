def largest_k_decker(T, test_cases):
    results = []

    for i in range(T):
        A, B, C = test_cases[i]

        # Use binary search to find the largest possible K
        left = 1
        right = C // A  # Initial upper bound based on spending all on single cheeseburgers
        while left <= right:
            mid = (left + right) // 2
            cost = mid * A + ((mid + 1) // 2) * B  # Calculate cost for mid K-decker cheeseburgers

            if cost <= C:
                left = mid + 1
            else:
                right = mid - 1

        # Subtract 1 to get the largest possible K
        largest_k = left - 1

        results.append(largest_k)

    return results

# Read input from a text file
with open('E:\GIT\Meta Coding Comp\Meta-Coding-Comp\A2\cheeseburger_corollary_2_validation_input.txt', 'r') as file:
    input_lines = file.readlines()

T = int(input_lines[0])
test_cases = [list(map(int, line.split())) for line in input_lines[1:]]

# Calculate results
results = largest_k_decker(T, test_cases)

# Write output to a text file
with open('E:\GIT\Meta Coding Comp\Meta-Coding-Comp\A2\output.txt', 'w') as file:
    for i, result in enumerate(results):
        file.write(f"Case #{i + 1}: {result}\n")
