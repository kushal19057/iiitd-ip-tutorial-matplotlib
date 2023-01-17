# import libraries
import matplotlib.pyplot as plt

# data
max_temps = [20, 24, 30, 37, 40, 39, 35, 34, 34, 33, 28, 22]
min_temps = [8, 11, 16, 23, 27, 28, 28, 27, 25, 21, 14, 9]
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# plot max temp v/s month with a red color and 'x' marks
plt.plot(months, max_temps, marker='x', color='r', label='Max Temp')

# plot min temp v/s month with a blue color and 'o' marks
plt.plot(months, min_temps, marker='o', color='b', label='Min Temp')

# define plot x axis and y axis labels
plt.xlabel("Months")
plt.ylabel("Temperature (in deg. C)")

# define plot title
plt.title("Delhi min and max temperature over 12 months")

# create a legend
plt.legend()


# save image as a file
plt.savefig("plots/plot001.png")

# and show the plot as a pop up window when python file run
plt.show()