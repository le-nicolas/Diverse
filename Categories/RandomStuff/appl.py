# application....
# algo for creating a pencil sketch from an image
# calculation - grad of an image is a 2d vector that points in the direction of the greatest rate of change in intensity ( pixel )
# we use edge detection algo like sobel operator

# find the high intens - thresholding the grad magnitude

# store paths of high intensity gradients as strokkes

# rank the strokes, base on their goodness (function of length and intensity)

#draw..... start with high-ranked strokes and ending with the lowest- ranked ones. 
#requires good understanding of image processing and graphics
# identifies points in a digital image where the image brightness changes sharply or has discontinuities
#Understanding how edge detection works is crucial because it helps in identifying the boundaries of objects within images, which in this case, helps in identifying where the strokes should be placed.

import cv2
import numpy as np

# Load the image
#image = cv2.imread('cute.jpg', cv2.IMREAD_GRAYSCALE)

# Detect edges in the image
#edges = cv2.Canny(image, threshold1=30, threshold2=100)

# Dilate the edges to create the sketch effect
#dilated_edges = cv2.dilate(edges, (1, 1), iterations=2)

# Invert the dilated edges to get the pencil sketch
#sketch = cv2.bitwise_not(dilated_edges)

# Save the pencil sketch image
#cv2.imwrite('output2.jpg', sketch)

# Invert the image
#image_inv = cv2.bitwise_not(image)

# Apply a Gaussian blur
#image_blur = cv2.GaussianBlur(image_inv, (13,13),0)

# Invert the blurred image
#image_blur_inv = cv2.bitwise_not(image_blur)

# Create the pencil sketch image
#image_sketch = cv2.divide(image, image_blur_inv, scale=256.0)

# Save the pencil sketch image
#cv2.imwrite('output.jpg', image_sketch)



# Load the image
image = cv2.imread('cute.jpg', cv2.IMREAD_GRAYSCALE)

# Calculate the x and y gradients using the Sobel operator
grad_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
grad_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)

# Calculate the magnitude and direction of the gradients
mag, angle = cv2.cartToPolar(grad_x, grad_y, angleInDegrees=True)

# Threshold the magnitudes
_, mask = cv2.threshold(mag, 150, 255, cv2.THRESH_BINARY)

# Create a black image to draw the strokes on
sketch = np.zeros_like(image)

# Draw the strokes on the sketch
for y in range(0, image.shape[0], 7):
    for x in range(0, image.shape[1], 7):
        if mask[y, x] == 255:
            cv2.line(sketch, (x, y), (x + int(5 * np.cos(angle[y, x])), y + int(5 * np.sin(angle[y, x]))), 150, 1)

# Save the pencil sketch image
cv2.imwrite('output6.jpg', sketch)