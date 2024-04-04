import os
import zipfile
import pandas as pd
import numpy as np
import time

# iterate over files in data.zip matching data/*/*.csv
means = []

start_time = time.time()

with zipfile.ZipFile("data.zip") as z:
    files = [f for f in z.namelist() if f.endswith(".csv")]
    files = np.random.permutation(files)
    for filename in files:
        data = pd.read_csv(z.open(filename))
        mean = data["activity_level"].mean()
        means.append(mean)

end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")
print(np.mean(means))
