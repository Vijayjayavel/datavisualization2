import csv

from datetime import datetime

import matplotlib.pyplot as plt

filename='chennai.csv'

with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    print(header_row)

    for index,column_header in enumerate(header_row):
        print(index,column_header)

    highs=[]
    dates=[]
    lows=[]
    for row in reader:
        high=float(row[2])
        high=round(high)
        highs.append(high)

        current_date=datetime.strptime(row[1],"%Y-%m-%d")
        dates.append(current_date)

        low=float(row[3])
        low=round(low)
        lows.append(low)

    #plotting
    plt.figure(figsize=(10,6))
    plt.plot(dates,highs,c='red',alpha=0.9)
    plt.plot(dates,lows,c='blue',alpha=0.9)

    plt.xticks(rotation=45) # rotating x axis label
    plt.title('temperature of chennai in june 2023')
    plt.xlabel('',fontsize=15)
    plt.ylabel('temperature(C)',fontsize=15)

    plt.fill_between(dates,highs,lows,facecolor='maroon',alpha=0.3)


    plt.ylim(25,41) # limiting scale in y axis

    plt.savefig('chennai_june23.png')
    plt.show()