import csv as csv
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

csv_file = csv.reader(open('../train.csv', 'rb'))
header = csv_file.next()

data = []

for row in csv_file:
    data.append(row)

df = pd.DataFrame(data)


print df[:5]
