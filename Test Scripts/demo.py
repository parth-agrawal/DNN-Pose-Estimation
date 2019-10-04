# import sys
# sys.path.append("C:/Users/Parth/Dropbox/Research/Sahin Research/DeepLabCut/examples")

import os

import deeplabcut

path_config_file = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "DeepLabCut/examples/Reaching-Mackenzie-2018-08-30/config.yaml"))
print (path_config_file)

# load demo data and create a training set
deeplabcut.load_demo_data(path_config_file)

deeplabcut.check_labels(path_config_file)

# deeplabcut.create_training_dataset(path_config_file)
deeplabcut.train_network(path_config_file, shuffle=1, saveiters=300, displayiters=10)




deeplabcut.evaluate_network(path_config_file, plotting=True)
