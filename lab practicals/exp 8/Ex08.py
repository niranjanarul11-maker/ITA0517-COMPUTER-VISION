import cv2
import numpy as np

# Read the image
image = cv2.imread("input.jpg")

# Create a kernel
kernel = np.ones((5, 5), np.uint8)

# Apply dilation
dilated = cv2.dilate(image, kernel, iterations=1)

# Save the output
cv2.imwrite("dilated.jpg", dilated)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Dilated Image", dilated)

cv2.waitKey(0)
cv2.destroyAllWindows()