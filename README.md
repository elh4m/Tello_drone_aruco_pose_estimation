# Tello_drone_aruco_pose_estimation
this repository contains all requirements to perform aruco marker detection and pose estimation (estimate the position of the camera with respect to the marker)

# How it works

1.calibrate your camera with the calibration.py file (i got this file from https://github.com/GSNCodes/ArUCo-Markers-Pose-Estimation-Generation-Python where you can find all the information for camera pose estimation)  , this file gives you two .npy files namely calibration_matrix.npy and distortion_coefficients.npy at the end

2.detect markers using aruco_detection_live.py

3.open those two .npy files and copy their values inside the file aruco_pose_estimation.py in front of intrisic_camera and distortion variables respectively,around line 100 ,like below 

intrinsic_camera = np.array(([[ 897.27955019,  0.00000000,  483.55665412],
 [ 0.00000000,  896.26488347,  343.89480185],
 [ 0.00000000,  0.00000000,  1.00000000]]))
distortion = np.array(([ -0.02182483,  -0.13931554,  0.00126883,  -0.00275032,  0.50072274]))

4.you did it!


5.feel free to report any problem and contact me

elhmohamadii@gmail.com



