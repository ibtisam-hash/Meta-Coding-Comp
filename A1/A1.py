def can_build_k_decker(T, test_cases):
    results = []
    
    for i in range(T):
        S, D, K = test_cases[i]
        total_buns = 2 * S + 2 * D
        total_patties = S + 2 * D
        total_cheese_slices = S + 2 * D
        
        if K % 2 == 0:
            # If K is even, you need an even number of buns, patties, and cheese slices.
            if total_buns >= K and total_patties >= K // 2 and total_cheese_slices >= K // 2:
                results.append("YES")
            else:
                results.append("NO")
        else:
            # If K is odd, you need an odd number of buns, patties, and cheese slices.
            if total_buns >= K and total_patties >= K // 2 and total_cheese_slices >= K // 2:
                results.append("YES")
            elif total_buns >= K + 1 and total_patties >= (K // 2) + 1 and total_cheese_slices >= (K // 2) + 1:
                results.append("YES")
            else:
                results.append("NO")
    
    return results

# Read input from a text file
with open('cheeseburger_corollary_1_input.txt', 'r') as file:
    input_lines = file.readlines()

T = int(input_lines[0])
test_cases = [list(map(int, line.split())) for line in input_lines[1:]]

# Calculate results
results = can_build_k_decker(T, test_cases)

# Write output to a text file
with open('output.txt', 'w') as file:
    for i, result in enumerate(results):
        file.write(f"Case #{i + 1}: {result}\n")
