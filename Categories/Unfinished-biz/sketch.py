import cv2 
img = cv2.imread('img.jpg')
dst_gray, dst_color = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.05) 
# sigma_s and sigma_r are the same as in stylization.
# shade_factor is a simple scaling of the output image intensity. The higher the value, the brighter is the result. Range 0 - 0.1

