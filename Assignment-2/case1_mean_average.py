import cv2
import numpy as np

# Read color image
image = cv2.imread("../image.jpg")

if image is None:
    print("Error: Unable to read image.jpg")
    exit()

# OpenCV stores color images as BGR
b, g, r = cv2.split(image)

# Mean average of the three color planes
gray_image = ((r.astype(np.float32) +
               g.astype(np.float32) +
               b.astype(np.float32)) / 3)

gray_image = np.uint8(gray_image)

cv2.imshow("RGB Image", image)
cv2.imshow("Grayscale Image", gray_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
