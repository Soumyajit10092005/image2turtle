import cv2, turtle
import sys, os.path
import numpy as np
import tkinter as tk
from PIL import Image

img_path = r"E:\MY IMAges\folder_01\Shivling CDR File Contact 9350235840.jpg"

# img_path = r"E:\MY IMAges\netaji111.jpg"

if not os.path.exists(img_path):
    sys.exit(f'File not found (please check file path)')

# Convert GIF to JPG(IF YOUR IMAGE IS GIF TYPE)

# if img_path.lower().endswith('.gif'):
#     jpg_path = img_path.replace('.gif', '.jpg')
#     try:
#         gif_image = Image.open(img_path)
#         # Convert RGBA to RGB if necessary
#         if gif_image.mode in ('RGBA', 'LA', 'P'):
#             rgb_image = Image.new('RGB', gif_image.size, (255, 255, 255))
#             rgb_image.paste(gif_image, mask=gif_image.split()[-1] if gif_image.mode == 'RGBA' else None)
#         else:
#             rgb_image = gif_image.convert('RGB')
#         rgb_image.save(jpg_path, 'JPEG')
#         img_path = jpg_path
#         print(f"GIF converted to JPG: {jpg_path}")
#     except Exception as e:
#         sys.exit(f'Error converting GIF: {e}')

# OtherWise
image = cv2.imread(img_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.GaussianBlur(image, (1,1), 0)
thresh_mean = cv2.adaptiveThreshold(
    image, 255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY_INV,
    17,2
)
kernel = np.ones((1,1), np.uint8)
closed_img = cv2.morphologyEx(thresh_mean, 
                              cv2.MORPH_CLOSE, kernel)

contours,_ = cv2.findContours(
    closed_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
sorted_contours = sorted(contours, key = cv2.contourArea, reverse = True)

t = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor('white')

# Comment out this part if you want to show formation of image (LIVE ACTION)
t.speed(0)
wn.tracer(0, 0)


t.pensize(1)
t.penup()

img_height, img_width = closed_img.shape
root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.destroy()

scale_x = screen_width / img_width
scale_y = screen_height / img_height
scale = min(scale_x, scale_y)
scale = scale * 0.9

for cnt in sorted_contours:
    if (cv2.contourArea(cnt) < 50) or len(cnt) < 3:
        continue
    x0 , y0 = cnt[0][0]
    t.goto(
        (x0 - img_width / 2) * scale,
        (img_height / 2 - y0) * scale
    )
    t.pendown()

    for point in cnt[1:]:
        x,y = point[0]
        t.goto(
            (x - img_width / 2) * scale,
            (img_height / 2 - y) * scale
        )
    t.goto(
        (x0 - img_width / 2) * scale,
        (img_height / 2 - y0) * scale
    )
    t.penup()

t.hideturtle()  
wn.update()

turtle.done()










