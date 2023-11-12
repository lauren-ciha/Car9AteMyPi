# MOVE THE ROBOT TO KEEP THE FACE CENTERED
# get the face location as 2 pairs of (x,y) - top right, bottom left
# 720 x 1280 height, width
from Freenove_Three_Wheeled_Smart_Car_Kit_for_Raspberry_Pi_Master.Server.mDev import *
from face_rec import FaceRecognizer

class Driver:
    centerBuffer = 50
    leftCenterBound = (1280 / 2) - centerBuffer
    rightCenterBound = (1280 / 2) + centerBuffer
    upperCenterBound = (720 / 2) + centerBuffer
    lowerCenterBound = (720 / 2) - centerBuffer

    def __init__(self, target, face_imgs, face_labels):
        self.recognizer = FaceRecognizer(face_imgs, face_labels)
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

        # if the face is to the right of our center bounds, move right
        if right > self.rightCenterBound:
            print("right")

        # if the face is to the left of our center bounds, move left
        if left < self.leftCenterBound:
            print("left")

        # if the face is above our center bounds, back up
        if top > self.upperCenterBound:
            print("up")

        # if the face is below our center bounds, move forward
        if bottom < self.lowerCenterBound:
            print("down")

