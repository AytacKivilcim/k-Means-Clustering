# Aytaç Kıvılcım 041504008 k-Means Clustering
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import random
import math

label_number = 8
# data1.txt
# data2.txt
# data3.txt
data = open("data3.txt", "r")

x_axis = []
y_axis = []
cluster_centers_x = []
cluster_centers_y = []

# gathering all the x_axis and y_axis information from the data.txt
for line in data:
    splitedLine = line.split(",")
    x_axis.append(float(splitedLine[0]))
    y_axis.append(float(splitedLine[1]))

max_x = max(x_axis)
min_x = min(x_axis)
max_y = max(y_axis)
min_y = min(y_axis)

# plotting core data
plt.figure(figsize=(6, 6))
plt.title('Data')
plt.scatter(x_axis, y_axis, c='brown', s=1.5)
plt.xlabel('x_axis')
plt.ylabel('y_axis')
plt.show()
plt.close()

colors = ['red', 'green', 'blue', 'purple', 'orange', 'violet', 'aqua', 'grey']
label_colors = []
label_count = 0

# creating label colors according to label_number
while label_count < label_number:
    label_colors.append(colors[label_count])
    label_count += 1

# create random initial cluster_centers
for i in range(label_number):
    cluster_centers_x.append(random.uniform(min_x, max_x))
    cluster_centers_y.append(random.uniform(min_y, max_y))

min_change_in_cluster_centers = 10000
iterations = 0
objective_function = []
# while goes until there is less than 0.0001 change in cluster centers
while min_change_in_cluster_centers > 0.0001:
    iterations += 1
    # assigning labels to the closest cluster center
    labels = []
    for i in range(len(x_axis)):
        min_distance = math.sqrt(math.pow((max_x - min_x), 2) + math.pow((max_y - min_y), 2))
        label = -1
        for j in range(len(cluster_centers_x)):
            distance = math.sqrt(
                math.pow((cluster_centers_x[j] - x_axis[i]), 2) + math.pow((cluster_centers_y[j] - y_axis[i]), 2))
            if min_distance > distance:
                min_distance = distance
                label = j
        labels.append(label)

    # before the iterations plot the data with initial random cluster centers
    if iterations == 1:
        plt.figure(figsize=(6, 6))
        plt.title('Random cluster centers')
        plt.scatter(x_axis, y_axis, c=labels, cmap=matplotlib.colors.ListedColormap(label_colors), s=1.5)
        plt.scatter(cluster_centers_x, cluster_centers_y, c='black')
        plt.xlabel('x_axis')
        plt.ylabel('y_axis')
        plt.show()
        plt.close()

    # recalculate cluster_centers coordinates
    for i in range(len(cluster_centers_x)):
        x_sum = 0
        y_sum = 0
        point_count = 0
        for j in range(len(x_axis)):
            if labels[j] == i:
                point_count += 1
                x_sum += x_axis[j]
                y_sum += y_axis[j]
        if point_count != 0:
            average_x = x_sum / point_count
            average_y = y_sum / point_count
            change = math.sqrt(
                math.pow((cluster_centers_x[i] - average_x), 2) + math.pow((cluster_centers_y[i] - average_y), 2))
            if change < min_change_in_cluster_centers:
                min_change_in_cluster_centers = change
            cluster_centers_x[i] = average_x
            cluster_centers_y[i] = average_y
    # plotting all the iterations

    plt.figure(figsize=(6, 6))
    title_name = str(iterations) + ". iteration"
    plt.title(title_name)
    plt.scatter(x_axis, y_axis, c=labels, cmap=matplotlib.colors.ListedColormap(label_colors), s=1.5)
    plt.scatter(cluster_centers_x, cluster_centers_y, c='black')
    plt.xlabel('x_axis')
    plt.ylabel('y_axis')
    plt.show()
    plt.close()

    # calculate Objective function value
    objective_function_sum = 0
    for i in range(len(x_axis)):
        distance_from_cluster_center = math.sqrt(math.pow((cluster_centers_x[labels[i]] - x_axis[i]), 2) + math.pow((cluster_centers_y[labels[i]] - y_axis[i]), 2))
        objective_function_sum += distance_from_cluster_center
    objective_function.append(objective_function_sum)

plt.figure(figsize=(6, 6))
title_name = str(iterations) + ". iteration\nFunction Value is " + str(objective_function_sum)
plt.title(title_name)
plt.scatter(x_axis, y_axis, c=labels, cmap=matplotlib.colors.ListedColormap(label_colors), s=1.5)
plt.scatter(cluster_centers_x, cluster_centers_y, c='black')
plt.xlabel('x_axis')
plt.ylabel('y_axis')
plt.show()
plt.close()

x_axis = []
for i in range(iterations):
    print("For iteration {} objective function value is {}".format(i+1, objective_function[i]))
    x_axis.append(i+1)

plt.title('Objective Function')
plt.plot(x_axis, objective_function)
plt.xlabel('Iterations')
plt.ylabel('Funtion Value')
plt.show()
plt.close()