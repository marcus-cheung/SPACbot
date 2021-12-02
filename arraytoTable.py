import csv

def makeTable2(table):
    # make table of raw data
    with open("spacdata.csv", "w", newline="") as file:
        writer = csv.writer(file)
        for x in table:
            writer.writerow(
                [
                    x[0],
                    x[22],
                    x[23]
                ]
            )
table = []