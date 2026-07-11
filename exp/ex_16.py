# -*- coding: utf-8 -*-
"""ex-16: Sobel algorithm to filter the input image (OpenCV)."""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from local_io import get_image_path

image_path = get_image_path()
print(f"Using file: {image_path}")

# 2. Read the image and convert to grayscale
image = cv2.imread(image_path)
if image is None:
    raise ValueError(f"Could not read image from '{image_path}'.")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 3. Sobel filters
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
sobel_mag = np.sqrt(sobel_x**2 + sobel_y**2)
sobel_mag = np.uint8(np.clip(sobel_mag, 0, 255))

# 4. Display original and Sobel results
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
fig, axes = plt.subplots(2, 2, figsize=(10, 10))
axes[0, 0].imshow(image_rgb)
axes[0, 0].set_title("Original Image")
axes[0, 0].axis("off")
axes[0, 1].imshow(sobel_x, cmap="gray")
axes[0, 1].set_title("Sobel X (horizontal edges)")
axes[0, 1].axis("off")
axes[1, 0].imshow(sobel_y, cmap="gray")
axes[1, 0].set_title("Sobel Y (vertical edges)")
axes[1, 0].axis("off")
axes[1, 1].imshow(sobel_mag, cmap="gray")
axes[1, 1].set_title("Sobel Magnitude")
axes[1, 1].axis("off")
plt.tight_layout()
plt.show()
