# -*- coding: utf-8 -*-
"""ex-8: Read image and dilate using Dilate function (OpenCV)."""

import cv2
import matplotlib.pyplot as plt
from local_io import get_image_path

image_path = get_image_path()
print(f"Using file: {image_path}")

# 2. Read the image
image = cv2.imread(image_path)
if image is None:
    raise ValueError(f"Could not read image from '{image_path}'.")

# 3. Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 4. Create kernel and apply dilation
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
dilated = cv2.dilate(gray, kernel)

# 5. Display original and dilated
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(image_rgb)
axes[0].set_title("Original Image")
axes[0].axis("off")
axes[1].imshow(dilated, cmap="gray")
axes[1].set_title("Dilated Image")
axes[1].axis("off")
plt.tight_layout()
plt.show()
