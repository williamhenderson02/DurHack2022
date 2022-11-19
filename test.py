import csv

header = ['Time', 'Price']
data = [
    [0.0, 2874800.0],
    [1.0, 23817410.0],
    [2, 199000.0],
    [3, 468000.0],
    [4, 1246700.0]
]

with open('scatter.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(data)