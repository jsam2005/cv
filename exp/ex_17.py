# -*- coding: utf-8 -*-
"""ex-17: Watermarking — insert watermark into image effectively (OpenCV)."""

import cv2
import matplotlib.pyplot as plt
from local_io import get_image_path

image_path = get_image_path()
print(f"Using file: {image_path}")
image = cv2.imread(image_path)
if image is None:
    raise ValueError(f"Could not read image from '{image_path}'.")
h, w = image.shape[:2]

# 2. Create overlay and add text watermark (semi-transparent)
overlay = image.copy()
text = "  (c) Your Name  "
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1.2
thickness = 2
(text_size, _), _ = cv2.getTextSize(text, font, font_scale, thickness)
x = w - text_size - 20
y = h - 20
cv2.putText(overlay, text, (x, y), font, font_scale, (0, 0, 0), thickness + 2)
cv2.putText(overlay, text, (x, y), font, font_scale, (255, 255, 255), thickness)
alpha = 0.3
watermarked = cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0)

# 3. Display original and watermarked
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
watermarked_rgb = cv2.cvtColor(watermarked, cv2.COLOR_BGR2RGB)
fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(image_rgb)
axes[0].set_title("Original Image")
axes[0].axis("off")
axes[1].imshow(watermarked_rgb)
axes[1].set_title("With Watermark")
axes[1].axis("off")
plt.tight_layout()
plt.show()
