import tarfile
import os

tar = tarfile.open("data.tar", "w")

for folder in os.listdir("data"):
    for file in os.listdir(f"data/{folder}"):
        tar.add(f"data/{folder}/{file}")
        
tar.close()
