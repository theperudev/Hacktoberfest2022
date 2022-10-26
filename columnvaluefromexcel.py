import pandas as pd
import numpy as np
filename=input("Enter File Name : ")
columnname=input("Enter Column Name : ")
df = pd.read_excel(filename)[[columnname]]
print(df)
