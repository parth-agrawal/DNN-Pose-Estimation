import deeplabcut
import os

path_config_file = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "DeepLabCut/examples/Reaching-Mackenzie-2018-08-30/config.yaml"))
print (path_config_file)

videofile_path = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "DeepLabCut/examples/Reaching-Mackenzie-2018-08-30/videos/mmc2.mp4"))
print(videofile_path)

print ("start Analyzing the video!")
deeplabcut.analyze_videos(path_config_file,[videofile_path], videotype=".mp4")

deeplabcut.create_labeled_video(path_config_file, [videofile_path], draw_skeleton=True)

# %matplotlib notebook

# deeplabcut.plot_trajectories(path_config_file, [videofile_path],showfigures=True)


deeplabcut.extract_outlier_frames(path_config_file, videofile_path, outlieralgorithm='uncertain',p_bound=0.2)
