# MOVE THE ROBOT TO KEEP THE FACE CENTERED
# get the face location as 2 pairs of (x,y) - top right, bottom left
# 720 x 1280 height, width
from Freenove_Three_Wheeled_Smart_Car_Kit_for_Raspberry_Pi_Master.Server.mDev import *

class Driver:
    centerBuffer = 50
    centerX = (1280 / 2)
    centerY = (720 / 2)
    leftCenterBound = (1280 / 2) - centerBuffer # 590
    rightCenterBound = (1280 / 2) + centerBuffer # 690
    upperCenterBound = (720 / 2) + centerBuffer # 410
    lowerCenterBound = (720 / 2) - centerBuffer # 310

    def __init__(self, target, face_recognizer):
        self.recognizer = face_recognizer
        self.target = target

    # get the location of the face from the facial recognition
    def make_movement_given_frame(self, frame):
        face_locations, face_names = self.recognizer.find_locs_given_frame(frame)
        index = face_names.index(self.target)
        coords = face_locations[index]
        top = coords[0]
        right = coords[1]
        bottom = coords[2]
        left = coords[3]

        mdev = mDEV()  # create object

        # initialize variables used to call move
        left_pwm = 0
        right_pwm = 0
        steering_angle = 0

        # change the variables depending on where the face is
        # if the face is to the right of our center bounds, move right
        if right > self.rightCenterBound:
            print("right")
            value = (right - self.centerX) / self.centerX # the difference divided by the max difference, get proportion
            steering_angle = 30 * value # needs to be positive, change on how far over the bound it is
            # mdev.move(0, 0, 30)  # Car TurnRight

        # if the face is to the left of our center bounds, move left
        if left < self.leftCenterBound:
            print("left")
            value = (self.centerX - left) / self.centerX # the difference divided by the max difference, get proportion
            steering_angle = -30 * value # needs to be negative, change on how far over the bound it is
            # mdev.move(0, 0, -30)  # Car TurnLeft

        # if the face is above our center bounds, back up
        if top > self.upperCenterBound:
            print("up")
            left_pwm = -10
            right_pwm = -10
            # mdev.move(-10,-10,0) # Car back up

        # if the face is below our center bounds, move forward
        if bottom < self.lowerCenterBound:
            print("down")
            left_pwm = 10
            right_pwm = 10
            # mdev.move(10,10,0) # Car move forward

        mdev.move(left_pwm, right_pwm, steering_angle)