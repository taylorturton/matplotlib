import matplotlib.pyplot as plt
import numpy as np

# Data
data = [2, 3, 2, 4, 3, 5, 7, 6, 8, 9, 10, 11, 12]

# Count the frequency of each unique value
unique_values, value_counts = np.unique(data, return_counts=True)

# Create the histogram with customizations
plt.bar(unique_values, value_counts, color='green', align='center')

# Customize the plot (optional)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Customized Histogram')

# Set the x-axis ticks and labels directly under each bin
plt.xticks(unique_values)
plt.gca().xaxis.set_major_locator(plt.MultipleLocator(1))  # Ensure tick for each bin

# Display the plot
plt.show()

# Save the plot as an image file (optional)
plt.savefig('histogram.png')
