# 🎨 Image to Turtle Sketcher



An automated Python script that takes any image, processes its contours using **OpenCV**, and reconstructs it as a vector-style drawing using the **Turtle** graphics library.

---

## ✨ Features
*   **Edge Detection:** Uses Adaptive Gaussian Thresholding for high-detail contour extraction.
*   **Auto-Scaling:** Automatically scales the drawing to fit your monitor resolution using `Tkinter`.
*   **Optimization:** Uses `morphologyEx` to close gaps in lines for a cleaner sketch.
*   **Fast Rendering:** Utilizes `wn.tracer(0,0)` for near-instant rendering of complex images.

## 🚀 How to Use

### 1. Prerequisites
Ensure you have Python installed, then install the required libraries:
```bash
pip install opencv-python numpy pillow tkinter sys
