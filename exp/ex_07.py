# -*- coding: utf-8 -*-
"""ex-7: Read captured video, display in normal / slow motion / fast motion (OpenCV)."""

import subprocess
import sys

import cv2
from local_io import get_video_path

video_path = get_video_path()
print(f"Using file: {video_path}")

cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    raise ValueError(f"Could not open video '{video_path}'.")

fps = cap.get(cv2.CAP_PROP_FPS) or 25.0
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*"mp4v")

frames = []
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)
cap.release()
print(f"Read {len(frames)} frames, {fps:.1f} fps, size {w}x{h}.")

slow_path = "output_slow_motion.mp4"
out_slow = cv2.VideoWriter(slow_path, fourcc, fps, (w, h))
for f in frames:
    out_slow.write(f)
    out_slow.write(f)
out_slow.release()

fast_path = "output_fast_motion.mp4"
out_fast = cv2.VideoWriter(fast_path, fourcc, fps, (w, h))
for f in frames[::2]:
    out_fast.write(f)
out_fast.release()

print(f"Original:   {video_path}")
print(f"Slow (2x):  {slow_path}")
print(f"Fast (2x):  {fast_path}")

if sys.platform == "darwin":
    for path in (video_path, slow_path, fast_path):
        subprocess.run(["open", path], check=False)
