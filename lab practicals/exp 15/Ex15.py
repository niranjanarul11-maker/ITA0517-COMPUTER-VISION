import cv2
import numpy as np

# Read the image
image = cv2.imread("input.jpg")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Convert to float32
gray = np.float32(gray)

# Harris corner detection
corners = cv2.cornerHarris(gray, 2, 3, 0.04)

# Dilate the corners to make them visible
corners = cv2.dilate(corners, None)

# Mark the corners in red
image[corners > 0.01 * corners.max()] = [0, 0, 255]

# Save the output
cv2.imwrite("harris_corners.jpg", image)

# Display
cv2.imshow("Harris Corner Detection", image)

cv2.waitKey(0)
cv2.destroyAllWindows()