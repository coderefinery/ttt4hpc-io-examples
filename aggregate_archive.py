import time
import io
import os
import tarfile
import pandas as pd

# iterate over files in data.zip matching data/*/*.csv
start_time = time.time()

# Read the tar file into memory
with open("data.tar", "rb") as tar:
    content = tar.read()

end_time = time.time()
print(f"Time taken reading to memory: {end_time - start_time} seconds")

# Now process
csv = "index,hour,activity_level\n"
with tarfile.open(fileobj=io.BytesIO(content)) as tar:
    for member in tar:
        if member.name.endswith(".csv"):
            f = tar.extractfile(member)
            f = io.TextIOWrapper(f)
            csv += "\n".join(f.readlines()[1:])

data = pd.read_csv(io.StringIO(csv))
mean = data["activity_level"].mean()

end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")
print(mean)
