import matplotlib.pyplot as plt
import numpy as np

# Data
data1 = [2, 3, 2, 4, 3, 5, 7, 6, 8, 9, 10, 11, 12]
data2 = [1, 2, 3, 4, 4, 5, 5, 6, 7, 8, 8, 9, 10]

# Create a figure with multiple subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))  # 1 row, 2 columns

# Plot on the first subplot
unique_values1, value_counts1 = np.unique(data1, return_counts=True)
ax1.bar(unique_values1, value_counts1, color='green', align='center')
ax1.set_xlabel('Value')
ax1.set_ylabel('Frequency')
ax1.set_title('Histogram 1')
ax1.set_xticks(unique_values1)  # Set x-axis ticks to unique values
ax1.set_xticklabels(unique_values1)  # Set x-axis tick labels to unique values

# Plot on the second subplot
unique_values2, value_counts2 = np.unique(data2, return_counts=True)
ax2.bar(unique_values2, value_counts2, color='blue', align='center')
ax2.set_xlabel('Value')
ax2.set_ylabel('Frequency')
ax2.set_title('Histogram 2')
ax2.set_xticks(unique_values2)  # Set x-axis ticks to unique values
ax2.set_xticklabels(unique_values2)  # Set x-axis tick labels to unique values

# Adjust spacing between subplots
plt.tight_layout()

# Display the figure with subplots
plt.show()

# Save the figure as an image file (optional)
plt.savefig('multiple_subplots.png')
