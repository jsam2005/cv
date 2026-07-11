# -*- coding: utf-8 -*-
"""ex-10: Rotate image 90° clockwise (OpenCV)."""

import cv2
import matplotlib.pyplot as plt
from local_io import get_image_path

image_path = get_image_path()
print(f"Using file: {image_path}")

image = cv2.imread(image_path)
if image is None:
    raise ValueError(f"Could not read image from '{image_path}'.")

rot_90 = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
rot_90_rgb = cv2.cvtColor(rot_90, cv2.COLOR_BGR2RGB)

fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].imshow(image_rgb)
axes[0].set_title("Original")
axes[0].axis("off")
axes[1].imshow(rot_90_rgb)
axes[1].set_title("90° clockwise")
axes[1].axis("off")
plt.tight_layout()
plt.show()
