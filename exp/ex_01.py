# -*- coding: utf-8 -*-
"""ex-1: Basic image handling — upload image and convert to grayscale."""

import cv2
import matplotlib.pyplot as plt
from local_io import get_image_path

# 1. Get image path (pass as argument or enter when prompted)
image_path = get_image_path()

# 2. Read the image
image = cv2.imread(image_path)
if image is None:
    raise ValueError(f"Could not read image from '{image_path}'.")

# 3. Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 4. Display both images (Colab has no cv2.imshow; use matplotlib)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].imshow(image_rgb)
axes[0].set_title("Original Image")
axes[0].axis("off")

axes[1].imshow(gray_image, cmap="gray")
axes[1].set_title("Grayscale Image")
axes[1].axis("off")

plt.tight_layout()
plt.show()
