import deeplabcut

task = 'Reaching'
experimenter = 'Parth'

video = ["c:/users/parth/desktop/dnn-pose-estimation/Videos/rat1.mp4"]
path_config_file=deeplabcut.create_new_project(task,experimenter,video, working_directory='C:/Users/parth/Desktop/DNN-Pose-Estimation',copy_videos=False)
