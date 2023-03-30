# image resizer

import cv2

image = cv2.imread("AI.jpg") # take original image as input
cv2.imshow("Image" , image) # print the image

# percent by which the image is resized
percent = 50 # lets take 50 percent

# take 50 percent of the original image

width = int((image.shape[1] * percent) / 100)
height = int((image.shape[0] * percent) / 100)

# resize image
rSize = cv2.resize(image , (width , height))

cv2.imwrite("newIMage.png" , rSize) # store the resize image in a new file
cv2.waitKey(0)
