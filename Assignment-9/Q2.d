import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
image = cv2.imread(input("Enter image path: "),
                   cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Image not found!")
    exit()

# Generate Gaussian noise
gaussian_noise = np.random.normal(0, 20, image.shape)
gaussian_noisy = np.clip(
    image.astype(float) + gaussian_noise, 0, 255
).astype(np.uint8)

# Generate Speckle noise
speckle_noise = np.random.normal(0, 0.2, image.shape)
speckle_noisy = np.clip(
    image.astype(float) + image.astype(float) * speckle_noise,
    0, 255
).astype(np.uint8)

# Apply bilateral filter
gaussian_denoised = cv2.bilateralFilter(
    gaussian_noisy, 5, 75, 75
)

speckle_denoised = cv2.bilateralFilter(
    speckle_noisy, 5, 75, 75
)

# Display results
plt.figure(figsize=(12, 8))

images = [
    image,
    gaussian_noisy,
    gaussian_denoised,
    speckle_noisy,
    speckle_denoised
]

titles = [
    "Original Image",
    "Gaussian Noisy",
    "Gaussian Bilateral",
    "Speckle Noisy",
    "Speckle Bilateral"
]

for i in range(5):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis("off")

plt.tight_layout()
plt.show()
