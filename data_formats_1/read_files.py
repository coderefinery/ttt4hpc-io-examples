import time
import io
import os
import pandas as pd


# Read and get the text contents
start_time = time.time()
texts = []
for folder in os.listdir("data"):
    for file in os.listdir(f"data/{folder}"):
        with open(f"data/{folder}/{file}") as f:
            texts.append(f.read())


# Turn in into a dataframe
csv = "index,hour,activity_level\n"
csv += "\n".join([
    "\n".join(t.split("\n")[1:]) for t in texts
])
data = pd.read_csv(io.StringIO(csv))
mean = data["activity_level"].mean()


end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")
print(f"Mean: {mean}")
