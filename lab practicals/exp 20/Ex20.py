import cv2
import numpy as np

# Read image
image = cv2.imread("input.jpg")

# Create kernel
kernel = np.ones((5, 5), np.uint8)

# Apply dilation
dilated = cv2.dilate(image, kernel, iterations=1)

# Save output
cv2.imwrite("dilation.jpg", dilated)

# Display
cv2.imshow("Original Image", image)
cv2.imshow("Dilation", dilated)

cv2.waitKey(0)
cv2.destroyAllWindows()