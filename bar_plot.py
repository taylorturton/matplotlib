import matplotlib.pyplot as plt

# Data
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [10, 15, 7, 12]

# Create the bar plot
plt.bar(categories, values)

# Customize the plot (optional)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Simple Bar Plot')
plt.xticks(rotation=45)

# Display the plot
plt.show()

# Save the plot as an image file (optional)
plt.savefig('bar_plot.png')
