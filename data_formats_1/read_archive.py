import time
import io
import os
import tarfile
import pandas as pd


# Read sequantially. The "r|" sets tar reading mode to
# streaming
start_time = time.time()
csv = "index,hour,activity_level\n"
with tarfile.open("data.tar", "r|") as tar:
    for member in tar:
        if member.name.endswith(".csv"):
            f = tar.extractfile(member)
            lines = f.read().decode("utf-8").split("\n")
            csv += "\n".join(lines[1:])


data = pd.read_csv(io.StringIO(csv))
mean = data["activity_level"].mean()


end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")
print(f"Mean: {mean}")
