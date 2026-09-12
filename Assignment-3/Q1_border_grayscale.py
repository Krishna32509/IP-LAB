import cv2

# Read grayscale image
image = cv2.imread("../image.jpg", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: Unable to read image.jpg")
    exit()

# Input border details
border_width = int(input("Enter border width in pixels: "))
border_color = int(input("Enter border color (0-255): "))

if border_width < 0:
    print("Border width cannot be negative.")
    exit()

if border_color < 0 or border_color > 255:
    print("Border color must be between 0 and 255.")
    exit()

# Add border
bordered_image = cv2.copyMakeBorder(
    image,
    border_width,
    border_width,
    border_width,
    border_width,
    cv2.BORDER_CONSTANT,
    value=border_color
)

cv2.imshow("Original Grayscale Image", image)
cv2.imshow("Image with Border", bordered_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
