import io
import tarfile
import pandas as pd
import numpy as np
import time

# iterate over files in data.zip matching data/*/*.csv
start_time = time.time()

# Read the tar file into memory
with open("data.tar", "rb") as tar:
    content = tar.read()

# Now process
csvs = []
with tarfile.open(fileobj=io.BytesIO(content)) as tar:
    
    
    for i, member in enumerate(tar):
        if i % 10 == 0:
            csv = "index,hour,activity_level\n"

        if member.name.endswith(".csv"):
            f = tar.extractfile(member)
            f = io.TextIOWrapper(f)
            csv += "\n".join(f.readlines()[1:])
        
        if i % 10 == 9:
            csvs.append(csv)

dfs = [pd.read_csv(io.StringIO(csv)) for csv in csvs]
data = pd.concat(dfs)
mean = data["activity_level"].mean()

end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")
print(mean)
