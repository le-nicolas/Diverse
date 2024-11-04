import cv2
import numpy as np

# Load and blur the image
image = cv2.imread('Cat03.jpg', cv2.IMREAD_GRAYSCALE)
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

# Perform edge detection
edges = cv2.Canny(blurred_image, threshold1=100, threshold2=200)

# Calculate the gradients
gradient_x = cv2.Sobel(blurred_image, cv2.CV_64F, 1, 0, ksize=5)
gradient_y = cv2.Sobel(blurred_image, cv2.CV_64F, 0, 1, ksize=5)

# Calculate the magnitude of the gradients
gradient_magnitude = np.sqrt(gradient_x**2 + gradient_y**2)

# Normalize the gradient magnitude to the range 0-255
gradient_magnitude = (gradient_magnitude / np.max(gradient_magnitude)) * 255

# Find contours in the edge image
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Define a function to calculate the "goodness" of a stroke
def calculate_goodness(contour):
    return cv2.arcLength(contour, True)

# Calculate the "goodness" of each stroke
goodness = [calculate_goodness(contour) for contour in contours]

# Sort the strokes by their "goodness", in descending order.
sorted_strokes = [stroke for _, stroke in sorted(zip(goodness, contours), reverse=True)]

# Create a blank image to draw the strokes on.
sketch = np.zeros_like(image)


# Draw the strokes.
for i, stroke in enumerate(sorted_strokes):
    # Calculate the relative rank of this stroke (from 0 to 1)
    rank = i / len(sorted_strokes)

    # Determine the color and thickness of the stroke based on its rank
    color = (255 * (1 - rank),)  # "Better" strokes are drawn in white
    thickness = int(5 * (1 - rank) + 1)  # "Better" strokes are drawn thicker

    cv2.drawContours(sketch, [stroke], -1, color, thickness)

# Display the images
cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', blurred_image)
cv2.imshow('Edges', edges)
cv2.imshow('Gradient Magnitude', gradient_magnitude)
cv2.imshow('Sketch', sketch)
cv2.waitKey(0)
cv2.destroyAllWindows()