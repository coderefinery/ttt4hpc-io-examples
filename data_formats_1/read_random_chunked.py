import io
import tarfile
import pandas as pd
import numpy as np
import time

streaming_mode = True

if streaming_mode:
    mode = "r|"
else:
    mode = "r"


# Read sequantially. The "r|" sets tar reading mode to
# streaming
start_time = time.time()
texts = []
with tarfile.open("data.tar", mode) as tar:
    for i, member in enumerate(tar):
        if member.name.endswith(".csv"):
            if i%10 == 0:
                chunk = []
        
            f = tar.extractfile(member)
            chunk.append(f.read().decode("utf-8"))
        
            if i%10 == 9:
                chunk = np.random.permutation(chunk)
                texts += list(chunk)


csv = "index,hour,activity_level\n"
csv += "\n".join([
    "\n".join(t.split("\n")[1:]) for t in texts
])
data = pd.read_csv(io.StringIO(csv))
mean = data["activity_level"].mean()


end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")
print(f"Mean: {mean}")