import cv2

# Read grayscale image
image = cv2.imread("../image.jpg", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: Unable to read image.jpg")
    exit()

# Convert grayscale image to binary
threshold = float(input("Enter threshold for binary conversion (0-255): "))

if threshold < 0 or threshold > 255:
    print("Threshold must be between 0 and 255.")
    exit()

_, binary_image = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)

# Input border details
border_width = int(input("Enter border width in pixels: "))
border_color = int(input("Enter binary border color (0 for black, 255 for white): "))

if border_width < 0:
    print("Border width cannot be negative.")
    exit()

if border_color not in (0, 255):
    print("For a binary image, border color must be 0 or 255.")
    exit()

# Add border
bordered_image = cv2.copyMakeBorder(
    binary_image,
    border_width,
    border_width,
    border_width,
    border_width,
    cv2.BORDER_CONSTANT,
    value=border_color
)

cv2.imshow("Binary Image", binary_image)
cv2.imshow("Binary Image with Border", bordered_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
