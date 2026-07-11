# -*- coding: utf-8 -*-
"""ex-15: Read image and detect corners using Harris Corner Detection (OpenCV)."""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from local_io import get_image_path

image_path = get_image_path()
print(f"Using file: {image_path}")

# 2. Read the image
image = cv2.imread(image_path)
if image is None:
    raise ValueError(f"Could not read image from '{image_path}'.")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_float = np.float32(gray)

# 3. Harris Corner Detection
harris = cv2.cornerHarris(gray_float, blockSize=2, ksize=3, k=0.04)

# 4. Mark corners
harris_dilate = cv2.dilate(harris, None)
thresh = 0.01 * harris_dilate.max()
image_with_corners = image.copy()
image_with_corners[harris_dilate > thresh] = [0, 0, 255]

# 5. Display original and image with detected corners
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
corners_rgb = cv2.cvtColor(image_with_corners, cv2.COLOR_BGR2RGB)
fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(image_rgb)
axes[0].set_title("Original Image")
axes[0].axis("off")
axes[1].imshow(corners_rgb)
axes[1].set_title("Harris Corner Detection")
axes[1].axis("off")
plt.tight_layout()
plt.show()
