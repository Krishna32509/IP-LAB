import cv2
import numpy as np

# Read color image
image = cv2.imread("../image.jpg")

if image is None:
    print("Error: Unable to read image.jpg")
    exit()

# OpenCV stores color images as BGR
b, g, r = cv2.split(image)

# Input weightages from user
r_weight = float(input("Enter weightage of R (0-1): "))
g_weight = float(input("Enter weightage of G (0-1): "))
b_weight = float(input("Enter weightage of B (0-1): "))

# Validate weightages
if not (0 <= r_weight <= 1 and
        0 <= g_weight <= 1 and
        0 <= b_weight <= 1):
    print("Each weightage must be between 0 and 1.")
    exit()

if not np.isclose(r_weight + g_weight + b_weight, 1.0):
    print("The sum of R, G and B weightages must be equal to 1.")
    exit()

# Weighted grayscale conversion
gray_image = (r_weight * r.astype(np.float32) +
              g_weight * g.astype(np.float32) +
              b_weight * b.astype(np.float32))

gray_image = np.uint8(np.clip(gray_image, 0, 255))

cv2.imshow("RGB Image", image)
cv2.imshow("Grayscale Image", gray_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
