# MOVE THE ROBOT TO KEEP THE FACE CENTERED
# get the face location as 2 pairs of (x,y) - top right, bottom left
# 720 x 1280 height, width
from Freenove_Three_Wheeled_Smart_Car_Kit_for_Raspberry_Pi_Master.Server.mDev import *


class Driver:
    centerBuffer = 50
    centerX = (1280 / 2)
    centerY = (720 / 2)
    leftCenterBound = (1280 / 2) - centerBuffer  # 590
    rightCenterBound = (1280 / 2) + centerBuffer  # 690
    upperCenterBound = (720 / 2) + centerBuffer  # 410
    lowerCenterBound = (720 / 2) - centerBuffer  # 310
    goal_x = 100
    goal_y = 100
    goal_tolerance = 10

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
        center_y = (top + bottom) / 2
        center_x = (right + left) / 2
        span_y = abs(top - bottom)
        span_x = abs(right - left)

        mdev = mDEV()  # create object

        # initialize variables used to call move
        left_pwm = 0
        right_pwm = 0
        steering_angle = 0

        # change the variables depending on where the face is
        # if the face is to the right of our center bounds, move right
        if center_x > self.rightCenterBound + self.goal_tolerance:
            print("right")
            value = (
                                center_x - self.centerX) / self.centerX  # the difference divided by the max difference, get proportion
            steering_angle = 30 * value  # needs to be positive, change on how far over the bound it is
            # mdev.move(0, 0, 30)  # Car TurnRight

        # if the face is to the left of our center bounds, move left
        if center_x < self.leftCenterBound - self.goal_tolerance:
            print("left")
            value = (
                                self.centerX - center_x) / self.centerX  # the difference divided by the max difference, get proportion
            steering_angle = -30 * value  # needs to be negative, change on how far over the bound it is
            # mdev.move(0, 0, -30)  # Car TurnLeft

        # if were too small (if either are not less than, we're not too small), move forward
        if span_x < self.goal_x - self.goal_tolerance and span_y < self.goal_y - self.goal_tolerance:
            print("too small")
            left_pwm = abs(left_pwm)
            right_pwm = abs(right_pwm)

        if span_x > self.goal_x + self.goal_tolerance and span_y > self.goal_y + self.goal_tolerance:
            print("too big")
            left_pwm = abs(left_pwm) * -1
            right_pwm = abs(right_pwm) * -1

        # if the face is above our center bounds, tilt camera up
        if center_y > self.upperCenterBound + self.goal_tolerance:
            print("up")
            # ????
            # mdev.move(-10,-10,0) # Car back up

        # if the face is below our center bounds, tilt camera down
        if center_y < self.lowerCenterBound - self.goal_tolerance:
            print("down")
            # ????
            # mdev.move(10,10,0) # Car move forward

        mdev.move(left_pwm, right_pwm, steering_angle)
