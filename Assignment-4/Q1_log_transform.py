import cv2
import numpy as np

# Read grayscale image
image = cv2.imread("../image.jpg", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: Unable to read image.jpg")
    exit()

# Log transformation
# s = c * log(1 + r), where c = 1
c = 1
image_float = image.astype(np.float32)

log_image = c * np.log1p(image_float)

# Normalize result to 0-255
log_image = cv2.normalize(
    log_image,
    None,
    0,
    255,
    cv2.NORM_MINMAX
)

log_image = np.uint8(log_image)

cv2.imshow("Original Image", image)
cv2.imshow("Log Transformed Image", log_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
