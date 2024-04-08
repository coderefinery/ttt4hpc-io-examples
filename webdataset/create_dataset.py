import webdataset as wds
from tqdm import tqdm
import torchvision
import sys

dataset = torchvision.datasets.MNIST(root="/tmp", download=True)

tarred_dataset = wds.ShardWriter("mnist_%d.tar")
for index, (input, output) in enumerate(tqdm(dataset)):
    tarred_dataset.write({
        "__key__": "sample%06d" % index,
        "input.pyd": input,
        "output.pyd": output,
    })
tarred_dataset.close()
