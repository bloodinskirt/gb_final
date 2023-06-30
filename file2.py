import matplotlib.pyplot as plt

grouped_data = df.groupby(['height_group', 'flipper_length_mm']).size().unstack()

grouped_data.plot(kind='bar', stacked=True)

plt.xlabel('flipper_length_mm')
plt.ylabel('Count')
plt.title('Histogram of flipper_length_mm by height_group')

plt.show()

