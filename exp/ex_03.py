# -*- coding: utf-8 -*-
"""ex-3: Read image from user and show outline using Canny."""

import cv2
import matplotlib.pyplot as plt
from local_io import get_image_path

image_path = get_image_path()
print(f"Using file: {image_path}")

# 2. Read the image
image = cv2.imread(image_path)
if image is None:
    raise ValueError(f"Could not read image from '{image_path}'.")

# 3. Convert to grayscale (Canny works on single channel)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 4. Canny edge detection (outline)
edges = cv2.Canny(gray, 50, 150)

# 5. Display original and outline
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(image_rgb)
axes[0].set_title("Original Image")
axes[0].axis("off")
axes[1].imshow(edges, cmap="gray")
axes[1].set_title("Outline (Canny Edges)")
axes[1].axis("off")
plt.tight_layout()
plt.show()
