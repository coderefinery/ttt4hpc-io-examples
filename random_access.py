import io
import os
import pandas as pd
import numpy as np
import time

# iterate over files in data.zip matching data/*/*.csv
start_time = time.time()


csv = "index,hour,activity_level\n"
filenames = []
for folder in os.listdir("data"):
    for file in os.listdir(f"data/{folder}"):
        filenames.append(f"data/{folder}/{file}")

# randomize order
filenames = np.random.permutation(filenames)

for file in filenames:
    with open(file) as f:
        csv += "\n".join(f.readlines()[1:])

data = pd.read_csv(io.StringIO(csv))
mean = data["activity_level"].mean()

end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")
print(mean)
