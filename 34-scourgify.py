import sys
import csv
import pandas as pd

try:
    if len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    if not sys.argv[2].endswith(".csv"):
        print("Invalid output file")
        sys.exit(1)
    if sys.argv[1] != "before.csv":
        print(f"Could not read {sys.argv[1]}")
        sys.exit(1)
    else:    
        with open(f"{sys.argv[1]}") as file:
            reader = csv.DictReader(file)
            df = pd.DataFrame(reader)
            df[['first', 'second']] = df["name"].apply(lambda x: pd.Series(str(x).split(", ")))
            df.pop("name")
            df = df[['first', 'second', 'house']]
            df.to_csv(f'{sys.argv[2]}', index=False)
            print(df)
        
    
except FileNotFoundError:
    sys.exit("File Not Found")

