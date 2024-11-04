import cv2
import numpy as np

# Load the image
image = cv2.imread('cute.jpg', cv2.IMREAD_GRAYSCALE)

# Check if the image was loaded successfully
if image is None:
    print('Could not open or find the image')
else:
    # Invert the image
    inverted_image = cv2.bitwise_not(image)

    # Apply Gaussian blur to the inverted image
    blurred_image = cv2.GaussianBlur(inverted_image, (13, 13), 0)

    # Invert the blurred image
    inverted_blurred_image = cv2.bitwise_not(blurred_image)

    # Blend the original image and the blurred image using a color dodge
    sketch = cv2.divide(image, inverted_blurred_image, scale=256.0)

    # Save the sketch image
    cv2.imwrite('output9.jpg', sketch)