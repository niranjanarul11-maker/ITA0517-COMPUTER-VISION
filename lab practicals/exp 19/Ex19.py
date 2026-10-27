import cv2
import numpy as np

# Read image
image = cv2.imread("input.jpg")

# Create kernel
kernel = np.ones((5, 5), np.uint8)

# Apply erosion
eroded = cv2.erode(image, kernel, iterations=1)

# Save output
cv2.imwrite("erosion.jpg", eroded)

# Display
cv2.imshow("Original Image", image)
cv2.imshow("Erosion", eroded)

cv2.waitKey(0)
cv2.destroyAllWindows()