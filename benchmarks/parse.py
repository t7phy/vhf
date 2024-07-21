import yaml
import numpy as np


# Open the YAML file
with open('benchmarks/240721/res_0_0.yaml', 'r') as file:
    # Load the file content into a dictionary
    data = yaml.load(file, Loader=yaml.FullLoader)

# Now, 'data' is a dictionary containing the YAML file content
print(np.array(data[(-5, -5)]).shape)