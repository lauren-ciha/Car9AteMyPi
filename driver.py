# MOVE THE ROBOT TO KEEP THE FACE CENTERED
# get the face location as 2 pairs of (x,y) - top right, bottom left
# 720 x 1280 height, width
class driver():
    centerBuffer = 100
    leftCenterBound = (1280 / 2) - centerBuffer
    rightCenterBound = (1280 / 2) + centerBuffer
    upperCenterBound = (720 / 2) + centerBuffer
    lowerCenterBound = (720 / 2) - centerBuffer

    # get the location of the face from the facial recognition


    # if the face is to the right of our center bounds, move right
    if right > rightCenterBound:

    # if the face is to the left of our center bounds, move left
    if left < leftCenterBound:

    # if the face is above our center bounds
    if top > upperCenterBound:

    # if the face is below our center bounds
    if bottom < lowerCenterBound: