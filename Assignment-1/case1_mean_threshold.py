import cv2
import numpy as np

# Read grayscale image
image = cv2.imread("../image.jpg", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: Unable to read image.jpg")
    exit()

# Calculate mean intensity and use it as threshold
threshold = np.mean(image)

# Convert grayscale image to binary image
_, binary_image = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)

print("Mean intensity (threshold):", threshold)

cv2.imshow("Grayscale Image", image)
cv2.imshow("Binary Image", binary_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
