# import libraries
import matplotlib.pyplot as plt
import random

# create some dummy data
xs = list(range(1, 25))
ys = [round(x + random.uniform(0, 4), 2) for x in xs]

# # plot max temp v/s month with a red color and 'x' marks
plt.scatter(xs, ys, marker='x', color='r')

# define plot x axis and y axis labels
plt.xlabel("X")
plt.ylabel("Y")

# # define plot title
plt.title("Scatter Plot of data points")

# # save image as a file
plt.savefig("plots/plot002.png")

# # and show the plot as a pop up window when python file run
plt.show()