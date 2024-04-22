import webdataset as wds
import glob


# List all shards
urls = glob.glob("data/*.tar")

# Create a dataset. Set it up to shuffle in batches of 100 images.
dataset = (
    wds.WebDataset(urls)
    .shuffle(100)
    .decode("rgb")
    .to_tuple("input.pyd", "output.pyd", "__key__")
)


# At this point we have not actually read the files.
# Thea are read when we actually iterate over them
for i, (image, output, key) in enumerate(dataset):
    print(image, output, key)
    
    if i == 3:
        break
