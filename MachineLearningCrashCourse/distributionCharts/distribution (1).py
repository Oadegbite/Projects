#!/home/tomi/anaconda3/bin/python3
import csv
import matplotlib.pyplot as plt

def makeGraph(file,col):
    values = []
    fileName = file
    # Fixing random state for reproducibility
    with open(fileName+'.csv', 'r', newline='') as csvfile:
        askreader = csv.reader(csvfile, delimiter=',', lineterminator='\n')

        for rows in askreader:
            values.append(rows[col]) # from cols 11-20 are the values from the API

    title = values[0]
    print(title)
    values = [float(i) for i in values[1:]] #converting values from string to floats for the chart

    #bins = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1] #bins to sort numbers into based on values they fall between

    # the histogram of the data
    plt.hist(values,rwidth=0.6)
    plt.xlabel('Values')
    plt.ylabel('Count')
    plt.title('{} Distribution of {}'.format(fileName, title))
    plt.grid(True)
    plt.savefig('{} {} Distribution.png'.format(fileName,title))
    plt.clf() #clear the current graph, can be removed to see all values on one chart
    print("Done")

for i in range(0,10): #from the start col values in the dataset 9 catagories + 1 extra for the loop termination
    makeGraph('california_housing_train',i)
