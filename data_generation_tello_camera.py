
#this code takes picture when the user press "c"
'''
i use this file for taking pictures from drone camera by pressing c ,not only for calibration purposes
path = "/home/elham/thesis/drone_project_thesis/camera_calibration_packages/ArUCo-Markers-Pose-Estimation-Generation-Python/detection_droneA/ "

'''

import os
import cv2
from djitellopy import Tello


tello = Tello()
tello.connect()
tello.streamon()
# print(f"the height is :{tello.get_height()}")
frame_read = tello.get_frame_read()
path = "/home/elham/thesis/drone_project_thesis/camera_calibration_packages/ArUCo-Markers-Pose-Estimation-Generation-Python/detect_droneD/ "
print(tello.get_battery())

count=0
frame = frame_read.frame
# Define a function to take a picture
def take_picture():
    
    # Capture a frame from the Tello camera
    frame = frame_read.frame

    # Save the frame 
    cv2.imwrite(name, frame)
    print(f"Image saved as {name}")



counter=0
# Loop for reading frames
while True:
    name = path + str(counter)+".jpg"
    name=os.path.join(os.path.expanduser('~'),name)
    # Read a frame from the Tello camera
    frame = frame_read.frame

    # Display the frame
    cv2.imshow("Tello", frame)
    k = cv2.waitKey(10)
    # Check for the "c" key
    
    if k==99:
        #print(k)
        take_picture()
        counter+=1

    # Check for the ESC key
    elif k==27:
        break


