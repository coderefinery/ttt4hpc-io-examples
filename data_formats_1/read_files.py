import time
import io
import os
import pandas as pd


# Read and get the text contents
start_time = time.time()
csv = "index,hour,activity_level\n"
for folder in os.listdir("data"):
    for file in os.listdir(f"data/{folder}"):
        with open(f"data/{folder}/{file}") as f:
            csv += '\n'.join(f.readlines()[1:])


# Turn in into a dataframe
data = pd.read_csv(io.StringIO(csv))
mean = data["activity_level"].mean()


end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")
print(f"Mean: {mean}")
