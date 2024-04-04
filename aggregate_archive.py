import time
import io
import os
import tarfile
import pandas as pd

# iterate over files in data.zip matching data/*/*.csv
start_time = time.time()

csv = "index,hour,activity_level\n"
with tarfile.open("data.tar") as tar:
    for member in tar:
        if member.name.endswith(".csv"):
            f = tar.extractfile(member)
            f = io.TextIOWrapper(f)
            csv += "\n".join(f.readlines()[1:])

end_time = time.time()
print(f"Time taken reading files: {end_time - start_time} seconds")


data = pd.read_csv(io.StringIO(csv))
mean = data["activity_level"].mean()


end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")
print(mean)
