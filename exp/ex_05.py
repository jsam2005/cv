# -*- coding: utf-8 -*-
"""ex-5: Analyze histogram by color levels (B, G, R) using OpenCV."""

import cv2
import matplotlib.pyplot as plt
from local_io import get_image_path


def analyze_histogram_color(image):
    """Analyze and plot the histogram of an image based on color levels (B, G, R)."""
    if image is None:
        raise ValueError("Image is None.")
    channels = cv2.split(image)
    channel_names = ("Blue", "Green", "Red")
    colors = ("b", "g", "r")
    histograms = []
    for ch, name, color in zip(channels, channel_names, colors):
        hist = cv2.calcHist([ch], [0], None, [256], [0, 256])
        histograms.append((name, hist, color))
    return histograms


image_path = get_image_path()
print(f"Using file: {image_path}")
image = cv2.imread(image_path)
if image is None:
    raise ValueError(f"Could not read image from '{image_path}'.")

# Analyze and plot
hists = analyze_histogram_color(image)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

fig, axes = plt.subplots(2, 1, figsize=(10, 8))
axes[0].imshow(image_rgb)
axes[0].set_title("Input Image")
axes[0].axis("off")
for name, hist, color in hists:
    axes[1].plot(hist, color=color, label=name, alpha=0.7)
axes[1].set_title("Histogram by Color Level (B, G, R)")
axes[1].set_xlabel("Pixel value (0–255)")
axes[1].set_ylabel("Count")
axes[1].legend()
axes[1].set_xlim([0, 256])
plt.tight_layout()
plt.show()
