import io
import tarfile
import pandas as pd
import time


# Read in random order. Extract the list of file names and
# randomize.
start_time = time.time()
texts = []
with tarfile.open("data.tar", "r") as tar:
    filenames = [member.name for member in tar if member.name.endswith(".csv")]
    for member in filenames:
        f = tar.extractfile(member)
        texts.append(f.read().decode("utf-8"))


csv = "index,hour,activity_level\n"
csv += "\n".join([
    "\n".join(t.split("\n")[1:]) for t in texts
])
data = pd.read_csv(io.StringIO(csv))
mean = data["activity_level"].mean()


end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")
print(f"Mean: {mean}")
