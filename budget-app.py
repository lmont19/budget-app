import csv
import re
import sys

statement = sys.argv[1]

with open(statement) as csv_file:
    total_spent = 0
    money_in = 0
    file = csv.reader(csv_file)
    for row in file:
        if row:
            dollars = row[6]
            if re.match(r'-{2}', dollars):
                money_in += float(dollars.replace("--", ""))
            else:
                total_spent += float(dollars.replace("-", ""))
                #print(dollars)

    print("This month you made: $" + str(money_in))
    print("This month you spent: $" + str(total_spent))
        
