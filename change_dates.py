from __future__ import print_function
import csv
from datetime import datetime

with open('orcl-2000.csv', 'r') as f:
    for line in f.readlines():
        if line != "" and not line.startswith("Date"):
            line = line.split(",")
            new_line = ''

            for l in line:
                if l == 'Date':
                    continue

                if new_line == '':
                    date = l.split("-")
                    if int(date[0]) < 10:
                        new_line = '2000-' + date[1] + '-0' + date[0]
                    else:
                        new_line = '2000-' + date[1] + '-' + date[0]
                else:
                    new_line = new_line + "," + l

            print(new_line, end='')