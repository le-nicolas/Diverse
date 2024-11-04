import cv2
import numpy as np

# Load the image
image = cv2.imread('Cat03.jpg', cv2.IMREAD_GRAYSCALE)

# Check if the image was loaded successfully
if image is None:
    print('Could not open or find the image')
else:
    # Apply Gaussian blur to the image
    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

    # Apply Canny edge detection
    edges = cv2.Canny(blurred_image, threshold1=100, threshold2=200)

    # Calculate the x and y gradients using the Sobel operator
    grad_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
    grad_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

    # Calculate the magnitude of the gradients
    gradient_magnitude = np.sqrt(grad_x**2 + grad_y**2)

    # Normalize the gradient magnitude to the range 0-255
    gradient_magnitude = (gradient_magnitude / np.max(gradient_magnitude)) * 255


    # Calculate the magnitude and direction of the gradients
    mag, angle = cv2.cartToPolar(grad_x, grad_y, angleInDegrees=True)

    # Threshold the magnitudes
    _, mask = cv2.threshold(mag, 100, 255, cv2.THRESH_BINARY)

    # Combine the edges and the gradient directions
    combined = np.bitwise_or(edges, mask.astype(np.uint8))

    # Invert the combined image to get a sketch-like effect
    sketch = cv2.bitwise_not(combined)

    # Resize the image
    resized_sketch = cv2.resize(sketch, (700, 100))  # Change the dimensions as needed

    # Save the sketch image
    cv2.imwrite('output12.jpg', sketch)

cv2.imshow('Sketch', resized_sketch)
cv2.waitKey(0)
cv2.destroyAllWindows()    