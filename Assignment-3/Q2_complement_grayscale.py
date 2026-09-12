import cv2

# Read grayscale image
image = cv2.imread("../image.jpg", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: Unable to read image.jpg")
    exit()

# Grayscale image complement
complement = 255 - image

cv2.imshow("Original Grayscale Image", image)
cv2.imshow("Grayscale Complement", complement)

cv2.waitKey(0)
cv2.destroyAllWindows()
