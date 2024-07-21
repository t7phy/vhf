import yaml
import numpy as np


with open('benchmarks/240721/res_0_0.yaml', 'r') as file:
    data = yaml.load(file, Loader=yaml.FullLoader)

print(np.array(data[(1, 1)]).shape)