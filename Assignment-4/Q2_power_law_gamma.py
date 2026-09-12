import cv2
import numpy as np

# Read grayscale image
image = cv2.imread("../image.jpg", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: Unable to read image.jpg")
    exit()

# Input gamma value
gamma = float(input("Enter gamma value: "))

if gamma <= 0:
    print("Gamma must be greater than 0.")
    exit()

# Power-law transformation
# s = c * r^gamma, where c = 1
c = 1
normalized_image = image.astype(np.float32) / 255.0

gamma_image = c * np.power(normalized_image, gamma)

# Convert back to 0-255
gamma_image = np.uint8(np.clip(gamma_image * 255, 0, 255))

cv2.imshow("Original Image", image)
cv2.imshow("Power Law / Gamma Transformed Image", gamma_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
