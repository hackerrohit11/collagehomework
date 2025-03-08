def min_starting_energy(nums):
    current_energy = 0
    min_energy = float('inf')

    for energy in nums:
        current_energy += energy
        min_energy = min(min_energy, current_energy)

    # Minimum starting energy required
    if min_energy < 1:
        return 1 - min_energy
    else:
        return 1

# Test cases
print(min_starting_energy([-3, 2, -3, 4, 2]))  # Output: 5
print(min_starting_energy([1, 2]))              # Output: 1
