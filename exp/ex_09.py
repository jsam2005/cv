# -*- coding: utf-8 -*-
"""ex-9: Image scaling — resize to bigger and smaller sizes (OpenCV)."""

import cv2
import matplotlib.pyplot as plt
from local_io import get_image_path

image_path = get_image_path()
print(f"Using file: {image_path}")

# 2. Read the image
image = cv2.imread(image_path)
if image is None:
    raise ValueError(f"Could not read image from '{image_path}'.")

h, w = image.shape[:2]

# 3. Scale down (50% of original)
small_w, small_h = int(w * 0.5), int(h * 0.5)
image_small = cv2.resize(image, (small_w, small_h), interpolation=cv2.INTER_AREA)

# 4. Scale up (150% of original)
big_w, big_h = int(w * 1.5), int(h * 1.5)
image_big = cv2.resize(image, (big_w, big_h), interpolation=cv2.INTER_LINEAR)

# 5. Display original, smaller, and bigger
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
small_rgb = cv2.cvtColor(image_small, cv2.COLOR_BGR2RGB)
big_rgb = cv2.cvtColor(image_big, cv2.COLOR_BGR2RGB)

fig, axes = plt.subplots(1, 3, figsize=(14, 5))
axes[0].imshow(small_rgb)
axes[0].set_title(f"Smaller (50%)\n{small_w}x{small_h}")
axes[0].axis("off")
axes[1].imshow(image_rgb)
axes[1].set_title(f"Original\n{w}x{h}")
axes[1].axis("off")
axes[2].imshow(big_rgb)
axes[2].set_title(f"Bigger (150%)\n{big_w}x{big_h}")
axes[2].axis("off")
plt.tight_layout()
plt.show()
