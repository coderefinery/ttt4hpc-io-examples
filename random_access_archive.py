import io
import tarfile
import pandas as pd
import numpy as np
import time

# iterate over files in data.zip matching data/*/*.csv
start_time = time.time()

texts = []
with tarfile.open("data.tar") as tar:
    filenames = [member.name for member in tar if member.name.endswith(".csv")]
    # randomize order
    filenames = np.random.permutation(filenames)
    for member in filenames:
        f = tar.extractfile(member)
        texts.append(f.read())

end_time = time.time()
print(f"Time taken reading files: {end_time - start_time} seconds")


data = pd.concat([pd.read_csv(io.BytesIO(text)) for text in texts])
mean = data["activity_level"].mean()


end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")
print(mean)
