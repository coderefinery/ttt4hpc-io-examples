import os
import pandas as pd
import numpy as np
import time

# iterate over folders matching data/*/*.csv
start_time = time.time()

dfs = []
for folder in os.listdir("data"):
    for file in os.listdir(f"data/{folder}"):
        dfs.append(pd.read_csv(f"data/{folder}/{file}"))

data = pd.concat(dfs)
mean = data["activity_level"].mean()

end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")
print(mean)
