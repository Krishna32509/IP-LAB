import cv2
import numpy as np

# Read grayscale image
image = cv2.imread("../image.jpg", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: Unable to read image.jpg")
    exit()

# Input ranges
input_low = int(input("Enter input range lower value (0-255): "))
input_high = int(input("Enter input range upper value (0-255): "))
output_low = int(input("Enter output range lower value (0-255): "))
output_high = int(input("Enter output range upper value (0-255): "))

# Validate input
if not (0 <= input_low <= 255 and
        0 <= input_high <= 255 and
        0 <= output_low <= 255 and
        0 <= output_high <= 255):
    print("All intensity values must be between 0 and 255.")
    exit()

if input_low >= input_high:
    print("Input lower value must be less than input upper value.")
    exit()

if output_low > output_high:
    print("Output lower value must not be greater than output upper value.")
    exit()

# Intensity-level slicing / contrast stretching
output_image = image.astype(np.float32)

mask = (image >= input_low) & (image <= input_high)

output_image[mask] = (
    output_low
    + ((image[mask].astype(np.float32) - input_low)
       * (output_high - output_low)
       / (input_high - input_low))
)

output_image = np.uint8(np.clip(output_image, 0, 255))

cv2.imshow("Original Image", image)
cv2.imshow("Intensity Level Sliced Image", output_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
