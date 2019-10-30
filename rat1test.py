import deeplabcut

from IPython import get_ipython

path_config_file= "C:/Users/parth/desktop/DNN-Pose-Estimation/Reaching-Parth-2019-10-07/config.yaml"

get_ipython().run_line_magic('matplotlib', 'tk')
# exec(%matplotlib inline)

deeplabcut.extract_frames(path_config_file)
get_ipython().run_line_magic('gui', 'wx')
deeplabcut.label_frames(path_config_file)
