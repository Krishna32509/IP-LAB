import cv2

# Read grayscale image
image = cv2.imread("../image.jpg", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: Unable to read image.jpg")
    exit()

# Input threshold from user
threshold = float(input("Enter threshold value (0-255): "))

if threshold < 0 or threshold > 255:
    print("Threshold must be between 0 and 255.")
    exit()

# Convert grayscale image to binary image
_, binary_image = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)

cv2.imshow("Grayscale Image", image)
cv2.imshow("Binary Image", binary_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
