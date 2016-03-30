"""
Simple demo of a horizontal bar chart.
"""
import matplotlib.pyplot as plt

plt.rcdefaults()
import matplotlib.pyplot as plt


people = ('1-10', '11-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80', '81-90', '91-100')
y_pos = range(1, 11)

print(y_pos)
data = [2, 3, 4, 1, 9, 10, 20, 11, 20, 20]

plt.barh(y_pos, data, align='center', alpha=0.9)
plt.yticks(y_pos, people)
plt.xlabel('Performance')
plt.title('How fast do you want to go today?')

plt.show()

d = {1: 2, 3: 4}
# print(3 in d)