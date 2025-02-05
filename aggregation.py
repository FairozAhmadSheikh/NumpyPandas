import numpy as np

# Create two arrays
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

# Aggregation operations
sum_array = arr1 + arr2  # Element-wise sum
mean_value = np.mean([arr1, arr2])  # Overall mean
min_value = np.min([arr1, arr2])  # Overall min
max_value = np.max([arr1, arr2])  # Overall max

# Print results
print("Sum:", sum_array)
print("Mean:", mean_value)
print("Min:", min_value)
print("Max:", max_value)
