import os
import zipfile
import pandas as pd
import numpy as np
import time

# iterate over files in data.zip matching data/*/*.csv
start_time = time.time()

dfs = []
with zipfile.ZipFile("data.zip") as z:
    files = [f for f in z.namelist() if f.endswith(".csv")]
    files = np.random.permutation(files)
    for filename in files:
        dfs.append(pd.read_csv(z.open(filename)))

data = pd.concat(dfs)
mean = data["activity_level"].mean()

end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")
print(mean)
