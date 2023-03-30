import csv
import numpy as np
import matplotlib.pyplot as plt

# Open the CSV file
with open('data2.csv', 'r') as csv_file:
    # Read the CSV file using a CSV reader
    csv_reader = csv.reader(csv_file)

    # Create empty lists to store the values
    y_values = []

    # Read the values from the CSV file and append them to the lists
    for row in csv_reader:
        # y_values.append(float(row[0]))
        y_values = row
        for i in range(len(y_values)):
            y_values[i] = float(y_values[i])

        #y_values.append(float(row[1]))

    x_values = np.arange(len(y_values))

    big = max(y_values)
    for i in range(len(y_values)):
        y_values[i] = float(y_values[i])/big


# Plot the values using matplotlib
plt.plot(x_values, y_values)

# Set the title and axis labels
plt.title('Plot (Clap)')
plt.xlabel('Samples')
plt.ylabel('Data')

# Show the plot
plt.show()
