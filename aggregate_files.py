import os
import pandas as pd
import numpy as np
import time

# iterate over folders matching data/*/*.csv
means = []

start_time = time.time()

for folder in os.listdir("data"):
    for file in os.listdir(f"data/{folder}"):
        data = pd.read_csv(f"data/{folder}/{file}")
        mean = data["activity_level"].mean()
        means.append(mean)

end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")
print(np.mean(means))
