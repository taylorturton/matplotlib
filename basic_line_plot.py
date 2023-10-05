import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create the plot with a red line
plt.plot(x, y, color='red')  # You can also use color='r'

# Customize the plot (optional)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Red Line Plot')
plt.grid(True)

# Display the plot
plt.show()
