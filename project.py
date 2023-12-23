import numpy as np
import matplotlib.pyplot as plt

#  1: Create a 2D numpy array
#  size of a house (in square feet) vs  cost (in thousands of dollars)

data = np.array([
    [1000, 100],
    [1500, 150],
    [2000, 200],
    [2500, 250],
    [3000, 300]
])

# 2: Extract the columns for size and cost
size = data[:, 0]
cost = data[:, 1]

# 3: Plot the data
plt.scatter(size, cost, label='Houses', color='blue')

# 4: Add labels and title
plt.xlabel('Size (sq. ft)')
plt.ylabel('Cost (thousands of dollars)')
plt.title('Size vs Cost of Houses')

#  5: Add legend
plt.legend()

# 6: Show the plot
plt.show()
