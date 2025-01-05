import seaborn as sns
import matplotlib.pyplot as plt

data = [7, 15, 13, 18, 19, 10, 9, 11, 30]
sns.boxplot(data=data)

plt.title('Distribution and Outliers in Data (Box Plot)')
plt.show()
