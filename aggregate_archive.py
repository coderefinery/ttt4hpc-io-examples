import os
import tarfile
import pandas as pd
import numpy as np
import time
import io

# iterate over files in data.zip matching data/*/*.csv
start_time = time.time()

dfs = []
with tarfile.open("data.tar") as tar:
    for member in tar:
        if member.name.endswith(".csv"):
            f = tar.extractfile(member)
            content = io.BytesIO(f.read())
            dfs.append(pd.read_csv(content))
            
data = pd.concat(dfs)
mean = data["activity_level"].mean()


end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")
print(mean)
