import webdataset as wds
from itertools import islice
import glob


urls = glob.glob(
    "/scratch/shareddata/dldata/imagenet/ILSVRC2012_img_train/*.tar"
)


dataset = (
    wds.WebDataset(urls)
    .shuffle(100)
    .decode("rgb")
    .to_tuple("jpeg;jpg;png", "__key__")
)

for image, key in islice(dataset, 0, 3):
    print(image.shape, key)