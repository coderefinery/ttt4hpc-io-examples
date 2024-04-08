import io
import tarfile
import pandas as pd
import time


# Read in random order. Extract the list of file names and
# randomize.
start_time = time.time()
csv = "index,hour,activity_level\n"
with tarfile.open("data.tar", "r") as tar:
    filenames = [member.name for member in tar if member.name.endswith(".csv")]
    for member in filenames:
        f = tar.extractfile(member)
        lines = f.read().decode("utf-8").split("\n")
        csv += "\n".join(lines[1:])


data = pd.read_csv(io.StringIO(csv))
mean = data["activity_level"].mean()


end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")
print(f"Mean: {mean}")
