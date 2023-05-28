import cv2
import numpy as np

filepath = "../data/alphabet.png"
image = cv2.imread(filepath)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_tan = np.array([20,  0, 0])
upper_tan = np.array([25, 255, 255])

mask = cv2.inRange(hsv, lower_tan, upper_tan)

result = cv2.bitwise_and(image, image, mask = mask)
edges = cv2.Canny(result,100,200)

result2 = cv2.bitwise_and(image, image, mask = edges)

contours, hierarchy = cv2.findContours(edges, 
    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

cv2.drawContours(image, contours, -1, (0, 255, 0), 3)


# cnts = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# cnts = cnts[0] if len(result2) == 2 else cnts[1]

# for c in cnts:
#     cv2.drawContours(image,[c], 0, (0,255,0), 3)



cv2.imshow("Im", image)
cv2.waitKey(0)