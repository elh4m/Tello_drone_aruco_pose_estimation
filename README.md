# Tello_drone_aruco_pose_estimation
this repository contains all requirements to perform aruco marker detection and pose estimation (estimate the position of the camera with respect to the marker)

# How it works

1.connect tello wifi to you computer and run the file data_generation_tello_camera.py for easily taking as many pictures as you want (in this case from a checkerboard) by just pressing "c" and exit the programe by pressing "Esc".you just need to give a path for the images to be saved and there you are,all the pictures in one place


2.run the file calibration.py with the path of checkerboard images (i got this file from https://github.com/GSNCodes/ArUCo-Markers-Pose-Estimation-Generation-Python where you can find all the information for camera pose estimation)  , this gives you two .npy files namely calibration_matrix.npy and distortion_coefficients.npy (you can change the .npy files as you prefer),notice that in this step you do not need to connect the tello to the wifi

3.connect your tello and run aruco_detection_live.py for detecting markers

4.open those two .npy files and copy their values inside the file aruco_pose_estimation.py in front of intrisic_camera and distortion variables respectively,around line 100 ,like below 

intrinsic_camera = np.array(([[ 897.27955019,  0.00000000,  483.55665412],
 [ 0.00000000,  896.26488347,  343.89480185],
 [ 0.00000000,  0.00000000,  1.00000000]]))
distortion = np.array(([ -0.02182483,  -0.13931554,  0.00126883,  -0.00275032,  0.50072274]))


5.this work is part of my thesis project in the university of Genova,Italy 
I used 4 Dji Tello drone namely A,B,C,D for detection and pose estimation ,you can refer to calib_images_drone A for image references 


6.feel free to report any problem and contact me

elhmohamadii@gmail.com



