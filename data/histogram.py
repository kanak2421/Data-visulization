import matplotlib.pyplot as plt 

# draw a simple line chart showing population growth over the last 115 years
years =[1900, 1960, 1990, 2000, 2005, 2015]
medals =[5, 10, 15, 20, 25, 30]

# ploy our chat with data above
plt.plot(years, medals, color=(0/255, 100/255, 100/255), linewidth=8.0)

#label on the left hand side
plt.ylabel("Medals won by country")
# label on the bottom of the chart
plt.xlabel("Medals won in these years")

# add a title to the chart
plt.title("Total medals won by the country", pad="20")

# run the show method (this lives inside the pylot package)
# this will generate a graph in a new window
plt.show()