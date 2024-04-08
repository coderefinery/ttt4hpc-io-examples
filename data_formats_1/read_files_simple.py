import time
import io
import os
import pandas as pd


# iterate over folders matching data/*/*.csv
start_time = time.time()

dfs = []
for folder in os.listdir("data"):
    for file in os.listdir(f"data/{folder}"):
        with open(f"data/{folder}/{file}") as f:
            dfs.append(pd.read_csv(f))


# Turn in into a dataframe
data = pd.concat(dfs)
mean = data["activity_level"].mean()


end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")
print(f"Mean: {mean}")
