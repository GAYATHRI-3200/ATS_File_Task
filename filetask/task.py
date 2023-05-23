import os
import pandas as pd

df = pd.DataFrame()

for f in os.listdir(os.getcwd()):
    if f.endswith('.csv'):
        try:
            data = pd.read_csv(f, encoding='latin1')
            df = df.append(data)
        except pd.errors.ParserError as e:
            print(f"Error parsing file: {f} - {e}")

df.to_csv('mergedfile.csv', index=False)
