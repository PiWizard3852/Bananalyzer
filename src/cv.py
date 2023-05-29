import cv2
import numpy as np

filepath = "../data/alphabet.png"
image = cv2.imread(filepath)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lowerLimit = np.array([17, 12, 0])
upperLimit = np.array([29, 255, 255])

tileMask = cv2.inRange(hsv, lowerLimit, upperLimit)
tiles = cv2.bitwise_and(image, image, mask=tileMask)

edgeMask = cv2.Canny(tiles, 100, 200)
edges = cv2.bitwise_and(image, image, mask=edgeMask)

contours, hierarchy = cv2.findContours(edgeMask,
                                       cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

cv2.drawContours(image, contours, -1, (0, 255, 0), 3)

# cnts = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# cnts = cnts[0] if len(result2) == 2 else cnts[1]

# for c in cnts:
#     cv2.drawContours(image,[c], 0, (0,255,0), 3)


cv2.imshow("Image", image)
cv2.waitKey(0)
