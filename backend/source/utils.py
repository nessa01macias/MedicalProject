import cv2
# using computer-vision to pre-process the imagen
import numpy as np


# for array-handling

def preprocessing_images(image):
    # image comes in and array comes out
    image_gray = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(image_gray, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)
    # we need adaptive thresholding because there are many shade colors in the image
    processed = cv2.adaptiveThreshold(
        resized, 255,
        # specify that it is the adaptive threst
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        # and that the pic going to be white&black
        cv2.THRESH_BINARY,
        # block size of the black area
        61,
        # constant
        11
    )
    return processed
