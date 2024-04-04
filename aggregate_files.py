import os
import pandas as pd
import io
import time

# iterate over folders matching data/*/*.csv
start_time = time.time()

texts = []
for folder in os.listdir("data"):
    for file in os.listdir(f"data/{folder}"):
        with open(f"data/{folder}/{file}") as f:
            texts.append(f.read())

end_time = time.time()
print(f"Time taken reading files: {end_time - start_time} seconds")


data = pd.concat([pd.read_csv(io.StringIO(text)) for text in texts])
mean = data["activity_level"].mean()

end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")
print(mean)
