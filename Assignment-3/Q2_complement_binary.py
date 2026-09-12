import cv2

# Read grayscale image
image = cv2.imread("../image.jpg", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: Unable to read image.jpg")
    exit()

# Convert image to binary
threshold = float(input("Enter threshold for binary conversion (0-255): "))

if threshold < 0 or threshold > 255:
    print("Threshold must be between 0 and 255.")
    exit()

_, binary_image = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)

# Binary image complement
complement = 255 - binary_image

cv2.imshow("Binary Image", binary_image)
cv2.imshow("Binary Complement", complement)

cv2.waitKey(0)
cv2.destroyAllWindows()
