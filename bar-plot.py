import matplotlib.pyplot as plt

# define data
player_names = ["Kylian Mbappe", "Lionel Messi", "Julian Alvarez", "Olivier Giroud", "Goncalo Ramos"]
goals = [8, 7, 4, 4, 3]

# create bar plot
plt.bar(player_names, goals)

# rotate text for better visual
plt.xticks(rotation=15)

# define plot x axis and y axis labels
plt.xlabel("player names")
plt.ylabel("number of goals scored")

# # define plot title
plt.title("Goals scored by players in FIFA world cup")

# # save image as a file
plt.savefig("plots/plot003.png")

# and show the plot as a pop up window when python file run
plt.show()

