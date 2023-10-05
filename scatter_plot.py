import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 3, 5]

# Create the scatter plot with customizations
plt.scatter(x, y, marker='o', s=50, color='red', alpha=0.7)

# Customize the plot (optional)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Customized Scatter Plot')
plt.grid(True)

# Display the plot
plt.show()
