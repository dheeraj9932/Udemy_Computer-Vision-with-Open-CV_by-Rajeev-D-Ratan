#!/usr/bin/env python
# coding: utf-8

# ## Blob Detection

# In[9]:


# Standard imports
import cv2
import numpy as np;
 
# Read image
image = cv2.imread("images/Sunflowers.jpg", 0)
cv2.imshow("Blobs", image)
cv2.waitKey(0)
#cv2.destroyAllWindows()
print("1")
# Set up the detector with default parameters.
detector = cv2.SimpleBlobDetector()
print("2")
# Detect blobs.
keypoints = detector.detect(image)
print("3")
# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of
# the circle corresponds to the size of blob
blank = np.zeros((1,1)) 
print("4")
cv2.drawKeypoints(image, keypoints, blank, (0,255,255), cv2.DRAW_MATCHES_FLAGS_DEFAULT)
 
# Show keypoints
cv2.imshow("Blobs", image)
print("5")
cv2.waitKey(0)
cv2.destroyAllWindows()


# The function **cv2.drawKeypoints** takes the following arguments:
# 
# **cv2.drawKeypoints**(input image, keypoints, blank_output_array, color, flags)
# 
# flags:
# - cv2.DRAW_MATCHES_FLAGS_DEFAULT
# - cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
# - cv2.DRAW_MATCHES_FLAGS_DRAW_OVER_OUTIMG
# - cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS

# 

# In[3]:
'''
# Standard imports
import cv2
import numpy as np;

# Read image
im = cv2.imread("images/Sunflowers.jpg", cv2.IMREAD_GRAYSCALE)

# Set up the detector with default parameters.
detector = cv2.SimpleBlobDetector()

# Detect blobs.
keypoints = detector.detect(im)

# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Show keypoints
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)
'''

