# # of biathlon sport: 3
# # of bobsleigh sport: 22
# # of curling sport: 50
# # of ice hockey sport: 351
# # of skating sport: 159
# # of skiing sport: 40
import matplotlib.pyplot as plt

values = values = [3, 22, 50, 351, 159, 40]
labels = ["biathlon sport", "bobsleigh sport", "curling sport", "ice hockey sport", "skating sport", "skiing sport"]
colors = ["pink", "grey", "gold", "skyblue", "orange", "red"]
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1)

plt.pie(values, labels=labels, colors=colors, explode=explode)
plt.show()